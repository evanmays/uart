#!/usr/bin/python3

import serial
from tqdm import tqdm
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

port = "/dev/cu.usbserial-210319B26E8C1"
tosend = [(i).to_bytes(1,byteorder='big') for i in range(256)] # [b'\xef']

print ("Opening %s" % port)
with serial.Serial(port, timeout=4, baudrate=4800, bytesize=8, stopbits=1) as ser:

    for byte in tqdm(tosend):
        time.sleep(0.01) # if you want to see pretty lights of binary increment, then make this 0.1.
        # print("Sending %s" % byte)
        bytes_written = ser.write(byte)
        assert bytes_written == 1, bytes_written

    ret = ser.read(len(tosend))
    
    # print("Got back:")
    # print(ret)
    assert len(ret) == len(tosend), f"{len(ret)} {ret}"
    passed = 0
    tot = 0
    for i in range(len(ret)):
        actual = ret[i:i+1]
        expected = tosend[i]
        is_pass = actual == expected
        pass_str = (bcolors.OKGREEN + "PASS" if is_pass else bcolors.FAIL + "FAIL" ) + bcolors.ENDC
        passed += is_pass
        tot += 1
        print(f"{i:<6} {pass_str:<6} expected {expected.hex():<8} actual {actual.hex():<8}")
    print("TESTS PASS" if passed == tot else f"TESTS FAILED. Passed {passed}/{tot}")