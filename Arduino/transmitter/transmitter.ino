#include "transmitter.h"
#include "config.h"

Transmitter* transmitter;

void setup()
{
    Serial.begin(9600);
    Serial.print("HEloo\n");
    transmitter = new Transmitter();
}

void loop()
{
    if (Serial.available())
    {
        String msg = Serial.readString();

        // Check file
        if (msg[0] == FILE_IND_BYTE)
        {
            delay(20 * INTERVAL);
            transmitter->sendFile(Serial.readString());
        }
        else transmitter->transmit(msg);
    }
}
