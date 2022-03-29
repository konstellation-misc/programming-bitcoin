import json
from pprint import pprint


meta_data = {
    "project_name": "Wallet Provider",
    "author": "Michael Jordan",
    "email": "michael.ngowi@vegaxholdings.com"
}

def dict_to_json(file_path):
    with open(file_path, "w") as file:
        json.dump(meta_data, file)
    return True

def reading_data_back(file_path):
    with open(file_path, "r") as file:
        return json.load(file)
    

if __name__ == "__main__":
    res = dict_to_json("package.json")
    pprint(res)

    meta_data = reading_data_back("package.json")
    pprint(meta_data)
