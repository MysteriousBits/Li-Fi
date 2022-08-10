import gui
import receiver

app = gui.Gui()
arduino = receiver.Arduino(app)

# Run the receiver and gui in 2 seperate threads
app.after(1, arduino.sync)
app.mainloop()