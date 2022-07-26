/* Transmitter class header @lifi_project */

#ifndef TRANSMITTER_H
#define TRANSMITTER_H

#include <Arduino.h>

class Transmitter
{
public:
    Transmitter();

    // msg => The input message to transmit
    void transmit(String msg);

private:
    void sendByte(char Byte);
    void sendBit(bool BIT);
};

#endif