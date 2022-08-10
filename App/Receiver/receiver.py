import serial
import config

class Arduino:
    def __init__(self, gui):
        self.ser = serial.Serial(port = port, baudrate = 9600, timeout = 0.1)
        self.gui = gui

    def sync(self):
        while True:
            logs = self.ser.readline()
            logs = logs.decode("utf-8")

            if logs == msg_ind_bytes:
                self.getmsg()
                continue
            elif logs == file_ind_bytes:
                self.getfile(int(logs[1:]))
                continue

            if logs != None:
                logs += "\n"
                self.gui.logbox.insert("end", logs)

    def getmsg(self):
        print("Reading message...")
        msg = self.ser.readline()
        msg = msg.decode("utf-8")
        self.gui.show_msg(msg)

    def getfile(self, size):
        print("Reading file...")
        Bytes = self.ser.read(size)
        filedir = self.gui.get_save_dir()

        with open(filedir, "wb") as file:
            file.write(Bytes)

        print("File saved.")
        gui.show_file(filedir)