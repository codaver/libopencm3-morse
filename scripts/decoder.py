from sys import *
from serial import *
from re import *

device = '/dev/cu.usbserial' # Change this to your UART-USB connector port.

port = Serial(device, 115200)

MORSE_CODE_DICT = { 
    int('101'   , 2) : 'A',
    int('11000' , 2) : 'B',
    int('11010' , 2) : 'C',
    int('1100'  , 2) : 'D',
    int('10'    , 2) : 'E',
    int('10010' , 2) : 'F',
    int('1110'  , 2) : 'G',
    int('10000' , 2) : 'H',
    int('100'   , 2) : 'I',
    int('10111' , 2) : 'J',
    int('1101'  , 2) : 'K',
    int('10100' , 2) : 'L',
    int('111'   , 2) : 'M',
    int('110'   , 2) : 'N',
    int('1111'  , 2) : 'O',
    int('10110' , 2) : 'P',
    int('11101' , 2) : 'Q',
    int('1010'  , 2) : 'R',
    int('1000'  , 2) : 'S',
    int('11'    , 2) : 'T',
    int('1001'  , 2) : 'U',
    int('10001' , 2) : 'V',
    int('1011'  , 2) : 'W',
    int('11001' , 2) : 'X',
    int('11011' , 2) : 'Y',
    int('11100' , 2) : 'Z',
    int('101111', 2) : '1',
    int('100111', 2) : '2',
    int('100011', 2) : '3',
    int('100001', 2) : '4',
    int('100000', 2) : '5',
    int('110000', 2) : '6',
    int('111000', 2) : '7',
    int('111100', 2) : '8',
    int('111110', 2) : '9',
    int('111111', 2) : '0',
}


while True:
    line = port.readline().rstrip()
    if len(line) > 1:
        print(line.decode('ascii'))
    else:
        result = int.from_bytes(line, byteorder='little')
        print(MORSE_CODE_DICT[result])

