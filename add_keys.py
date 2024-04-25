import json

# Load your existing COCO JSON data
with open('/home/kumar/kumar/train.json', 'r') as f:
    coco_data = json.load(f)

# Add "area" field to annotations
for annotation in coco_data['annotations']:
    annotation["area"] = 0.0  # Replace with the appropriate area value

# Add fields to images
for image in coco_data['images']:
    image["license"] = 1
    image["flickr_url"] = ""
    image["coco_url"] = ""
    image["date_captured"] = "2023-08-11"  # Replace with actual date

# Save the modified JSON data
with open('/home/kumar/Images/tao_train.json', 'w') as f:
    json.dump(coco_data, f, indent=4)
