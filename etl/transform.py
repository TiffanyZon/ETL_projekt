from etl.sensor_data import TransformedSensorData


def transform_all(sensor_data):
    timestamp = sensor_data.timestamp

    imu_data = sensor_data.imu
    transformed_imu_data = transform_imu(imu_data)

    image_data = sensor_data.image
    transformed_image_data = transform_image(image_data)

    lidar_data = sensor_data.lidar
    transformed_lidar_data = transform_lidar(lidar_data)

    return TransformedSensorData(
        image=transformed_image_data,
        lidar=transformed_lidar_data,
        imu=transformed_imu_data,
        timestamp=timestamp,
    )


def transform_imu(imu_data): ...


def transform_image(image_data): ...


def transform_lidar(lidar_data): ...


def format_conversion(): ...
