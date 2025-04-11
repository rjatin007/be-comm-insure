import json
import uuid

DB_FILE = "data.json"

def read_db():
    with open(DB_FILE, "r") as f:
        return json.load(f)

def write_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=2)

def enroll_user(user_data):
    db = read_db()
    enrollment_id = str(uuid.uuid4())
    new_user = {"id": enrollment_id, **user_data}
    db["users"].append(new_user)
    write_db(db)
    return enrollment_id

def get_score_card():
    return read_db().get("scoreCards", [])

def join_my_community():
    return sorted(read_db().get("communities", []), key=lambda x: x["score"], reverse=True)
