import json

FILE_PATH = "app/database/file_path.json"


def read_users():

    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except:
        return []


def write_user(user):

    users = read_users()
    users.append(user)

    with open(FILE_PATH, "w") as file:
        json.dump(users, file, indent=4) 
        
