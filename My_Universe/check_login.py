# imports
import csv


# check login
def check_login(id_, passw):
    with open("login.csv", "r+") as f:
        id_true = False
        file_read = csv.DictReader(f)
        for i in file_read:
            if i['id'] == f"{id_}":
                id_true = True
                if i['password'] == f"{passw}":
                    return "1"
        if id_true:
            return "Your password is incorrect!"
        else:
            return "exit"
