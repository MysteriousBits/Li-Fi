import tkinter as tk
import tkinter.scrolledtext as tkscrolled
from tkinter import filedialog
from tkinter import messagebox
import sys
import os

class Gui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.bgc = "grey30"

        ##### Set up UI #####
        # Window
        self.title("Lifi Receiver")
        self.geometry("520x420")
        self.configure(bg = self.bgc)

        # Headline label
        tk.Label(self, text = "Lifi Receiver",  fg = "cyan", bg = self.bgc,
            font = ("Roboto", 20, "bold")).grid(row = 0, column = 4, pady = 10)

        # Message label
        self.msglbl = tk.Label(self, text = "Message: ", bg = self.bgc, fg = "white")
        self.msglbl.grid(row = 1, column = 0, columnspan = 2, padx = 2)

        # Message box
        self.msgbox = tk.Text(self, width = 50, height = 1, bg = self.bgc, fg = "white")
        self.msgbox.grid(row = 1, column = 2, columnspan = 7, pady = 10)

        # Log label
        tk.Label(self, text = "Logs: ", font = ("Helvetica", 13, "bold"), fg = "#F79C91",
            bg = self.bgc).grid(row = 2, column = 0, pady = 1)

        # Log clear button
        tk.Button(self, text = "Clear", font = ("Roboto", 8), bg = self.bgc, fg = "white",
            width = 4, height = 1, command = self.clear_log).grid(row = 2, column = 8)

        # Log box
        self.logbox = tkscrolled.ScrolledText(self, width = 50, height = 15,
            bg = "grey15", fg = "green2", font = "consolas")
        self.logbox.grid(row = 3, column = 0, columnspan = 9)

    def clear_log(self):
        self.logbox.delete(1.0, tk.END)

    def show_msg(self, msg):
        self.msgbox.delete(1.0, tk.END)
        self.msgbox.insert(1.0, msg)

    def show_file(self, filedir):
        reply = messagebox.askquestion("Show file", "File has been saved successfully.\nDo you want to open it now?")
        if reply == "yes":
            # Cross platform
            opener = ""
            if sys.platform == "win32":
                os.startfile(filedir)
                return
            if sys.platform == "linux":
                opener = "xdg-open "
            elif sys.platform == "darwin":
                opener = "open "
            os.system(opener + filedir)


    def get_save_dir(self):
        savedir = filedialog.asksaveasfilename(title = "Give file name with correct extension")
        if savedir == "":
            messagebox.showwarning(title = "Whoops!", message = "File not saved! Enter a valid save directory.")
            return None
        return savedir


if __name__ == "__main__":
    print("Please run the main.py file.")

    # Test
    # gui = Gui()
    # gui.mainloop()