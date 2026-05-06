#!/usr/bin/env python3

from scapy import Ether, IP, TCP, send, sendp

text_start = """
***************
*             *
*** START ! ***
*             *
***************
"""
print(text_start)

text_intro = '''
####### ####### ####### ####### ####### ####### ####### #######
tcpdump CMD
sudo tcpdump -i en1 -v 'tcp[tcpflags] & (tcp-syn|tcp-fin) != 0
sudo tcpdump -i en1 -n host 54.198.84.224
sudo tcpdump -i en1 -n icmp -w capture.pcap
####### ####### ####### ####### ####### ####### ####### #######
'''
print(text_intro)

tcp_text = """
#################
TCP Segment build 
#################
"""
print(tcp_text)

fake_mac = "de:ad:be:ef:ca:fe"
fake_ip = "192.168.40.10"

pkt = Ether(src=fake_mac)/IP(src=fake_ip, dst="54.198.84.224", flags=2)/TCP(sport=443, dport=80, seq=0, ack=0, flags="A", window=8192)
print(pkt.summary())
print("This is IP src: ", pkt.sprintf("%IP.flags%"))

print("IP flag", pkt[IP].flags)
print("TCP flag", pkt[TCP].flags) 

pkt.show()

print("\n---\n")

pkt.show2()


        # seq       = 0
        # ack       = 0
        # dataofs   = None
        # reserved  = 0
        # flags     = S
        # window    = 8192
        # chksum    = None
        # urgptr    = 0
        # options   = []

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

data = b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
complete_combo = pkt_comb / data

sendp(complete_combo, iface="en1")