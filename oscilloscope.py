import fire
import serial
from serial.tools import list_ports


def printToConsole():
    '''Prints two newlines, takes no arguments'''
    print('\n\n')
    return
    
def getPorts():
    '''Returns list of ports'''
    return list_ports.comports()

def main(serial_port, baud=9600, time=2, lines=10):
    '''Prints data to the console from the desired serial port'''
    data = serial.Serial(serial_port, baud, timeout=time)
    for i in range(lines):
        print(data.readline())
    data.close()

if __name__ == '__main__':
    fire.Fire()