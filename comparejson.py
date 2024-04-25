import json

def compare_json_files(file1_path, file2_path):
    with open(file1_path, 'r') as file1:
        data1 = json.load(file1)

    with open(file2_path, 'r') as file2:
        data2 = json.load(file2)

    return data1 == data2

file1_path = '/home/kumar/Images/tao_val.json'
file2_path = '/home/kumar/instances_val2017.json'

if compare_json_files(file1_path, file2_path):
    print("The JSON files are identical.")
else:
    print("The JSON files are not identical.")
