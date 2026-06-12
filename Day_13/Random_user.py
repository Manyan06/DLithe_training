#py -m pip install requests

import requests
import json
url = "https://randomuser.me/api/?results=5"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print("\nRandom User Data: ")
    print("=" * 50)
    for user in data['results']:
        print("Name: ",user['name']['first'],user['name']['last'])
        print("Gender: ",user['gender'])
        print("Email: ",user['email'])
        print("Country: ",user['location']['country'])
        print("-" * 50)
with open("random_users.json", "w") as file:
        json.dump(data, file, indent=4)
print("Data exported Successfully.")