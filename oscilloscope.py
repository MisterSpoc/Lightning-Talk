import serial
import fire

def printToConsole():
    print()

def main(serial_port, baud=9600, time=1, lines=10):
    data = serial.Serial(serial_port, baud, timeout=time)
    for i in range(lines):
        print(data.readline())
    data.close()

if __name__ == '__main__':
    fire.Fire(main)