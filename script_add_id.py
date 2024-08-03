import json
import uuid

# Read the JSON file
with open(
    "/home/teutondev/Documents/0.0_projects/car_logos_data/logos/data.json", "r"
) as file:
    data = json.load(file)

# Add unique ID to each item
for item in data:
    item["id"] = str(uuid.uuid4())

# Write the updated JSON back to the file
with open(
    "/home/teutondev/Documents/0.0_projects/car_logos_data/logos/data.json", "w"
) as file:
    json.dump(data, file, indent=4)
