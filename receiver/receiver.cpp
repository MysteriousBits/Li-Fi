/* receiver.cpp, Receiver class @lifi_project */

#include "config.h"
#include "receiver.h"

Receiver::Receiver(bool (*getBitFunc)() = nullptr)
{
    if (!getBitFunc) getBitFunc = &getSensor;

    getBit = getBitFunc;

    Serial.println("Receiver initiated.");
}

String Receiver::receive()
{
    Serial.println("Started receiving signal...");
    unsigned long before = millis();

    // Wait till the halfway of first bit
    delay(1.5 * INTERVAL);

    String msg = "";

    while(msg.length() <= MAX_LEN)
    {
        char Byte = getByte();

        if (Byte != END_BYTE) msg += Byte;
        else break;
    }

    // Logs
    unsigned long after = millis();
    if (msg.length() == MAX_LEN)
        Serial.println("Maximum message length reached.");
    Serial.println("Recieved message:\n" + msg);
    Serial.println("\nRecieved ");
    Serial.print(msg.length());
    Serial.print(" bytes datas in ");
    Serial.print(after - before);
    Serial.println("ms.");

    return msg;
}

static bool Receiver::getSensor()
{
    return analogRead(PIN) < THREASHOLD;
}

char Receiver::getByte()
{
    char Byte = 0;
    for (int pos = 7; pos >= 0; --pos)
    {
        Byte |= (getBit() << pos);
        delay(INTERVAL);
    }
    return Byte;
}