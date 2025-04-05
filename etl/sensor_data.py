class SensorData:
    def __init__(self, image=None, lidar=None, imu=None, timestamp=None):
        self.image = image
        self.lidar = lidar
        self.imu = imu
        self.timestamp = timestamp


class TransformedSensorData:
    def __init__(self, image=None, lidar=None, imu=None, timestamp=None):
        self.image = image
        self.lidar = lidar
        self.imu = imu
        self.timestamp = timestamp
