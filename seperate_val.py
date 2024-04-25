import os
import json
import cv2
img_folder = '/home/kumar/Images'
json_file = '/home/kumar/surgical_val.json'
save_folder = '/home/kumar/Images/validation'
if not os.path.exists(save_folder):
    os.makedirs(save_folder)
with open(json_file, 'r') as f:
    data = json.load(f)
img_names = [item['file_name'] for item in data['images']]
for img_name in img_names:
    img_path = os.path.join(img_folder,img_name)
    img = cv2.imread(img_path)
    save_path = os.path.join(save_folder, img_name)
    cv2.imwrite(save_path,img)