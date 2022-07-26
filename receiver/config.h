/*****************************
Config file for li-fi receiver class.
These values will control the behaviour of receiver.
Change the values according to your project setup.
Make sure the values match with the transmitter class.
******************************/

#ifndef CONFIG_H
#define CONFIG_H

#define PIN A0	// Input pin of transmitter led.
#define INTERVAL 10  // Delay time(in ms) between two bits
#define END_BYTE '\x04'  // Indicator byte(ASCII char) for string end
#define MAX_LEN 50  // Max length of input string, stops receiving while length is greater.

#endif