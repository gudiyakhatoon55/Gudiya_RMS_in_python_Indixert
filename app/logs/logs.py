import json
import datetime
import os

File_Path = "app/database/error.json"

def log_error(error):

    data = {
        "time": str(datetime.datetime.now()),
        "error": str(error)
    }
    try:
        if os.path.exists(File_Path):
            with open(File_Path,"r")as f:
                error = json.load(f)
        else:
            error = []

        error.append(data)

        with open(File_Path,"w") as f:
            json.dump(error,f,indent=4)

    except Exception as e:

        print(e)