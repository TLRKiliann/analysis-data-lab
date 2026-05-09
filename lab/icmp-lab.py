#!/usr/bin/env python3

import sys
from scapy.all import *

# sudo ./bin/python3 icmp-lab.py

width = 60
text_icmp = "ICMP as PING"
print(width * "#")
print()
print(text_icmp.center(width))
print()
print(width * "#")

fake_mac = "de:ad:be:ef:ca:fe"
fake_ip = "192.168.18.44"

# verify your internet interface
iface = "eth0"

response = sr1(IP(dst="8.8.8.8")/ICMP(), timeout=3, iface=iface, verbose=True)

if response:
    print(f"✅ IP dst response ok !")
else:
    print(f"❌ No response from IP dst...")