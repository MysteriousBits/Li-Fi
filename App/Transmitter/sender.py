import serial
from config import *
import time

class Arduino:
    def __init__(self):
        self.ser = serial.Serial(port = port, baudrate = 9600, timeout = wait)
        self.logging = True
        
    def send(self, Bytes):
        if type(Bytes) == str:
            Bytes = Bytes.encode("utf-8")
        self.ser.write(Bytes)
        print("Bytes written to arduino serial.")

    def sendfile(self, filedir):
        print("Sending file to arduino serial...")
        with open(filedir, 'rb') as file:
            self.send(file_ind_bytes)
            # Let arduino read the start signal first
            time.sleep(file_start_dalay)
            self.send(file.read())
        print("File sent.")

    def log(self, logbox):
        time.sleep(1)
        while self.logging:
            logs = self.ser.readline()
            logs = logs.decode("utf-8", errors = 'ignore')
            if logs != "":
                logbox.insert("end", logs)