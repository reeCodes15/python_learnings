import requests

url = "https://jsonplaceholder.typicode.com/users"








response = requests.get(url)



if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    print(data)
    # print(data)
    # print(data[0])
    # # Print the first user's name and email
    # print(f"Name: {data[0]['name']}")
    # print(f"Email: {data[0]['email']}")

    # # Loop through and print all user names
    print("\nAll User Names:")
    for user in data:
        print(user['name'])
        print(user['email'])
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
