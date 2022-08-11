import gui
import receiver
from threading import Thread

app = gui.Gui()
try:
    arduino = receiver.Arduino(app)
except:
    print("Connect an arduino and check if the port name is correct in config.py file.")
    quit()

# Run the receiver and gui in 2 seperate threads
thread = Thread(target = arduino.sync)
thread.start()
app.mainloop()
# Stop the thread
arduino.synced = False