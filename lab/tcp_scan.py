#!/usr/bin/env python3

import sys
from scapy.all import *

# Linux
# sudo ./bin/python3 tcp_scan.py

width = 60
title = "Port Scan with TCP & sr"
print(width * "#")
print()
print(title.center(width))
print()
print(width * "#")

try:
    ans, unans = sr(IP(dst="192.168.18.1")/TCP(dport=[22,80,443], flags="S"), 
        timeout=3, inter=0.5, retry=0)

    for sent, received in ans:
        if received.haslayer(IP):
            print(f"Response from {received[IP].src}")

        if not received.haslayer(TCP):
            print("  |- Not a TCP response")
            continue

        received.summary()
        print(f" |- Src port: {received[TCP].sport}")
        print(f" |- Dst port: {received[TCP].dport}")
        print(f" |- Sequence number: {received[TCP].seq}")
        print(f" |- Acknowledgment number: {received[TCP].ack}")
        print(f" |- Data Offset:{received[TCP].dataofs}")
        print(f" |- Reserved: {received[TCP].reserved}")

        flag = received[TCP].flags
        if flag == 0x12:
            print(" |- Flags: SA (SYN-ACK) → Port OPEN")
        elif flag == 0x14:
            print(" |- Flags: RA (RST-ACK) → Port CLOSED")
        else:
            print(f" |- Flags: {flag}")

        print(f" |- Window: {received[TCP].window}")
        print(f" |- Checksum: {received[TCP].chksum}")
        print(f" |- Urgent Pointer: {received[TCP].urgptr}")


    print("\n[+] Filtered/Blocked ports (no response):")
    for sent in unans:
        print(f"    Port {sent[TCP].dport}: FILTERED (timeout)")

    print(f"\n✅ Analysis completed: {len(ans)} responses, {len(unans)} unanswered")


except Exception as e:
    print(f"An error occured => {e}")
    sys.exit(1)

sys.exit(0)