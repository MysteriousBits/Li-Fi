import tkinter as tk
from tkinter import filedialog

class Gui(tk.Tk):
    def __init__(self, arduino):
        super().__init__()
        self.arduino = arduino

        # Gui variables
        self.message = tk.StringVar()
        self.message.set("Enter message here")

        ##### Set up UI #####
        # Window
        self.title("Lifi Transmitter")
        self.geometry("500x450")

        # Headline label
        tk.Label(self, text = "Lifi Receiver").pack()

        # Message entry box
        self.msgentry = tk.Entry(self, textvariable = self.message)
        self.msgentry.pack()

        # Message send button
        tk.Button(self, text = "Send", command = self.sendmsg).pack()

        # File send button
        tk.Button(self, text = "Send File", command = self.sendfile).pack()

        # Log label
        tk.Label(self, text = "Logs: ").pack()

        # Log box
        self.logbox = tk.Text(self, width = 60, height = 15)
        self.logbox.pack()

    def sendmsg(self):
        self.arduino.send(message.get())
        self.message.set("Enter message here")

    def sendfile(self):
        dir = filedialog.askopenfilename(title = "Select a file to send")
        if dir != None:
            self.arduino.sendfile(dir)


if __name__ == "__main__":
    print("Pleease run the main.py file.")

    # Test
    gui = Gui(None)
    gui.mainloop()