#!/usr/bin/env python3

from scapy import Ether, IP, ICMP, AsyncSniffer, sendp
import time

text = """
######################################################
send() - Couche 3 (Réseau/IP)
Travaille au niveau IP (pas besoin de couche Ethernet)
Envoie des paquets (datagrammes IP)
Le système détermine automatiquement l'Ethernet/MAC
Nécessite seulement la couche IP et au-dessus
------------------------------------------------------
sendp() - Couche 2 (Liaison/Ethernet)
Travaille au niveau Ethernet (frame complète)
Envoie des trames (adresse MAC source/destination)
Vous devez spécifier l'interface
Nécessite explicitement la couche Ethernet
######################################################
"""
print(text)

fake_mac = "de:ad:be:ef:ca:fe"

pktS = Ether(src=fake_mac)/IP(dst="8.8.8.8")/ICMP()

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

print("end !")