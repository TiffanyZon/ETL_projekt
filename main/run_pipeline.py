import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from etl.extract import exract_data
from etl.transform import transform_all
import pprint


base_path = "data/kitti"
frame_id = "0000000005"

# for i in range(10):
#    frame_id = str(i).zfill(10)
sensor_data = exract_data(base_path, frame_id)
if sensor_data is not None:

    print("Sensordata hämtad!")
    print(
        "Bildstorlek:",
        sensor_data.image.shape if sensor_data.image is not None else "Ingen bild",
    )
    print(
        "LiDAR-punkter:",
        sensor_data.lidar.shape if sensor_data.lidar is not None else "Ingen LiDAR",
    )
    print("IMU-data:")
    pprint.pprint(sensor_data.imu)
    print("Timestamp:", sensor_data.timestamp)

    transform_data = transform_all(sensor_data)
else:
    print("❌ Något gick fel – kunde inte hämta sensordata.")
