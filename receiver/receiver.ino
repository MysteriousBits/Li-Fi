#include "receiver.h"

Receiver* receiver;

void setup()
{
    Serial.begin(9600);
    Serial.print("\nHEloo\n");
    receiver = new Receiver(&getBit);
}

void loop()
{
    if (getBit())
    {
        String msg = receiver->receive();
    }
}

bool getBit()
{
    bool Bit = 0;
    // Read sensor and process...

    return Bit;
}