import serial
import struct
import sys
import pandas as pd
from datetime import datetime
import time


def wait_for_ack():
    ddata = bytes()
    ack = struct.pack("B", 0xFF)
    while ddata != ack:
        ddata = ser.read(1)
        print("0x%02x" % ddata[0])
    return


if len(sys.argv) < 2:
    print("no device specified")
    print("You need to specify the serial port of the device you wish to connect to")
    print("example:")
    print("   aAccel5Hz.py Com12")
    print("or")
    print("   aAccel5Hz.py /dev/rfcomm0")
else:
    ser = serial.Serial(sys.argv[1], 115200)
    ser.flushInput()
    print("port opening, done.")

    # send the set sensors command
    ser.write(struct.pack("BBBB", 0x08, 0x80, 0x00, 0x00))  # analogaccel
    wait_for_ack()
    print("sensor setting, done.")

    # send the set sampling rate command

    # ser.write(
    #     struct.pack("BBB", 0x05, 0x00, 0x19)
    #                              right, left
    # )  # 5.12Hz (6400 = (0x1900)). Has to be done like this for alignment reasons
    # 2^15 / 6400 = 5.12

    ser.write(struct.pack("BBB", 0x05, 0x3E, 0x00))  # 550 hz

    wait_for_ack()
    print("sampling rate setting, done.")

    # send start streaming command
    ser.write(struct.pack("B", 0x07))
    wait_for_ack()
    print("start command sending, done.")

    # read incoming data
    ddata = bytes()
    numbytes = 0
    framesize = 10  # 1byte packet type + 3byte timestamp + 3x2byte Analog Accel
    logx = []

    xlog = []

    print("Packet Type,Timestamp,Analog Accel X,Analog Accel Y,Analog Accel Z")
    start_time = time.time()
    try:
        while True:
            while numbytes < framesize:
                ddata += ser.read(framesize)
                numbytes = len(ddata)

            data = ddata[0:framesize]
            ddata = ddata[framesize:]
            numbytes = len(ddata)

            (packettype) = struct.unpack("B", data[0:1])
            (timestamp0, timestamp1, timestamp2) = struct.unpack("BBB", data[1:4])
            (analogaccelx, analogaccely, analogaccelz) = struct.unpack(
                "HHH", data[4:framesize]
            )

            timestamp = timestamp0 + timestamp1 * 256 + timestamp2 * 65536

            print(
                "0x%02x,%5d,\t%4d,%4d,%4d"
                % (packettype[0], timestamp, analogaccelx, analogaccely, analogaccelz)
            )
            xlog.append(analogaccelx)
            # print(xlog)
            # time.sleep(0.002)

    except KeyboardInterrupt:
        # send stop streaming command
        finish_time = time.time()
        time_elapsed = finish_time - start_time
        print(time_elapsed)
        pd.DataFrame(xlog).to_csv("data.csv", index=False)
        ser.write(struct.pack("B", 0x20))
        print
        print("stop command sent, waiting for ACK_COMMAND")
        wait_for_ack()
        print("ACK_COMMAND received.")
        # close serial port
        ser.close()
        print("All done")

        rounded_time = round(time_elapsed, 5)

        print(len(xlog) / rounded_time)
