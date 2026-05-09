#!/usr/bin/env python3

import sys
from scapy.all import *

# sudo ./bin/python3 icmp-lab.py

width = 60
text_icmp = "ARP-ICMP scan"
subtitle = "(you can also use tcpdump)"
print(width * "#")
print()
print(text_icmp.center(width))
print(subtitle.center(width))
print()
print(width * "#")

fake_mac = "de:ad:be:ef:ca:fe"

pkt = Ether(src=fake_mac)/IP(dst="8.8.8.8")/ICMP()/b"Payload"

print(f"\nMAC source: {fake_mac}")
print(f"Destination: 8.8.8.8\n")

# Sniffer with ARP & ICMP
arp_filter = "arp or icmp"
sniffer = AsyncSniffer(filter=arp_filter, count=10, timeout=5)
sniffer.start()

# Sendp
sendp(pkt, verbose=True)

time.sleep(1)
results = sniffer.stop()

print(f"\n{len(results)} pkt received:")
for pkt in results:
    if ARP in pkt:
        print(f" |- ARP: {pkt[ARP].op} - {pkt[ARP].psrc} -> {pkt[ARP].pdst}")
    elif ICMP in pkt:
        print(f" |- ICMP: Type {pkt[ICMP].type} from {pkt[IP].src} to {pkt[IP].dst}")
        if pkt[ICMP].type == 0:
            if pkt.haslayer(Raw):
                print(f" |- Payload received: {pkt[Raw].load}")
        else:
            print(" |- ICMP Type is not equal to reply (0)")

    else:
        print("No pkt received !")
        sys.exit(1)
sys.exit(0)