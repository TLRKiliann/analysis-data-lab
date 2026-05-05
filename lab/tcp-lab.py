#!/usr/bin/env python3

from scapy.all import *

tcp_text = """
#################
TCP Segment build 
#################
"""
print(tcp_text)

pkt = Ether()/IP()/TCP(dport=80)
print(pkt.summary())
print(pkt.sprintf("%Ether.src% > %IP.src%"))

print("\n---\n")

tcp_data_txt = """
############################################################
TCP packet with data with send to httpbin.org (IP - layer 3)
############################################################
"""
print(tcp_data_txt)

pktData = IP(dst="54.198.84.224")/TCP(dport=80)/b"GET / HTTP/1.1\r\n\r\n"
send(pktData)

print("\n---\n")

# tcp_sr1 = """ 
# TCP packet with SYN with sr1 = response
# """
# print(tcp_sr1)

# fake_mac = "de:ad:be:ef:ca:fe"
# pktSr1 = Ether(src=fake_mac)/IP(dst="54.198.84.224")/TCP(dport=80, flags="S")
# reponse = sr1(pktSr1, timeout=2, iface="en1")

# if reponse:
#     reponse.show()

print("\n---\n")

tcp_comb = """
#####################
TCP packet with data
#####################
"""
print(tcp_comb)

pkt_comb = Ether()/IP(dst="54.198.84.224")/TCP(dport=80)

donnees = b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
pkt_comb_complet = pkt_comb / donnees

sendp(pkt_comb_complet, iface="en1")

print("\n---")