#py -m pip install requests
import requests
import json
try:
    url = f"https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    if response.status_code == 200:
        users = response.json()
        print("=" * 60)
        print("\nUser Information: ")
        print("=" * 60)
        for user in users:
          print(f"ID: {user['id']}")
          print(f"Name: {user['name']}")
          print(f"Username: {user['username']}")
          print(f"Email: {user['email']}")
          print(f"City: {user['address']['city']}")
          print(f"Company: {user['company']['name']}")
          print("-" * 60)
          with open("users.json", "w") as file:
                  json.dump(users, file, indent=4)
          print("Data saved successfully to users.json .")
    else:
      print("Failed to retrieve data")
except requests.exceptions.RequestException as e:
  print("Error: ",e)