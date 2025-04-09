# Funktion för fil: Läsa in kamerabild, LiDAR-fil samt IMU-fil.
# Samla alla i ett objekt SensorData

from etl.sensor_data import SensorData
import cv2
import os
import numpy as np
import pandas as pd


def load_timestamp(base_path, frame_id, folder):
    timestamp_path = os.path.join(base_path, folder, "timestamps.txt")

    try:
        with open(timestamp_path, "r") as f:
            lines = f.readlines()
        timestamp = lines[int(frame_id)].strip()
        timestamp_df = pd.DataFrame([[timestamp]], columns=["time"])
        return timestamp_df

    except FileNotFoundError:
        print("Kunde inte hitta timestamp fil")
        return None


def load_image(base_path, frame_id):
    img_path = os.path.join(base_path, "image_00", "data", frame_id + ".png")
    img = cv2.imread(img_path)
    return img


def load_lidar(base_path, frame_id):
    bin_path = os.path.join(base_path, "velodyne_points", "data", frame_id + ".bin")
    try:
        lidar_data = np.fromfile(bin_path, dtype=np.float32).reshape(-1, 4)
        lidar_df = pd.DataFrame(lidar_data, columns=["x", "y", "z", "intensity"])
        return lidar_df
    except FileNotFoundError:
        print("Kunde inte hitta LiDAR fil")
        return None


def load_imu(base_path, frame_id):
    txt_path = os.path.join(base_path, "oxts", "data", frame_id + ".txt")
    try:
        with open(txt_path, "r") as f:
            line = f.readline()
            values = [float(x) for x in line.strip().split()]
            if len(values) < 30:
                print(f"För få IMU värden i filen!")
                return None
            keys = [
                "lat",
                "lon",
                "alt",
                "roll",
                "pitch",
                "yaw",
                "vn",
                "ve",
                "vf",
                "vl",
                "vu",
                "ax",
                "ay",
                "az",
                "af",
                "al",
                "au",
                "wx",
                "wy",
                "wz",
                "wf",
                "wl",
                "wu",
                "posacc",
                "velacc",
                "navstat",
                "numsats",
                "posmode",
                "velmode",
                "orimode",
            ]
            imu_df = pd.DataFrame([values], columns=keys)
            return imu_df
    except FileNotFoundError:
        print("Kunde inte hitta IMU fil")
        return None


def extract_data(base_path, frame_id):
    timestamp = load_timestamp(base_path, frame_id, folder="image_00")
    image = load_image(base_path, frame_id)
    lidar = load_lidar(base_path, frame_id)
    imu = load_imu(base_path, frame_id)

    return SensorData(image=image, lidar=lidar, imu=imu, timestamp=timestamp)
