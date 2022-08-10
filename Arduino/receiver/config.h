/*****************************
Config file for li-fi receiver class.
These values will control the behaviour of receiver.
Change the values according to your project setup.
Make sure the values match with the transmitter class.
******************************/

#ifndef CONFIG_H
#define CONFIG_H

#define PIN A0  // Input pin of transmitter led.
#define THREASHOLD 800	// Threashold for ldr (if used), greater = 0 and smaller = 1.
#define INTERVAL 10  // Delay time(in ms) between two bits
#define END_BYTE '\x04'  // Indicator byte(ASCII char) for string end
#define FILE_IND_BYTE '\x05'  // Indicator byte(ASCII char) for file start
#define MAX_LEN 50  // Max length of input string, stops receiving while length is greater.
#define MAX_FILE_SIZE 1000 // Max file size in bytes

#endif