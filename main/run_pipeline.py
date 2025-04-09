import sys
import os
import cv2
import matplotlib.pyplot as plt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from etl.extract import extract_data


def random_id(index: int, digits: int = 10):
    return str(index).zfill(digits)


base_path = "data/kitti"
frame_id = random_id(5)
print(frame_id)

sensor_data = extract_data(base_path, frame_id)
if sensor_data is not None:

    print("Sensordata hämtad!")
    print("\n")
    print(sensor_data.timestamp)
    print("\n")
    print(sensor_data.image)
    # image_rgb = cv2.cvtColor(sensor_data.image, cv2.COLOR_BGR2RGB)
    # plt.imshow(image_rgb)
    # plt.title("Kamera")
    # plt.axis("off")
    # plt.show()
    print("\n")
    print(sensor_data.imu)
    print("\n")
    print(sensor_data.lidar)

else:
    print("❌ Något gick fel – kunde inte hämta sensordata.")
