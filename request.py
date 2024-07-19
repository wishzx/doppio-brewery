import requests

# Make a GET request to the SSE endpoint
response = requests.get("http://localhost:5000/sensor_data", stream=True)

# Check if the request was successful
if response.status_code == 200:
    print("Connected to SSE endpoint. Waiting for data...")

    # Iterate over the response content (SSE messages)
    for line in response.iter_lines():
        if line:
            # Print the received data
            print("Received data:", line.decode())
else:
    print("Failed to connect to SSE endpoint. Status code:", response.status_code)
