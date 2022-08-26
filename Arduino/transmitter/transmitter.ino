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
            msg.remove(0, 1);
            // Extract file size from signal
            int size = msg.toInt();
            delay(1);
            transmitter->sendFile(size);
        }
        else transmitter->transmit(msg);
    }
}
