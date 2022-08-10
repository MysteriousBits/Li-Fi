import gui
import sender

arduino = sender.Arduino()
app = gui.Gui(arduino)

# Run the gui and logger in 2 seperate threads
app.after(1, lambda: arduino.log(app.logbox))
app.mainloop()