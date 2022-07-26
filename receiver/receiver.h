/* Receiver class header @lifi_project */

#ifndef RECEIVER_H
#define RECEIVER_H

#include <Arduino.h>

class Receiver
{
public:
	// getBitFunc => A function pointer, return type = bool
	// should return the current sensor value, either 0 or 1
	Receiver(bool (*getBitFunc)());

	// Recieves signal from the transmitter and return the message
	// Must be called after getting the start bit signal
	String receive();

private:
	bool (*getBit)();
};

#endif
