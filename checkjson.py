import json

def is_coco_format(annotation_data):
    # Check if required keys exist in the annotation data
    required_keys = ["annotations", "images", "categories"]
    for key in required_keys:
        if key not in annotation_data:
            return False
    
    # Check if each annotation has necessary keys
    for annotation in annotation_data["annotations"]:
        required_annotation_keys = ["id", "image_id", "category_id", "bbox", "area", "iscrowd"]
        for key in required_annotation_keys:
            if key not in annotation:
                return False
    
    # Check if each image has necessary keys
    for image in annotation_data["images"]:
        required_image_keys = ["id", "file_name", "width", "height"]
        for key in required_image_keys:
            if key not in image:
                return False
    
    # Check if each category has necessary keys
    for category in annotation_data["categories"]:
        required_category_keys = ["id", "name", "supercategory"]
        for key in required_category_keys:
            if key not in category:
                return False
    
    return True

# Load your annotation JSON file
annotation_file_path = '/home/kumar/tiny/val2017.json'
with open(annotation_file_path, 'r') as json_file:
    annotation_data = json.load(json_file)

# Check if it's in COCO format
if is_coco_format(annotation_data):
    print("The annotation file is in COCO format.")
else:
    print("The annotation file is not in COCO format.")
