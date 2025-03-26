from fastapi import FastAPI, HTTPException
from typing import List
from app.database import SessionLocal, engine
from app import models, schemas
from app.models import PetProfile
from app.schemas import PetCard, PetFullDetail
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins; adjust for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/pets", response_model=List[PetCard])
def get_pets():
    db = SessionLocal()
    try:
        results = db.query(
            PetProfile.Pet_ID,
            PetProfile.Pet_Name,
            PetProfile.Pet_Photo,
            PetProfile.Breed,
            PetProfile.Age
        ).all()
        
        pet_cards = [
            {
                "Pet_ID": pet.Pet_ID,
                "Pet_Name": pet.Pet_Name,
                "Pet_Photo": pet.Pet_Photo,
                "Breed": pet.Breed,
                "Age": pet.Age
            }
            for pet in results
        ]
        return pet_cards
    except Exception as e:
        # Log the error to the console
        print("Error in /pets endpoint:", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
    finally:
        db.close()

# Endpoint for full pet details (/pets/{pet_id}/details)
@app.get("/pets/{pet_id}/details", response_model=schemas.PetFullDetail)
def get_pet_full_details(pet_id: int):
    db = SessionLocal()
    try:
        # Build the join query based on your SQL:
        # SELECT 
        #    pp.Pet_Name,
        #    pp.Breed,
        #    pp.Age,
        #    pp.Weight,
        #    pb.Compatibility AS "Good_With",
        #    pb.Behavioral_Notes,
        #    vr.Vaccination_Status,
        #    pp.Medical_Condition,
        #    pb.Energy_Level,
        #    pb.Training_Status,
        #    pp.Pet_Photo
        # FROM Pet_Profile pp
        # JOIN Pet_Behavior pb ON pp.Pet_ID = pb.Pet_ID
        # JOIN Vaccination_Record vr ON pp.Pet_ID = vr.Pet_ID;
        result = (
            db.query(
                models.PetProfile.Pet_Name,
                models.PetProfile.Breed,
                models.PetProfile.Age,
                models.PetProfile.Weight,
                models.PetBehavior.Compatibility.label("Good_With"),
                models.PetBehavior.Behavioral_Notes,
                models.VaccinationRecord.Vaccination_Status,
                models.PetProfile.Medical_Condition,
                models.PetBehavior.Energy_Level,
                models.PetBehavior.Training_Status,
                models.PetProfile.Pet_Photo
            )
            .join(models.PetBehavior, models.PetProfile.Pet_ID == models.PetBehavior.Pet_ID)
            .join(models.VaccinationRecord, models.PetProfile.Pet_ID == models.VaccinationRecord.Pet_ID)
            .filter(models.PetProfile.Pet_ID == pet_id)
            .first()
        )
        if result is None:
            raise HTTPException(status_code=404, detail="Pet not found")
        return result._asdict()
    except Exception as e:
        print("Error in /pets/{pet_id}/details endpoint:", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
    finally:
        db.close()