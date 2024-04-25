import json
import os
# Path to the reduced COCO JSON file
coco_json_path = '/home/kumar/tiny/instances_train2017.json'

# Path to the folder containing the 20 images
image_folder_path = '/home/kumar/tiny/train'

# Load the reduced COCO JSON
with open(coco_json_path, 'r') as json_file:
    coco_data = json.load(json_file)

# List image files in the folder
image_files = [f for f in os.listdir(image_folder_path) if f.endswith(('.jpg', '.png'))]

# Create a dictionary to map image filenames to their corresponding IDs
image_id_map = {image_data['file_name']: image_data['id'] for image_data in coco_data['images']}

# Filter annotations based on the 20 image filenames
new_annotations = []
for annotation in coco_data['annotations']:
    image_id = annotation['image_id']
    image_filename = coco_data['images'][image_id]['file_name']
    if image_filename in image_files:
        new_annotation = annotation.copy()
        new_annotation['image_id'] = image_id_map[image_filename]
        new_annotations.append(new_annotation)

# Update the annotations and images in the COCO JSON data
coco_data['annotations'] = new_annotations
coco_data['images'] = [image_data for image_data in coco_data['images'] if image_data['file_name'] in image_files]

# Save the updated COCO JSON back to file
updated_coco_json_path = '/home/solomon/tiny/train2017.json'
with open(updated_coco_json_path, 'w') as json_file:
    json.dump(coco_data, json_file)
