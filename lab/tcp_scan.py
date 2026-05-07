#!/usr/bin/env python3

from scapy.all import *

pkt = sr1(IP(dst="192.168.18.1")/TCP(dport=80, flags="S"), timeout=1, inter=0.5)

