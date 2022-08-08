# Li-Fi
Arduino based lifi communication project. Transfer data through light!  
  
Use an led to transmit data from one arduino and a ldr/photo-diode in another arduino board.  
Upload the transmitter class in transmitter arduino and receiver class in the receiver arduino.  
  
Make sure you edit the `congig.h` properly in both receiver and transmitter class. Also read the sensor value inside `bool getBit()` function in `receiver.ino` and return true if the light is on and false otherwise. **Update:** You don't need to use your own custom `getBit()` function now if you use an ldr. Just pass no arguments to the constructuor and the default implemented function inside the class will be used. You can even use the static `getSensor()` function in your code.    
Note that you may have to threshold the analog input value according to the brightness of the room.