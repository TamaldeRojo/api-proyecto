from typing import Union
from fastapi import FastAPI 
from config.db import conn
import json

from schemas.user import userModel,usersModel
from schemas.exercise import exerciseModel,exercisesModel

from models.user import User
from models.exercise import Exercise

from bson.objectid import ObjectId
from passlib.hash import sha256_crypt

app = FastAPI()

@app.get('/')
def read_root():
    urls = """{
        "usersGET":"/users",
        "usersPOST":"/users",
        "usersGET_ID":"/users/id",
        "exercisesGET":"/exercises",
        "exercisesPOST":"/exercises",
        "exercisesGET_ID":"/exercise/id"
        }"""
    json_urls = json.loads(urls)
    return json_urls

@app.get('/users')
def users():
    return usersModel(conn.MoveFit.Users.find())

@app.post('/users')
def users(user: User):
    newUser = dict(user)
    newUser["password"] = sha256_crypt.encrypt(newUser['password'])
    userid = conn.MoveFit.Users.insert_one(newUser).inserted_id
    createdUser = conn.MoveFit.Users.find({"_id":ObjectId(str(userid))})
    return usersModel(createdUser)

@app.get('/user/{id}')
def user(id: str):
    return userModel(conn.MoveFit.Users.find_one({"_id":ObjectId(str(id))}))


@app.get('/exercises')
def getExercise():
    return exercisesModel(conn.MoveFit.Exercises.find())

@app.post('/exercises')
def postExcercise(Exercise: Exercise):
    newExercise = dict(Exercise)
    ExerciseID = conn.MoveFit.Exercises.insert_one(newExercise).inserted_id
    theExerciseData = conn.MoveFit.Exercises.find({"_id":ObjectId(str(ExerciseID))})
    print(ExerciseID)
    return exercisesModel(theExerciseData)

@app.get('/exercise/{id}')
def exercise(id: str):
    return exerciseModel(conn.MoveFit.Exercises.find_one({"_id":ObjectId(str(id))}))