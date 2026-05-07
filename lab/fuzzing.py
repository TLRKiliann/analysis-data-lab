#!/usr/bin/env python3

from scapy.all import *
import sys

# Linux
# sudo ./bin/python3 specials_filters.py

width = 90
title = "Fuzzing with Scapy"
subtitle = "(Test how the OS handles invalid protocols)"
print('#' * width)
print()
print(title.center(width))
print(subtitle.center(width))
print()
print('#' * width)

# ICMP
# pkt = sr1(IP(dst="192.168.18.1-10", proto=(1))/ICMP()/"SCAPY", retry=0, timeout=3, inter=0.5)

start_text = "This may take a while..."
print(start_text)

try:
        # A lower level IP Scan can be used to enumerate supported protocols:
        ans, unans = sr(IP(dst="192.168.18.1", proto=(0,255))/"SCAPY", retry=0, timeout=3, inter=0.5)

        for sent, received in ans:
                print(f"Response received from : {received[IP].src}")
        
                # not recommanded
                received.summary()

                # Champs IP critiques pour le fuzzing
                print(f"  ├─ Protocol: {received[IP].proto} (réponse du proto {sent[IP].proto} envoyé)")
                print(f"  ├─ TTL: {received[IP].ttl} (indique l'OS: {received[IP].ttl} = ?)")
                print(f"  ├─ Length: {received[IP].len} octets")
                print(f"  ├─ ID: {received[IP].id} (fragment tracking)")
                print(f"  ├─ Flags: {received[IP].flags} (DF, MF)")
                print(f"  ├─ Fragment offset: {received[IP].frag}")
                print(f"  ├─ Checksum: {received[IP].chksum} (0x{received[IP].chksum:04x})")
                print(f"  ├─ TOS/DSCP: {received[IP].tos} (0x{received[IP].tos:02x})")

                if received.haslayer(Raw):
                        print(f"Payload received : {received[Raw].load}")

except Exception as e:
        print("An error occured => {e}")
        sys.exit(1)

print(f"\n✅ Analysis completed - {len(ans)} response received, {len(unans)} without response")

del ans, unans

sys.exit(0)