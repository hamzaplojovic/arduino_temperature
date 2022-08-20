import serial
import time
import httpx

ser = serial.Serial('/dev/cu.usbmodem1201', 9600)
time.sleep(1)

while True:
    line = ser.readline().decode("utf-8")
    if len(line.strip()) > 0:
        httpx.get(
            f"https://lrlegx.deta.dev/temperature/add?new={str(line.strip()[39:-1])}")
        httpx.get(
            f"https://lrlegx.deta.dev/humidity/add?new={line.strip()[19:24]}")
