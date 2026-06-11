# RUN json_fileCreation 1st

import json
file = open("employee.json", "r")
data = json.load(file)
print("ID: ", data["id"])
print("Name: ", data["name"])
print("Salary: ", data["salary"])
file.close()