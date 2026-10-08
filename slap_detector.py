import time
from macimu import IMU

print("1. Attempting to start hardware link...")

with IMU() as imu:

    print("2. Pipeline connected! Waiting for first data block from sensor...")

    while True:
     for data in imu.accelerometer:

         print("3. Data packet received!")

         print(f"X-Axis (Tilt left/right): {data.x}g | "
               f"Y-Axis (Tilt front/back): {data.y}g | "
               f"Z-Axis (Up/Down motion) : {data.z}g", end="\r")

         time.sleep(0.05)