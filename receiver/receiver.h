/* Receiver class header @lifi_project */

#ifndef RECEIVER_H
#define RECEIVER_H

#include <Arduino.h>

class Receiver
{
public:
    // getBitFunc => (Optional) A function pointer, return type = bool
    // should return the current sensor value, either 0 or 1
    // pass nothing if you want to use the default implementation for ldr.
    Receiver(bool (*getBitFunc)() = nullptr);

    // return 1 if the sensor is receiving light signal
    // or 0 otherwise.
    static bool getSensor();

    // Recieves signal from the transmitter and return the message
    // Must be called after getting the start bit signal
    String receive();

private:
    bool (*getBit)();
    char getByte();
    void getFile(String signal);
};

#endif
