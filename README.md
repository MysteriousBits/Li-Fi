# Li-Fi
Arduino based lifi communication project. Transfer data through light!  

Use an led to transmit data from one arduino and a ldr/photo-diode in another arduino board.  
Upload the transmitter class in transmitter arduino and receiver class in the receiver arduino.  
  
Make sure you edit the `congig.h` properly in both receiver and transmitter class. Also read the sensor value inside `bool getBit()` function in `receiver.ino` and return true if the light is on and false otherwise.  
Note that you may have to threshold the analog input value according to the brightness of the room.