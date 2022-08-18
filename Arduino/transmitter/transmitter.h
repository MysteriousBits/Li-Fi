/* Transmitter class header @lifi_project */

#ifndef TRANSMITTER_H
#define TRANSMITTER_H

#include <Arduino.h>

class Transmitter
{
public:
    Transmitter();

    // Mesage transmitter method
    // msg => The input message to transmit
    // logs => turn logging on/off
    void transmit(String msg);
    // File transmitter method
    // file => Byte data of binary file
    void sendFile(String file);

private:
    void sendByte(char Byte);
    void sendBit(bool Bit);
};

#endif