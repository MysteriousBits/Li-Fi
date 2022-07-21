/******************************************************
Config file for transmitter class.
These values will control the behaviour of transmitter.
Change the value of pins, delay time acording to your project setup.
Make sure the interval matches with the receiver class.
*******************************************************/

#ifndef CONFIG_H
#define CONFIG_H

#define PIN 13  // Output pin of transmitter led.
#define INTERVAL 20  // Delay time(in ms) between two bits
#define END_BYTE '#'  // Indicator byte(ASCII char) for string end
#define MAX_LEN 50  // Max length of input string, won't transmit if length is greater.

#endif
