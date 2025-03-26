from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DECIMAL, Text, ForeignKey, Date
from sqlalchemy.orm import relationship

Base = declarative_base()

# class PetProfile(Base):
#     ___tablename___ = "Pet_Profile"
#     Pet_ID = Column(Integer, primary_key=True, index=True)
#     Pet_Name = Column(String(50), nullable=False)
#     Pet_Photo = Column(String(255))  # URL or file path to the pet's photo
#     Breed = Column(String(30), nullable=False)
#     Age = Column(Integer, nullable=False)

class PetProfile(Base):
    __tablename__ = "Pet_Profile"
    Pet_ID = Column(Integer, primary_key=True, index=True)
    Pet_Name = Column(String(50), nullable=False)
    Pet_Photo = Column(String(255))  # URL or file path to the pet's photo
    Breed = Column(String(30), nullable=False)
    Age = Column(Integer, nullable=False)
    Weight = Column(DECIMAL(5,2))
    Medical_Condition = Column(String(255))
    
    # Relationships (one-to-one)
    behavior = relationship("PetBehavior", back_populates="pet", uselist=False)
    vaccination = relationship("VaccinationRecord", back_populates="pet", uselist=False)

class PetBehavior(Base):
    __tablename__ = "Pet_Behavior"
    Behavior_ID = Column(Integer, primary_key=True)
    Pet_ID = Column(Integer, ForeignKey("Pet_Profile.Pet_ID"), nullable=False)
    Energy_Level = Column(String(50))
    Training_Status = Column(String(50), nullable=False)
    Compatibility = Column(String(50))
    Behavioral_Notes = Column(Text)
    
    pet = relationship("PetProfile", back_populates="behavior")

class VaccinationRecord(Base):
    __tablename__ = "Vaccination_Record"
    Vaccination_ID = Column(Integer, primary_key=True)
    Pet_ID = Column(Integer, ForeignKey("Pet_Profile.Pet_ID"), nullable=False)
    Vaccination_Status = Column(String(255))
    Vaccination_Details = Column(Text)
    Last_Vaccination_Date = Column(Date)
    Next_Appointment_Date = Column(Date)
    
    pet = relationship("PetProfile", back_populates="vaccination")
