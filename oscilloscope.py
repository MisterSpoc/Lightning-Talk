import fire
import serial
from serial.tools import list_ports

def printToConsole():
    print('\n\n')
    
def getPorts():
    return list_ports.comports()

def main(serial_port, baud=9600, time=2, lines=10):
    data = serial.Serial(serial_port, baud, timeout=time)
    for i in range(lines):
        print(data.readline())
    data.close()

if __name__ == '__main__':
    fire.Fire()