#!/usr/bin/env python3

from scapy.all import *

width = 60
three_way = "Three-Way Handshake"

print(width * "#")
print()
print(three_way.center(width))
print()
print(width * "#")

get_request = b'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n'

ip_layer = IP(dst="93.184.216.34")  # IP of exemple.com

port_src = RandNum(1024, 65535)

# 1. Handshake TCP
syn_packet = ip_layer/TCP(sport=port_src, dport=80, flags="S", seq=1000)
syn_ack_response = sr1(syn_packet) # Send SYN & received SYN-ACK

# 2. Send ACK
ack_packet = ip_layer/TCP(sport=port_src, dport=80, flags="A",
                          seq=syn_ack_response.ack,
                          ack=syn_ack_response.seq + 1) / get_request
reply = sr1(ack_packet) # Send request & received response

if reply and Raw in reply:
    print(reply[Raw].load) # Display HTML content