import json

# Path to the JSON file
file_path = "python_learnings/python_concepts/data_scraping/data.json"

# Load JSON data from the file
with open(file_path, 'r') as reena:
    data = json.load(reena)

# Access the data
print(f"Name: {data['name']}")
print(f"Age: {data['age']}")
print(data['skills'])
print(f"Skills: {', '.join(data['skills'])}")

print("{data['name']}")
print(f"{data['name']}")