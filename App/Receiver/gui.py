import tkinter as tk
from tkinter import filedialog

class Gui(tk.Tk):
    def __init__(self):
        super().__init__()

        ##### Set up UI #####
        # Window
        self.title("Lifi Receiver")
        self.geometry("500x400")

        # Headline label
        self.headline = tk.Label(self, text = "Lifi Receiver")
        self.headline.pack()

        # Message label
        self.msglbl = tk.Label(self, text = "Message: ")
        self.msglbl.pack()

        # Message box
        self.msgbox = tk.Text(self, width = 50, height = 2)
        self.msgbox.pack()

        # Log label
        self.loglbl = tk.Label(self, text = "Logs: ")
        self.loglbl.pack()

        # Log box
        self.logbox = tk.Text(self, width = 60, height = 15)
        self.logbox.pack()


    def show_msg(self, msg):
        msgbox.delete(1.0, tk.END)
        msgbox.insert(1.0, msg)

    def show_file(self, filedir):
        pass

    def get_save_dir(self):
        savedir = filedialog.asksaveasfilename(title = "Give file name with correct extension")
        print(savedir)
        return savedir

# Test
if __name__ == "__main__":
    gui = Gui()
    gui.mainloop()