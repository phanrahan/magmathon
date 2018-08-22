import serial
import sys


def main(infile, outfile, usb_path):
    print (f"Running with infile={infile}, outfile={outfile}")

    with open(infile, "rb") as f:
        data = f.read()
    print(f"infile length={len(data)}")

    ser = serial.Serial(usb_path, 115200)
    ser.write(data)
    res = ser.read(len(data))
    ser.close()

    with open(outfile, "wb") as f:
        f.write(res)


def usage():
    print(f"usage: {sys.argv[0]} infile outfile usb_path")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        usage()
        exit(1)
    infile = sys.argv[1]
    outfile = sys.argv[2]
    usb_path = sys.argv[3]
    main(infile, outfile, usb_path)
