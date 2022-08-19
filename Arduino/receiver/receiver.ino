#include "receiver.h"
#include "config.h"

Receiver* receiver;

void setup()
{
    Serial.begin(9600);
    Serial.print("HEloo\n");
    receiver = new Receiver();
}

void loop()
{
    if (Receiver::getSensor())
    {
        String msg = receiver->receive();

        // Signal for python script
        Serial.println(String(MSG_IND_BYTE));
        Serial.println(msg);
    }
}
