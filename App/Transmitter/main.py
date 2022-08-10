import gui
import sender

try:
    arduino = sender.Arduino()
except:
    print("Connect an arduino and check if the port name is correct in config.py file.")
    quit()
    
app = gui.Gui(arduino)

# Run the gui and logger in 2 seperate threads
app.after(1, lambda: arduino.log(app.logbox))
app.mainloop()