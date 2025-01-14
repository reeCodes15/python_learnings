import json

# Sample JSON string (can also be loaded from a file or API)
json_data = '''
{
    "name": "John Doe",
    "age": 30,
    "skills": ["Python", "Data Analysis", "Machine Learning"],
    "address": {
        "city": "New York",
        "state": "NY"
    }
}
'''

# Load the JSON data into a Python dictionary
data = json.loads(json_data)

# Access specific fields
name = data['name']
age = data['age']
skills = data['skills']
city = data['address']['city']

# Print extracted data
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Skills: {', '.join(skills)}")
print(f"City: {city}")
