def exerciseModel(i) -> dict:
    return {
        "userID":i["userID"],
        "Type":i["Type"],
        "Count":i["Count"]
    }

def exercisesModel(i=10) -> list:
    return [exerciseModel(item) for item in i]