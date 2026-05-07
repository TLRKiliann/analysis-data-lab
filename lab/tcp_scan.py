#!/usr/bin/env python3

from scapy.all import *

# Linux
# sudo ./bin/python3 tcp_scan.py

width = 60
title = "Port Scan with TCP & sr1"
print(width * "#")
print()
print(title.center(width))
print()
print(width * "#")

pkt = sr1(IP(dst="192.168.18.1")/TCP(dport=80, flags="S"), timeout=3, inter=0.5, retry=0)
pkt.show()