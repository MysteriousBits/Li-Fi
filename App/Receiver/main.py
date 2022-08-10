import gui
import receiver

app = gui.Gui()
try:
    arduino = receiver.Arduino(app)
except:
    print("Connect an arduino and check if the port name is correct in config.py file.")
    quit()

# Run the receiver and gui in 2 seperate threads
app.after(1, arduino.sync)
app.mainloop()