/* Transmitter class header @lifi_project */

#include <Arduino.h>

class Transmitter
{
public:
  Transmitter();

  // msg -> The input message to transmit
  void transmit(String msg);

private:
  void sendByte(char Byte);
  void sendBit(bool BIT);
};
