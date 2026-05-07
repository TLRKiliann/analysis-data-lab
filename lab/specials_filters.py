#!/usr/bin/env python3

from scapy.all import *

txt_intro = """
#####################################

        \nFilters with Scapy\n

#####################################
"""
print(txt_intro)

# A lower level IP Scan can be used to enumerate supported protocols:
ans, unans = sr(IP(dst="172.18.1.1", proto=(0,255))/"SCAPY", retry=0)

for emis, recu in ans:
    print(f"Réponse reçue de : {recu[IP].src}")
    
    # not recommanded
    recu.show()
    
    if recu.haslayer(Raw):
        print(f"Charge utile reçue : {recu[Raw].load}")

print(f"\n✅ Analyse terminée - {len(ans)} réponses reçues, {len(unans)} sans réponse")
