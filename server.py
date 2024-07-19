from flask import Flask, Response
import json
import time
import random

app = Flask(__name__)


# Function to generate random sensor data
def generate_sensor_data():
    while True:
        # Simulate sensor data for Volume Sensor A
        volume_sensor_a = random.randint(0, 100)

        # Simulate sensor data for Volume Sensor B
        volume_sensor_b = random.randint(0, 100)

        # Simulate sensor data for Temperature Sensor A
        temperature_sensor_a = random.uniform(0, 100)

        # Simulate sensor data for Temperature Sensor B
        temperature_sensor_b = random.uniform(0, 100)

        # Simulate sensor data for Pressure Sensor A
        pressure_sensor_a = random.uniform(0, 10)

        # Simulate sensor data for Pressure Sensor B
        pressure_sensor_b = random.uniform(0, 10)

        # Construct JSON message with sensor data
        sensor_data = {
            "volume_sensor_a": volume_sensor_a,
            "volume_sensor_b": volume_sensor_b,
            "temperature_sensor_a": temperature_sensor_a,
            "temperature_sensor_b": temperature_sensor_b,
            "pressure_sensor_a": pressure_sensor_a,
            "pressure_sensor_b": pressure_sensor_b,
        }

        # Convert sensor data to JSON format
        json_data = json.dumps(sensor_data)

        # Yield JSON message
        yield f"data: {json_data}\n\n"

        # Introduce a delay before generating next set of sensor data
        time.sleep(1)


# SSE endpoint to provide sensor data
@app.route("/sensor_data")
def sensor_data():
    return Response(generate_sensor_data(), content_type="text/event-stream")


if __name__ == "__main__":
    app.run(debug=True)
