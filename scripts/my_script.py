import json

# Your Python script logic here
# For demonstration, we'll create a simple JSON file.
data = {"message": "Hello, world!"}

with open("output.json", "w") as json_file:
    json.dump(data, json_file)
