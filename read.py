import serial
import time

ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)
ser.flush()

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
