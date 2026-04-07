from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel, Field


app= FastAPI(
    title="Yoo",
    description="REST API",
    version="1.0.0"
)

fake_db: dict[int, dict]= {
    1: {"id":1, "name": "Rishi", "age":21},
    2: {"id":2, "name": "Chintu", "age":20},
    3: {"id":3, "name": "Mohith ", "age":21},
    4: {"id":4, "name": "Lohitaksha ", "age":20},
    5: {"id":5, "name": "DK ", "age":21},

}

next_id=6

class UserCreate(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    age:  int  = Field(gt=0, lt=120)


class UserUpdate(BaseModel) :
    name: Optional[str] = None
    age: Optional[int] = None

class UserResponse(BaseModel) :
    id: int
    name:str
    age:int

#ROUTES

@app.get("/")
def root () :
    return {"message":"API is Running..."}


@app.get("/users", response_model=list[UserResponse])
def get_users():
    return list(fake_db.values())


@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail="User not found")
    return fake_db[user_id]

@app.post("/users", response_model=UserResponse, status_code=201) 
def create_user(user: UserCreate) :
    global next_id
    new_user = {"id": next_id, "name" : user.name, "age": user.age}
    fake_db[next_id]= new_user
    next_id+=1
    return new_user


@app.patch("/users/{user_id}", response_model=UserResponse)
def update_user(user_id:int, updates: UserUpdate) :
    if user_id not in fake_db :
        raise HTTPException(status_code=404, detail="User not found")
    stored = fake_db[user_id]
    if updates.name is not None :
        stored["name"]= updates.name
    if updates.age is not None :
        stored["age"]=updates.age
    return stored


@app.delete("/users/{user_id}")
def delete_user(user_id: int ) :
    if user_id not in fake_db :
        raise HTTPException(status_code=404, detail="User not found")
    del fake_db[user_id]
    return{"message": f"User {user_id} deleted"}



