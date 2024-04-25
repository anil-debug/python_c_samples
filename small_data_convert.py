import json
import os

# Load your existing COCO JSON data
with open('/home/kumar/train.json', 'r') as f:
    coco_data = json.load(f)

# Create a set of image filenames present in the "Images" folder
image_filenames = set(os.listdir('/home/kumar/Images'))

# Filter annotations to only keep those associated with images in the folder
filtered_annotations = [annotation for annotation in coco_data['annotations'] if annotation['image_id'] in image_filenames]

# Filter images to only keep those present in the folder
filtered_images = [image for image in coco_data['images'] if image['file_name'] in image_filenames]

# Create a new COCO JSON data structure with filtered annotations and images
updated_coco_data = {
    'categories': coco_data['categories'],
    'images': filtered_images,
    'annotations': filtered_annotations
}

# Save the updated JSON data to a new file
with open('/home/kumar/2017.json', 'w') as f:
    json.dump(updated_coco_data, f, indent=4)
