import json

# Load the COCO dataset JSON file
with open('/home/kumar/tao-experiments/data/raw-data/annotations/instances_val2017.json', 'r') as json_file:
    coco_data = json.load(json_file)

# Modify category IDs
for category in coco_data['categories']:
    category['id'] -= 1

# Update annotation category IDs
for annotation in coco_data['annotations']:
    annotation['category_id'] -= 1

# Save the modified JSON to a new file
with open('/home/kumar/instances_vallae.json', 'w') as json_file:
    json.dump(coco_data, json_file, indent=4)
