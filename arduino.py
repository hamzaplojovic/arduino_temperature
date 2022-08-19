import serial
import time

ser = serial.Serial('COM6', 9600)
time.sleep(1)

for i in range(100):
    line = ser.readline().decode("utf-8")
    if len(line) > 0:
        print(line)
