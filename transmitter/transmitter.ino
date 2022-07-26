#include "transmitter.h"

Transmitter* transmitter;

void setup()
{
    Serial.begin(9600);
    Serial.print("\nHEloo\n");
    transmitter = new Transmitter();
}

void loop()
{
    if (Serial.available())
    {
        transmitter->transmit(Serial.readString());
    }
}
