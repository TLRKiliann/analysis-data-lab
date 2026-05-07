#!/usr/bin/env python3

from scapy.all import *

text_intro = '''
####### ####### ####### ####### ######

\nFields overview with show() & show2()\n

####### ####### ####### ####### #######
'''
print(text_intro)

print("\n--- Ether ---\n")

pkt = Ether()
pkt.show()

print("\n--- Ether + ARP ---\n")

pkt_5 = Ether()/ARP()
pkt_5.show()

print("\n--- IP ---\n")

pkt_2 = IP()
pkt_2.show()

print("\n--- IP + ICMP ---\n")

pkt_3 = IP()/ICMP()
pkt_3.show()

print("\n--- IP + TCP ---\n")

pkt_4 = IP()/TCP()
pkt_4.show()

print("\n--- Ether + IP + TCP with show() ---\n")

pkt_6 = Ether()/IP()/TCP()
pkt_6.show()

print("\n--- Ether + IP + TCP with show2() ---\n")

pkt_6.show2()

# View raw bytes
print("\n=== RAW BYTES OCTETS ===")
hexdump(pkt_4)

# Extract the header only (first 20 bytes or octets)
header_bytes = bytes(pkt_4)[:20]
print(f"\nHeader IP (20 bytes or octets) : {header_bytes.hex(' ')}")