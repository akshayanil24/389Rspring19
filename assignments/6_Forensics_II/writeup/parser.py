#!/usr/bin/env python2

import sys
import struct
import time
# pip install Pillow
from PIL import Image
import io

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0x8BADF00D
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# 4 spaces for magic, 4 for version, 4 for timestamp, 8 for author, and 4 for section_count
# 4 + 4 + 4 + 8 + 4 = 24 => data[0:24] for header
magic, version, timestamp, author, section_count = struct.unpack("<LLL8sL", data[0:24])
# Convert from epoch time to localtime
timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("TIMESTAMP: %s" % timestamp)
print("AUTHOR: %s" % author)
print("SECTION COUNT: %d" % int(section_count))

print("-------  BODY  -------")

# We don't need information from the header anymore so remove first 24 values
data = data[24:]
# Iterate through sections
for section in range(section_count):
    print("-SECTION %d-" % (section + 1))
    stype, slen = struct.unpack("<LL", data[:8])
    svalue = ""
    # Trim stype and slen
    data = data[8:]

    print("Length: %d" % slen)
    if stype == 0x1:
        print("Type: ASCII")
        # s - char array
        print("Value: " + str(struct.unpack(("<%ds" % slen), data[:slen])[0]))
    elif stype == 0x2:
        print("Type: UTF-8")
        # s - char array
        print("Value: " + str(struct.unpack(("<%ds" % slen), data[:slen])[0].decode('utf-8')))
    elif stype == 0x3:
        print("Type: WORDS")
        # L - unsigned long
        print("Value: " + str(struct.unpack(("<"+((slen/4)*"L")), data[:slen])[0]))
    elif (stype == 0x4):
        print("Type: DWORDS")
        # L - unsigned long
        print("Value: " + str(struct.unpack(("<"+((slen/8)*"L")), data[:slen])[0]))
    elif (stype == 0x5):
        print("Type: DOUBLES")
        # L - unsigned long
        print("Value: " + str(struct.unpack(("<"+((slen/8)*"L")), data[:slen])[0]))
    elif (stype == 0x6):
        print("Type: COORD")
        # d - double
        print("Value: " + str(struct.unpack(("<dd"), data[:slen])))
    elif (stype == 0x7):
        print("Type: REFERENCE")
        # L - unsigned long
        print("Value: " + str(struct.unpack(("<L"), data[:slen])))
    elif (stype == 0x8):
        print("Type: PNG")
        print("Value: Displayed in pop-up")
        # B - unsigned char
        # Signature as list grabbed from blog.netspi.com
        image = Image.open(io.BytesIO(bytearray([0x89,0x50,0x4E,0x47,0x0D,0x0A,0x1A,0x0A] + list(struct.unpack("<" + ("%s" % (slen*"B")), data[:slen])))))
        # Run 'sudo apt-get install imagemagick' for image.show() to work
        image.show()
    elif (stype == 0x9):
        print("Type: GIF87")
        print("Value: Displayed in pop-up")
        # B - unsigned char
        # Signature as list grabbed from blog.netspi.com
        image = Image.open(io.BytesIO(bytearray([0x47,0x49,0x46,0x38,0x37,0x61] + list(struct.unpack("<" + ("%s" % (slen*"B")), data[:slen])))))
        image.show()
    elif (stype == 0xA):
        print("Type: GIF89")
        print("Value: Displayed in pop-up")
        # B - unsigned char
        # Signature as list grabbed from blog.netspi.com
        image = Image.open(io.BytesIO(bytearray([0x47,0x49,0x46,0x38,0x39,0x61] + list(struct.unpack("<" + ("%s" % (slen*"B")), data[:slen])))))
        image.show()
    # Print new line to make output easier to read
    print
    # Trim already read data
    data = data[slen:]
