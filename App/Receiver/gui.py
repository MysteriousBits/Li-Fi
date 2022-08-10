import tkinter as tk
import tkinter.scrolledtext as tkscrolled
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
        self.geometry("520x420")

        # Headline label
        tk.Label(self, text = "Lifi Receiver",  fg = "cyan", font = ("Roboto", 20, "bold")).grid(row = 0, column = 4, pady = 10)

        # Message label
        self.msglbl = tk.Label(self, text = "Message: ")
        self.msglbl.grid(row = 1, column = 1, padx = 5)

        # Message box
        self.msgbox = tk.Text(self, width = 40, height = 1)
        self.msgbox.grid(row = 1, column = 2, columnspan = 6, pady = 5)

        # Log label
        tk.Label(self, text = "Logs: ", font = (12), fg = "orange").grid(row = 2, column = 4, pady = 2)

        # Log box
        self.logbox = tkscrolled.ScrolledText(self, width = 50, height = 15, bg = "grey15", fg = "green2", font = "consolas")
        self.logbox.grid(row = 3, column = 0, columnspan = 9)

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
    # gui = Gui()
    # gui.mainloop()