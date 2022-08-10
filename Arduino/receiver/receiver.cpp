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

    // Check for file start signal
    if (msg[0] == FILE_IND_BYTE)
    {
        getFile(msg);
        return msg;
    }

    // Logs
    unsigned long after = millis();
    if (msg.length() == MAX_LEN)
        Serial.println("Maximum message length reached.");
    Serial.println("Recieved message:\n" + msg);
    Serial.println("\nRecieved ");
    Serial.print(msg.length());
    Serial.print(" bytes data in ");
    Serial.print(after - before);
    Serial.println("ms.");

    return msg;
}

void Receiver::getFile(String signal)
{
    // extract file size from signal
    String size = signal;
    size.remove(0, 1);
    int filesize = signal.toInt();
    if (filesize > MAX_FILE_SIZE)
    {
        Serial.println(size + " bytes file size is too big. File can't be received.");
        Serial.println("Increase MAX_FILE_SIZE if you want.");
        Serial.println("Restart the transmitter now to avoid unwanted behaviour.");
        delay(10 * INTERVAL);
        return;
    }

    Serial.println("Started receiving file...");
    Serial.println("Will receive " + size + " bytes data.\n");
    unsigned long before = millis();

    // Wait till the halfway of first bit
    delay(1.5 * INTERVAL);

    String file = "";
    while (filesize--)
        file += getByte();

    // Signal for python script to save the file
    Serial.println(signal);
    Serial.println(file);

    // Logs
    unsigned long after = millis();
    Serial.println("\nRecieved " + size + " bytes data in ");
    Serial.print(after - before);
    Serial.println("ms.");
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