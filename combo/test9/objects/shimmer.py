# https://github.com/ShimmerResearch/shimmer3/tree/master/LogAndStream/python_scripts
import serial
import struct
import sys
import pandas as pd
from datetime import datetime
import time


class shimmer:
    def connect(self, port, baud=115200, sampling_rate=500):
        try:
            self.ser = serial.Serial(port, baud)
            self.ser.flushInput()
            print("shimmer connected")
            self.ser.write(struct.pack("BBBB", 0x08, 0x80, 0x00, 0x00))  # analogaccel
            self.wait_for_ack()
            print("sensor setting, done.")
            self.set_sampling_rate(sampling_rate)
            print("sampling rate set to " + str(sampling_rate))
            return True
        except serial.SerialException:
            print("failed to connect to " + str(port))
            return False

    def wait_for_ack(self):
        ddata = bytes()
        ack = struct.pack("B", 0xFF)
        while ddata != ack:
            ddata = self.ser.read(1)
        return

    def set_sampling_rate(self, sampling_rate=500):
        # Convert to integer and round
        hz = int(round(32768 / sampling_rate))
        hex_hz = hex(hz)

        # Split the sampling frequency into two bytes
        byte1 = hz & 0xFF  # Extracts the least significant byte
        byte2 = (hz >> 8) & 0xFF  # Extracts the most significant byte

        # print(f"Byte 1: {hex(byte1)}")
        # print(f"Byte 2: {hex(byte2)}")

        # ser.write(
        #     struct.pack("BBB", 0x05, 0x00, 0x19)
        #                              right, left
        # )  # 5.12Hz (6400 = (0x1900)). Has to be done like this for alignment reasons
        # 2^15 / 6400 = 5.12hz

        self.ser.write(struct.pack("BBB", 0x05, byte1, byte2))  # 550 hz
        self.wait_for_ack()
        print("sampling rate setting, done.")

    def end(self):
        # send stop streaming command
        self.ser.write(struct.pack("B", 0x20))
        print("stop command sent, waiting for ACK_COMMAND")
        self.wait_for_ack()
        print("ACK_COMMAND received.")
        # close serial port
        self.ser.close()
        print("All done")

    def record(self, record_duration):

        # send start streaming command
        self.ser.write(struct.pack("B", 0x07))
        self.wait_for_ack()
        print("start command sending, done.")

        # read incoming data
        ddata = bytes()
        numbytes = 0
        framesize = 10  # 1byte packet type + 3byte timestamp + 3x2byte Analog Accel
        xlog = []
        ylog = []
        zlog = []

        start_time = time.time()
        while time.time() - start_time < record_duration:
            while numbytes < framesize:
                ddata += self.ser.read(framesize)
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
            ylog.append(analogaccely)
            zlog.append(analogaccelz)

        data = {"x": xlog, "y": ylog, "z": zlog}

        pd.DataFrame(data).to_csv("data/shimmer_data.csv", index=False, header=False)

        self.end()


if __name__ == "__main__":
    shim = shimmer()
    if shim.connect("com8", sampling_rate=500):
        print("connected")
