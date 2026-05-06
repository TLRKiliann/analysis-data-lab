<div align="center">
  
# ⚡ analysis-data-lab

*Network scanning tool*

[![Stars](https://img.shields.io/github/stars/TLRKiliann/analysis-data-lab?style=social)](https://github.com/TLRKiliann/analysis-data-lab/stargazers)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/TLRKiliann/analysis-data-lab)](https://github.com/TLRKiliann/analysis-data-lab)

</div>

## Installation

```
# Clone the repository
git clone https://github.com/TLRKiliann/analysis-data-lab.git

# Go to the project folder
cd analysis-data-lab

# Create & activate virtual environment (lab for example)
python3 -m venv lab

source lab/bin/activate

# Update all versions
pip install -r requirements.txt

# Selective update
pip install --upgrade scapy

pip freeze > requirements.txt

# Or update to the latest compatible versions
pip install --upgrade -r requirements.txt

# Enter to the lab folder
cd lab

# Run
python3 any_file.py
```

## Links

- [ICMP-Lab](#icmp-lab)
- [tcpdump CMD](#tcpdump-cmd)
- [IP fields](#ip-fields)
- [TCP fields](#tcp-fields)


```
# Swiftly: 0.0082 sec  ✅
print("IP flag", pkt[IP].flags)

# sprintf: 0.2350 sec  ❌ (~29x slower)
print("This is IP src: ", pkt.sprintf("%IP.flags%"))
```

## ICMP-Lab

A Scapy script that uses tcpdump to analyze sent and received ICMP packets.

Run

```
Terminal 1

sudo python3 icmp-lab.py
```

In another terminal, you can use these CMD with tcpdump

```
Terminal 2

# request
sudo tcpdump -i en1 -c 1 -v -X 'icmp[icmptype] != icmp-echoreply'

# OR

# reply
sudo tcpdump -i en1 -c 1 -v -X 'icmp[icmptype] != icmp-echo'
```

## tcpdump CMD

[https://hackertarget.com/tcpdump-examples/](https://hackertarget.com/tcpdump-examples/)

```
$ sudo tcpdump -i eth0 -nn -c 1 -v -X -G 5 port 80

-i = interface

-A = ASCII

-X = hexadecimal & ASCII

-c = nb de paquet

-G = temps d'attente en sec 

-nn = A single (n) will not resolve hostnames. A double (nn) will not resolve hostnames or ports. 
This is handy for not only viewing the IP / port numbers but also when capturing a large amount 
of data, as the name resolution will slow

-v : Verbose, using (-v) or (-vv) increases the amount of detail shown in the output, often showing 
more protocol specific information.

$ sudo tcpdump -i eth0 -n icmp -w capture.pcap

-w = write

capture.pcap = to capture packet
```

---

## Calculate

0x45, 0x00, 0x00, 0x3C = octets (bytes) en notation hexadécimale

## IP fields

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|Version|  IHL  |Type of Service|          Total Length         | <- Fields
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|         Identification        |Flags|      Fragment Offset    | <- Fields
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|  Time to Live |    Protocol   |         Header Checksum       | <- Fields
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                       Source Address                          | <- Field src
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Destination Address                        | <- Field dst
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Options (if any)    |    Padding           | <- Options
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

# ihl (Internet Header Length)

ihl + options = 32 bits = 4 octets

Minimale value : 5 (5 × 4 = 20 octets)      <= without options
Maximale value : 15 (15 × 4 = 60 octets)    <= with all options

---

ihl = 5  # 20 octets
data_start = ihl * 4  # 20 octets since the beginning

ihl = 8  # 32 octets (header + options)
data_start = ihl * 4  # 32 octets since the beginning

# tos (Type of Service)

8 bits (1 octet)

DSCP (Differentiated Services Code Point) : bits 0-5 (6 bits)

ECN (Explicit Congestion Notification) : bits 6-7 (2 bits)

DSCP (decimal)      DSCP (binaire)      Nom	                            Usage typique
-------------------------------------------------------------------------------------------------------
0                   000000          Best Effort (BE)	            Trafic normal (par défaut)
8                   001000          Class Selector 1 (CS1)          Trafic "à moindre coût" (scavenger)
16                  010000	        Class Selector 2 (CS2)          Trafic de fond
24                  011000	        Class Selector 3 (CS3)          Appels téléphoniques
32                  100000	        Class Selector 4 (CS4)          Vidéoconférence
40                  101000	        Class Selector 5 (CS5)          Voice signaling
46                  101110          Expedited Forwarding (EF)       Voix (priorité maximale)
48                  110000	        Class Selector 6 (CS6)          Routage réseau (OSPF, BGP)
56                  111000	        Class Selector 7 (CS7)          Critical (réseau interne)

ex: <IP(dst="8.8.8.8" tos=0xB8)> # 184 in décimal = DSCP 46 (EF) with 6 bits

ECN value           Binaire             Signification
----------------------------------------------------------------------
0                   00          Non-ECT (ECN not capable) - par défaut
1                   01          ECT(1) (ECN Capable Transport)
2                   10          ECT(0) (ECN Capable Transport)
3                   11          CE (Congestion Experienced)

- Paquet capable ECN (ECT(0))
pkt = IP(dst="8.8.8.8", tos=128)  # ECN=10, DSCP=0

- Paquet avec notification de congestion
pkt = IP(dst="8.8.8.8", tos=192)  # ECN=11, DSCP=0

- Scapy - DSCP marking
voip = IP(tos=0xB8, dst="sip.server.com") / UDP(...)  # DSCP 46 = EF
video = IP(tos=0x88, dst="zoom.us") / UDP(...)        # DSCP 34 = AF41
backup = IP(tos=0x20, dst="backup.server") / TCP(...)  # DSCP 8 = CS1

# flags
[Bit 0 (Reserved)] [Bit 1 (DF)] [Bit 2 (MF)]

# 0x40 = 64 in decimal = bit DF
0x40 = "DF" => flags=0x40 or flags="DF"

# chksum

IP	En-tête seulement	Si l'en-tête est corrompu, on ne sait pas où livrer le paquet !
TCP/UDP	En-tête + données	Vérification complète de bout en bout

```

## TCP fields

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|          Source Port          |       Destination Port        | <- Fields (ports)
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                        Sequence Number                        | <- Field
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Acknowledgment Number                      | <- Field
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|  Data |           |U|A|P|R|S|F|                               |
| Offset| Reserved  |R|C|S|S|Y|I|            Window             | <- Flags !!!
|       |           |G|K|H|T|N|N|                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|           Checksum            |         Urgent Pointer        | <- Fields
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Options (if any)    |    Padding           | <- Options
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                             Data                              |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

# seq
Sequence number

# ack
Acknowledgment Number

# dataofs (Data Offset)

Minimale value : 5 (5 × 4 = 20 octets)      <= without options
Maximale value : 15 (15 × 4 = 60 octets)    <= with all options

# reserved

# flags
SYN, ACK, FIN, RST, PSH, URG

0x20 = "URG"
0x10 = "ACK"
0x08 = "PSH"
0x04 = "RST"
0x02 = "SYN"
0x01 = "FIN"

# window

# chksum
TCP/UDP	En-tête + données	Vérification complète de bout en bout

# urgptr
Urgent Pointer

# options
```

## SHOW() vs SHOW2()

```
show()  Au moment où vous construisez le paquet (valeurs "brutes" que vous avez mises)
show2() Après que Scapy a calculé tous les champs automatiques (checksums, longueurs, etc.)
```

## ANS & UNANS

```
ans,unans=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=sys.argv[1]), timeout=2)
```