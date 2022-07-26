/******************************************************
Config file for transmitter class.
These values will control the behaviour of transmitter.
Change the values according to your project setup.
Make sure the values match with the receiver class.
*******************************************************/

#ifndef CONFIG_H
#define CONFIG_H

#define PIN 13  // Output pin of transmitter led.
#define INTERVAL 10  // Delay time(in ms) between two bits
#define END_BYTE '\x04'  // Indicator byte(ASCII char) for string end
#define MAX_LEN 50  // Max length of input string, won't transmit if length is greater.

#endif
