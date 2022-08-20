import gui
import sender
from threading import Thread

try:
    arduino = sender.Arduino()
except:
    print("Connect an arduino and check if the port name is correct in config.py file.")
    quit()
    
app = gui.Gui(arduino)

# Run the gui and logger in 2 seperate threads
logger = Thread(target = arduino.log, args = (app.logbox,))
logger.start()
app.mainloop()
# Stop the thread
arduino.stop()