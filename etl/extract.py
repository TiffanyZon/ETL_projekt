# Funktion för fil: Läsa in kamerabild, LiDAR-fil samt IMU-fil.
# Samla alla i ett objekt SensorData

from etl.sensor_data import SensorData
import cv2
import os
import numpy as np


def load_timestamp(base_path, frame_id, sensor_type):
    timestamp_path = os.path.join(base_path, sensor_type, "timestamps.txt")

    try:
        with open(timestamp_path, "r") as f:
            lines = f.readlines()
        timestamp = lines[int(frame_id)]
        return timestamp.strip()

    except FileNotFoundError as e:
        print(e)
        return None


def load_image(base_path, frame_id):
    img_path = os.path.join(base_path, "image_00", "data", frame_id + ".png")
    img = cv2.imread(img_path)
    return img


def load_lidar(base_path, frame_id):
    bin_path = os.path.join(base_path, "velodyne_points", "data", frame_id + ".bin")
    try:
        lidar_data = np.fromfile(bin_path, dtype=np.float32).reshape(-1, 4)
    except FileNotFoundError as e:
        print(e)
        print(f"Hittade inte LiDAR-fil: {bin_path}")
        lidar_data = None
    return lidar_data


def load_imu(base_path, frame_id):
    txt_path = os.path.join(base_path, "oxts", "data", frame_id + ".txt")
    try:
        with open(txt_path, "r") as f:
            line = f.readline()
            values = [float(x) for x in line.strip().split()]
            if len(values) < 30:
                print(f"För få IMU värden i filen!")
                return None
            imu_data = {
                "lat": values[0],
                "lon": values[1],
                "alt": values[2],
                "roll": values[3],
                "pitch": values[4],
                "yaw": values[5],
                "vn": values[6],
                "ve": values[7],
                "vf": values[8],
                "vl": values[9],
                "vu": values[10],
                "ax": values[11],
                "ay": values[12],
                "az": values[13],
                "af": values[14],
                "al": values[15],
                "au": values[16],
                "wx": values[17],
                "wy": values[18],
                "wz": values[19],
                "wf": values[20],
                "wl": values[21],
                "wu": values[22],
                "posacc": values[23],
                "velacc": values[24],
                "navstat": values[25],
                "numsats": values[26],
                "posmode": values[27],
                "velmode": values[28],
                "orimode": values[29],
            }
    except FileNotFoundError:
        print(f"Hittade ingen fil med path: {txt_path}")
        imu_data = None
    return imu_data


def exract_data(base_path, frame_id):
    timestamp = load_timestamp(base_path, frame_id, sensor_type="image_00")
    image = load_image(base_path, frame_id)
    lidar = load_lidar(base_path, frame_id)
    imu = load_imu(base_path, frame_id)

    if image is None or lidar is None or imu is None:
        print("Gick inte att hämta sensorvärden...")
        return None

    return SensorData(image=image, lidar=lidar, imu=imu, timestamp=timestamp)
