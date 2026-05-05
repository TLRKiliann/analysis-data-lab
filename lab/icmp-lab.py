#!/usr/bin/env python3

from scapy.all import *
import time

text = '''
send() - Couche 3 (Réseau/IP)
Travaille au niveau IP (pas besoin de couche Ethernet)
Envoie des paquets (datagrammes IP)
Le système détermine automatiquement l'Ethernet/MAC
Nécessite seulement la couche IP et au-dessus

sendp() - Couche 2 (Liaison/Ethernet)
Travaille au niveau Ethernet (frame complète)
Envoie des trames (ye need MAC source/destination)
Vous devez spécifier l'interface
Nécessite explicitement la couche Ethernet
'''
print(text)

# Construction du paquet
pkt = Ether()/IP()/TCP(dport=80);
print(pkt.summary());

print(pkt.sprintf("%Ether.src% > %IP.src%"));

print("---\n");

fausse_mac = "de:ad:be:ef:ca:fe"

pktS = Ether(src=fausse_mac)/IP(dst="8.8.8.8")/ICMP()

sniffer = AsyncSniffer(filter="icmp and host 8.8.8.8", iface="en1", timeout=5)
sniffer.start()

time.sleep(0.5)
sendp(pktS, iface="en1", verbose=True)

time.sleep(2)
sniffer.stop()

if len(sniffer.results) > 1:
    print(f"✅ Réponse reçue ! {len(sniffer.results)} paquets capturés")
    for pkt in sniffer.results:
        if ICMP in pkt and pkt[ICMP].type == 0:
            print(f"   Réponse de {pkt[IP].src}")
else:
    print("❌ Pas de réponse")

'''
tcpdump CMD => https://hackertarget.com/tcpdump-examples/
===========

$ sudo tcpdump -i eth0 -nn -s0 -c 1 -v -X -G 5 port 80

-A = ASCII
-X = hexadecimal & ASCII

-c = nb de paquet

-G = temps d'attente en sec 

-nn = A single (n) will not resolve hostnames. A double (nn) will not resolve hostnames or ports. 
This is handy for not only viewing the IP / port numbers but also when capturing a large amount 
of data, as the name resolution will slow

-v : Verbose, using (-v) or (-vv) increases the amount of detail shown in the output, often showing 
more protocol specific information.

request:
sudo tcpdump -i en1 -c 1 -v -X 'icmp[icmptype] != icmp-echoreply'

reply:
sudo tcpdump -i en1 -c 1 -v -X 'icmp[icmptype] != icmp-echo'


sudo tcpdump 'tcp[tcpflags] & (tcp-syn|tcp-fin) != 0
sudo tcpdump -i en0 -n host 8.8.8.8
sudo tcpdump -i en0 -n icmp -w capture.pcap
'''