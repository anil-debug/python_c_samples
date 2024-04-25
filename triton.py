import json
import requests

# Define the server URL and model name
server_url = "https://10.1.2.139:8000"
model_name = "InstanceSeg_random6"

# Prepare the input data as a JSON payload
input_data = {
    "inputs": [
        {
            "name": "input_tensor",
            "datatype": "FP32",
            "shape": [1, 3, 224, 224],  # Example input shape
            "data": [0.0, 1.0, 2.0, ...],  # Example input data
        }
    ]
}

# Remove the ellipsis object from the input data
input_data["inputs"][0]["data"] = input_data["inputs"][0]["data"][:-3]

# Convert the input data to JSON format
payload = json.dumps({"model_name": model_name, "inputs": input_data})

# Set the headers
headers = {"Content-Type": "application/json", "Inference-Header-Content-Length": str(len(payload))}

# Send the POST request
response = requests.post(server_url, data=payload, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse and process the response
    result = json.loads(response.text)
    output_tensors = result["outputs"]
    # Process the output tensors as needed
    print(output_tensors)
else:
    print("Inference request failed with status code:", response.status_code)
    print("Error:", response.text)
