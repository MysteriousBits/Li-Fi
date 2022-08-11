import serial
from config import *
import time

class Arduino:
    def __init__(self):
        self.ser = serial.Serial(port = port, baudrate = 9600, timeout = 0.1)
        self.logging = True
        
    def send(self, Bytes):
        self.ser.write(Bytes.encode("utf-8"))
        print("Bytes written to arduino serial.")

    def sendfile(self, filedir):
        print("Sending file to arduino serial...")
        with open(filedir) as file:
            self.send(file_ind_bytes)
            self.send(file.read())

    def log(self, logbox):
        time.sleep(1)
        while logging:
            logs = self.ser.readline()
            logs = logs.decode("utf-8")
            if logs != None:
                logs += "\n"
                logbox.insert("end", logs)