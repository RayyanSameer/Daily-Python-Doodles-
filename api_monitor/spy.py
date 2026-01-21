import requests

url = "https://jsonplaceholder.typicode.com/users"
print(f"Connecting to {url}")

response = requests.get(url)
print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    data = response.json()
    file_name = "user_report.txt"
    print(f"Writing data to {file_name}")

   
    with open(file_name, "w") as file:
        file.write(f"--- CONFIDENTIAL USER REPORT ---\n")
        file.write(f"Total Entries: {len(data)}\n\n")

        
        for user in data:
            name = user['name']
            email = user['email']
            city = user['address']['city']
            lat = user['address']['geo']['lat']

            line = f"AGENT: {name} | EMAIL: {email} | LOC: {city} (Lat: {lat})\n"
            
            
            file.write(line)
            
            print(f"Saved: {name}")
 

    print("\n[+] Mission Complete. Check user_report.txt")

else:
    print("Connection Failed.")