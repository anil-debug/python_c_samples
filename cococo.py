import os

def remove_json_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"Removed: {file_path}")

if __name__ == "__main__":
    images_folder = "/home/kumar/Images"
    expanded_path = os.path.expanduser(images_folder)

    if os.path.exists(expanded_path):
        remove_json_files(expanded_path)
    else:
        print("Images folder not found.")
