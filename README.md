
# libopencm3-morse

### Description:

This project demonstrates the exaple of USART communication with STM32L152CDISCOVERY board.
You need to hold the button for 0.5 sec to send "bar" and less to send "dot".
Python script on your device will decode the message.
It is tested only with this board so you might change some code to use it with differet versions.
### Wiring
In addition you need to have some UART-USB connector. We used PL2303.
Connect it like this
Connector - Board
Black wire (GND) - GND pin
Red wire (5V) - EXT_5V pin
Green wire (TX) - USART(x)RX pin (This project is configured to use USART2 so it is PA3)
White wire (RX) - USART(x)TX pin (This project is configured to use USART2 so it is PA2)
### How it works
When you run and reset the board it will blink blue led 3 times showing that the setup was completed succesfully. Then the green led starts to blink. Now you can type your message with the user button. Blue led will show is it pressed or not. To send your message you have to waite timeout time. Now the project suports only 5 sybols lenght codes for [A-Z0-9]. If you enter to much it will send a message.
#### Default values are:
500 ms for "dot"-"bar" deifference.
5000 ms for timeout.
Port configuration "dev/ttyUSB0 115200" (You have to change it to your UART-USB connector port)

### Usage:
```
//Build libopencm3
make
cd src
//Build morse and burn flash
make flash
cd scripts
//Read from USART Result
python3 decode.py
```
