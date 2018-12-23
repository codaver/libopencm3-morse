import sys
import serial
import re

device = '/dev/ttyUSB0' # Change this to your UART-USB connector port.

port = serial.Serial(device, 115200)

MORSE_CODE_DICT = { '01':'A', '1000':'B', 
                    '1010':'C', '100':'D', '0':'E', 
                    '0010':'F', '110':'G', '0000':'H', 
                    '00':'I', '0111':'J', '101':'K', 
                    '0100':'L', '11':'M', '10':'N', 
                    '111':'O', '0110':'P', '1101':'Q', 
                    '010':'R', '000':'S', '1':'T', 
                    '001':'U', '0001':'V', '011':'W', 
                    '1001':'X', '1011':'Y', '1100':'Z', 
                    '01111':'1', '00111':'2', '00011':'3', 
                    '00001':'4', '00000':'5', '10000':'6', 
                    '11000':'7', '11100':'8', '11110':'9', 
                    '11111':'0'} 
# You can add more codes if you want. Dot't forget to change max length in morse.c

def decode(line):
    line = line[line.index('1')+1:]
    if line in MORSE_CODE_DICT.keys():
        return MORSE_CODE_DICT[line]
    else:
        return "Unknown code"

while True:
    line = port.readline()
    line = line[:-2]
    if re.match(r"0{7}1", line):
        # Empty message
        pass
    elif re.match(r"[01]{8}", line):
        # Morse code
        symbol=decode(line)
        print symbol
    else:
        # System messages
        print line

