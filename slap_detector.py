from macimu import IMU

with IMU() as imu:

    for data in imu.read_accel():
        print(sample)