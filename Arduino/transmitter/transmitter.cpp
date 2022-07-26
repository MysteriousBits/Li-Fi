/* transmitter.cpp, Transmitter class @lifi_project */

#include "config.h"
#include "transmitter.h"

Transmitter::Transmitter()
{
    pinMode(PIN, OUTPUT);
    sendBit(0);
    Serial.println("\nTransmitter initiated.");
    Serial.println("Feel free to use the reset button in arduino if you see any unwanted behaviour (:.");
}

void Transmitter::transmit(String msg)
{
    if (msg.length() > MAX_LEN)
    {
        Serial.println("String size too big.");
        return;
    }

    Serial.println("\nSending message: \"" + msg + "\"...");
    unsigned long before = millis();
    sendBit(1);  // Send starting signal
    
    for (char Byte : msg)
        sendByte(Byte);

    // Send end indicator Byte
    sendByte(END_BYTE);
    sendBit(0);  // Turn off the light
    
    // Logs
    unsigned long after = millis();
    Serial.print("Message sent.\nSent ");
    Serial.print(msg.length());
    Serial.print(" bytes data in ");
    Serial.print(after - before);
    Serial.println("ms.");
}

void Transmitter::sendFile(int Size)
{
    if (Size > MAX_FILE_SIZE)
    {
        Serial.println("Can't send file. File size too big.");
        Serial.println("Restart the arduino to avoid unwanted behaviour.");
        delay(10 * INTERVAL);
        return; 
    }

    Serial.println("Reading file.");
    byte *file = new byte[Size];

    // Wait till the first byte
    while (!Serial.available());

    for (int i = 0; i < Size; ++i)
    {
        file[i] = Serial.read();
        // Wait till the next byte if it wasn't the last one.
        while (!Serial.available() && i < size - 1);
    }


    // Signal for file start with file size
    String msg = "";
    msg += FILE_IND_BYTE;
    msg += String(Size);
    transmit(msg);
    // delay included at the end of transmit()
    Serial.println("\nSending file...");
    unsigned long before = millis();

    for (int i = 0; i < Size; ++i)
        sendByte(file[i]);

    delete[] file;
    sendBit(0);  // Turn off the light
    // Logs
    unsigned long after = millis();
    Serial.print("File sent.\nSent ");
    Serial.print(String(Size));
    Serial.print(" bytes data in ");
    Serial.print(after - before);
    Serial.println("ms.");
}

void Transmitter::sendByte(char Byte)
{
    for (int pos = 7; pos >= 0; --pos)
        sendBit(Byte & (1 << pos));
}

void Transmitter::sendBit(bool Bit)
{
    digitalWrite(PIN, Bit);
    delay(INTERVAL);
}