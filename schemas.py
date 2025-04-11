from pydantic import BaseModel
from typing import List

class Vehicle(BaseModel):
    make: str
    model: str
    year: int

class Insurance(BaseModel):
    provider: str
    policy_number: str

class UserEnrollRequest(BaseModel):
    name: str
    address: str
    vehicles: List[Vehicle]
    dependents: List[str]
    drivingLicenses: List[str]
    currentInsurance: List[Insurance]
    typeOfInsurance: str

class UserEnrollResponse(BaseModel):
    status: str
    enrollmentId: str = None

class ScoreCard(BaseModel):
    parameter: str
    score: int

class CommunityScore(BaseModel):
    community: str
    score: int
