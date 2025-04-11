from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import UserEnrollRequest, UserEnrollResponse, ScoreCard, CommunityScore
from database import enroll_user, get_score_card, join_my_community

app = FastAPI()

# Allow frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.put("/api/add_insurance", response_model=UserEnrollResponse)
def enroll_to_community(user: UserEnrollRequest):
    try:
        enrollment_id = enroll_user(user.model_dump())
        return {"status": "SUCCESS", "enrollmentId": enrollment_id}
    except Exception as e:
        print(f"Enrollment failed: {e}")
        return {"status": "FAILURE"}

@app.get("/api/join_community", response_model=list[ScoreCard])
def join_community():
    return join_my_community()

@app.get("/api/show_my_score", response_model=list[CommunityScore])
def get_my_score():
    return get_score_card()
