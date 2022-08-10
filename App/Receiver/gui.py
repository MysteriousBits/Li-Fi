import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import sys
import subprocess

class Gui(tk.Tk):
    def __init__(self):
        super().__init__()

        ##### Set up UI #####
        # Window
        self.title("Lifi Receiver")
        self.geometry("500x400")

        # Headline label
        tk.Label(self, text = "Lifi Receiver").pack()

        # Message label
        self.msglbl = tk.Label(self, text = "Message: ")
        self.msglbl.pack()

        # Message box
        self.msgbox = tk.Text(self, width = 50, height = 2)
        self.msgbox.pack()

        # Log label
        tk.Label(self, text = "Logs: ").pack()

        # Log box
        self.logbox = tk.Text(self, width = 60, height = 15)
        self.logbox.pack()

    def show_msg(self, msg):
        self.msgbox.delete(1.0, tk.END)
        self.msgbox.insert(1.0, msg)

    def show_file(self, filedir):
        reply = messagebox.askquestion("Show file", "File has been saved successfully.\nDo you want to open it now?")
        if reply == "yes":
            # Cross platform
            # Only writting the directory is enough in windows
            opener = ""
            if sys.platform == "linux":
                opener = "xdg-open "
            elif sys.platform == "darwin":
                opener = "open "
            subprocess.Popen(opener + filedir, shell = True)


    def get_save_dir(self):
        savedir = filedialog.asksaveasfilename(title = "Give file name with correct extension")
        return savedir


if __name__ == "__main__":
    print("Pleease run the main.py file.")

    # Test
    gui = Gui()
    gui.mainloop()