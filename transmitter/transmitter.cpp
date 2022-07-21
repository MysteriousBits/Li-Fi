/* transmitter.cpp, Transmitter class @lifi_project */

#include "config.h"
#include "transmitter.h"

Transmitter::Transmitter()
{
  pinMode(PIN, OUTPUT);
  sendBit(0);
  Serial.print("\nTransmitter initiated.\n");
}

void Transmitter::transmit(String msg)
{
  if (msg.length() > MAX_LEN)
  {
    Serial.print("\nString size too big.\n");
    return;
  }

  Serial.println("\nSending message: \"" + msg + "\"...");
  unsigned long before = millis();
  sendBit(1);  // Send starting signal
  
  for (auto Byte : msg)
    sendByte(Byte);

  // Send end indicator Byte
  sendByte(END_BYTE);
  sendBit(0);  // Turn off the light
  
  // Logs
  unsigned long after = millis();
  Serial.print("Message sent.\nSent ");
  Serial.print(msg.length());
  Serial.print(" bytes datas in ");
  Serial.print(after - before);
  Serial.println("ms.");
}

void Transmitter::sendByte(char Byte)
{
  for (int pos = 7; pos >= 0; --pos)
  {
    sendBit(Byte & (1 << pos));
  }
}

void Transmitter::sendBit(bool Bit)
{
  digitalWrite(PIN, Bit);
  delay(INTERVAL);
}
