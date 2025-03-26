from pydantic import BaseModel
from typing import Optional

# Schema for pet cards (first query)
class PetCard(BaseModel):
    Pet_ID: int
    Pet_Name: str
    Pet_Photo: Optional[str] = None  # URL or image path
    Breed: str
    Age: int

    class Config:
        orm_mode = True
        
# Schema for full pet details (detailed view)
class PetFullDetail(BaseModel):
    Pet_Name: str
    Breed: str
    Age: int
    Weight: Optional[float] = None
    Good_With: Optional[str] = None         # Maps from Pet_Behavior.Compatibility
    Behavioral_Notes: Optional[str] = None    # Maps from Pet_Behavior.Behavioral_Notes
    Vaccination_Status: Optional[str] = None   # Maps from Vaccination_Record.Vaccination_Status
    Medical_Condition: Optional[str] = None    # Maps from Pet_Profile.Medical_Condition
    Energy_Level: Optional[str] = None         # Maps from Pet_Behavior.Energy_Level
    Training_Status: Optional[str] = None      # Maps from Pet_Behavior.Training_Status
    Pet_Photo: Optional[str] = None

    class Config:
        orm_mode = True