from etl.sensor_data import TransformedSensorData
import cv2
import numpy as np
import matplotlib.pyplot as plt


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


# slipper interpolering pga synkroniserad data!
# projicera vektor på bild!
def transform_imu(imu_data): ...


# behöver ändra storlek + normalisera!
def transform_image(image_data):
    print("\n***** Transforming image data...... ***** ")
    print(f"Current Image: {image_data[0,0]}")
    plt.imshow(image_data)
    plt.show()
    resized = cv2.resize(image_data, (224, 224))
    print(f"Resized Image: {resized[0,0]}")
    normalized = (resized / 255.0).astype(np.float32)
    print(f"Normalized Image: {normalized[0,0]}")
    plt.imshow(normalized)
    plt.show()


# behöver ta bort brus?
# 3D till 2D projection!
def transform_lidar(lidar_data): ...
