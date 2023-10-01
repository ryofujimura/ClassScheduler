import json

# Read the user input from input.json
with open("input.json", "r") as json_file:
    input_data = json.load(json_file)

user_input = input_data.get("user_input", "No user input provided")

# Your Python script logic here, using the user_input variable
# For demonstration, we'll create a simple JSON file.
data = {"message": f"User input: {user_input}"}

with open("output.json", "w") as json_file:
    json.dump(data, json_file)
