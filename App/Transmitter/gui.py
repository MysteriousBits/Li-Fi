import tkinter as tk
from tkinter import filedialog
import tkinter.scrolledtext as tkscrolled

class Gui(tk.Tk):
    def __init__(self, arduino):
        super().__init__()
        self.arduino = arduino

        # Gui variables
        self.message = tk.StringVar()
        self.message.set("Enter message here")
        self.bgc = "grey30"

        ##### Set up UI #####
        # Window
        self.title("Lifi Transmitter")
        self.geometry("530x480")
        self.configure(bg = self.bgc)

        # Headline label
        tk.Label(self, text = "Lifi Transmitter", bg = self.bgc,fg = "cyan",
            font = ("Roboto", 20, "bold")).grid(row = 0, column = 4, pady = 10)

        # Message entry box
        self.msgentry = tk.Entry(self, textvariable = self.message, width = 50, bg = self.bgc, fg = "white")
        self.msgentry.grid(row = 1, column = 0, columnspan = 8, padx = 2, pady = 10)

        # Message send button
        tk.Button(self, text = "Send", bg = self.bgc, fg = "white",
            command = self.sendmsg).grid(row = 1, column = 8)

        # File send button
        tk.Button(self, text = "Send File", bg = self.bgc, fg = "white",
            command = self.sendfile).grid(row = 2, column = 4, pady = 5)

        # Log label
        tk.Label(self, text = "Logs: ", font = ("Helvetica", 13, "bold"), fg = "#F79C91",
            bg = self.bgc).grid(row = 4, column = 0, pady = 1)

        # Log clear button
        tk.Button(self, text = "Clear", font = ("Roboto", 8), bg = self.bgc, fg = "white",
            width = 4, height = 1, command = self.clear_log).grid(row = 4, column = 8)

        # Log box
        self.logbox = tkscrolled.ScrolledText(self, width = 50, height = 15, bg = "grey12",
            fg = "green2", font = "consolas")
        self.logbox.grid(row = 5, column = 0, columnspan = 9)

    def clear_log(self):
        self.logbox.delete(1.0, tk.END)

    def sendmsg(self):
        self.arduino.send(self.message.get())
        self.message.set("Enter message here")

    def sendfile(self):
        dir = filedialog.askopenfilename(title = "Select a file to send")
        if dir != None:
            self.arduino.sendfile(dir)


if __name__ == "__main__":
    print("Please run the main.py file.")

    # Test
    # gui = Gui(None)
    # gui.mainloop()