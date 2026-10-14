import json
import csv

with open("data/raw/yosar_located.geojson", "r") as file:
    data = json.load(file)

features = data["features"]

# Get the field names from the first record
fieldnames = features[0]["properties"].keys()

with open("data/yosar_located.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    for feature in features:
        writer.writerow(feature["properties"])

print(f"Exported {len(features)} records.")
