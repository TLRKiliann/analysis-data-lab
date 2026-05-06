#!/usr/bin/env python3

from scapy import IP, TCP

text_intro="""
====================================
\nIf you wanna test something with pkt\n
====================================
"""
print(text_intro)

fake_ip = "192.177.32.4"

pkt = IP(ttl=64, proto=6, src=fake_ip, dst="192.177.32.22")/TCP(dataofs=5 ,flags="S", sport=443, dport=80)

ip_src = pkt[IP].src
print("ip src =", ip_src)

addr_dst = pkt[IP].dst
print("ip dst =", addr_dst)

ttl_display = pkt[IP].ttl
print("ttl =", ttl_display)

protocol_ip = pkt[IP].proto
print("proto IP", protocol_ip)

# Don't not use "len" from IP !

port_src = pkt[TCP].sport
print("port src =", port_src)

port_dst = pkt[TCP].dport
print("port dst =", port_dst)

data_of_set = pkt[TCP].dataofs
print("dataofs =", data_of_set)

tcp_flag = pkt[TCP].flags
print("tcp_flag =", tcp_flag)

window_tcp = pkt[TCP].window
print("window =", window_tcp)

# ?
check = pkt[TCP].chksum
print("checksum =", check)

pkt.show()

print("end")