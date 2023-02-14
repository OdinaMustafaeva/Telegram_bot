# imports
import csv
import json


# register
def register(one_dict):
    # Save csv
    with open("login.csv", "a+", newline="\n") as f:
        header = ["id", "name", "password"]
        file_read = csv.DictWriter(f, header)
        file_read.writerow(one_dict)
        with open(f"{one_dict['id']}.json", "a+", newline="\n") as json_file:
            for_file = {
                'my_goals': {},
                'future_m': {}
            }
            json.dump(for_file, json_file)
        return f"Successful"

