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

# Install scapy
pip install scapy

# Create requirements.txt
touch requirements.txt

# add scapy into requirements.txt
pip freeze > requirements.txt

# Update all versions
pip install -r requirements.txt

# Selective update
pip install --upgrade scapy

# Or update to the latest compatible versions
pip install --upgrade -r requirements.txt

# Enter into the lab folder
cd lab

# Run
python3 any_file.py
```

## Links

- [⚡ analysis-data-lab](#-analysis-data-lab)
  - [Installation](#installation)
  - [Links](#links)
  - [ICMP-Lab](#icmp-lab)
  - [tcpdump CMD](#tcpdump-cmd)
  - [Calculate](#calculate)
  - [IP fields](#ip-fields)
  - [TCP fields](#tcp-fields)
  - [Summary of IP and TCP](#summary-of-ip-and-tcp)
  - [ARP](#arp)
  - [SHOW vs SHOW2](#show-vs-show2)
  - [sr sr1 srp srp1 send sendp](#sr-sr1-srp-srp1-send-sendp)

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

[:arrow_up: Up](#links)

---

## Calculate

```
0000  45 00 00 28 00 01 00 00 40 06 7C CD 7F 00 00 01 7F 00 00 01

Position 0-1 : 45 00
Position 2-3 : 00 28
Position 4-5 : 00 01
Position 6-7 : 00 00
Position 8-9 : 40 06
Position 10-11: 7C CD
Position 12-15: 7F 00 00 01
Position 16-19: 7F 00 00 01
Position 20... : data (TCP)

Adresse relative 0 : [45 00 00 28]  ← Mot 0
Adresse relative 4 : [00 01 00 00]  ← Mot 1
Adresse relative 8 : [40 06 7C CD]  ← Mot 2
Adresse relative 12: [7F 00 00 01]  ← Mot 3
Adresse relative 16: [7F 00 00 01]  ← Mot 4
TCP...

Corresponding with HEADER of IP

# Mot 0 (0x1000-0x1003) : 45 00 00 28
0x45 = premier octet (version + IHL)
0x00 = TOS
0x00 0x28 = Total Length (40 octets)

# Mot 1 (0x1004-0x1007) : 00 01 00 00
0x00 0x01 = Identification (1)
0x00 0x00 = Flags + Fragment Offset

# Mot 2 (0x1008-0x100B) : 40 06 7C CD
0x40 = TTL (64)
0x06 = Protocol (TCP)
0x7C 0xCD = Header Checksum

# Mot 3 (0x100C-0x100F) : 7F 00 00 01
7F 00 00 01 = Source IP (127.0.0.1)

# Mot 4 (0x1010-0x1013) : 7F 00 00 01
7F 00 00 01 = Destination IP (127.0.0.1)

Octets      Valeur hexa                 Champ                       Description
-------------------------------------------------------------------------------------------------------
0               0x45                Version + IHL               Version=4, IHL=5 (20 octets)
1               0x00                TOS/DSCP+ECN                Type of Service = 0
2-3             0x00 0x28           Total Length                40 octets (0x0028 = 40)
4-5             0x00 0x01           Identification	            0x0001 = 1
6-7             0x00 0x00           Flags + Fragment Offset	    Pas de fragmentation
8               0x40                TTL	64                      (0x40 = 64)
9               0x06                Protocol                    6 = TCP
10-11           0x7C 0xCD           Header Checksum             0x7CCD (valide)
12-15           0x7F 0x00 0x00 0x01	Source IP                   127.0.0.1 (localhost)
16-19           0x7F 0x00 0x00 0x01	Destination IP              127.0.0.1 (localhost)
20-23           0x00 0x00 0x00 0x00	Début données TCP           (À analyser)

16	Hexadécimal	0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F (16 chiffres)	0x42
2	Binaire	0,1 (2 chiffres)	101010
hexadécimal = 16

16 (hexadécimal) => 0x10 + 1x16 = 16

0x40 = 64
0x40 => (4x16) + (0x16) = 64 octets

0x28 = 40
0x28 = (2 x 16) + 8 = 40 octets

0x45 = ??
ihl => 0x45 = (4x16) + 5 = 69 octets ❌ False

Version = 0x04
ihl = 0x05
4 octets x 5 mots = 20 octets ✅

:warning: 1 mots = 32 bits = 4 octets :warning:

ihl = 4 octets x 5 mots = 20 octets
32 bits x 5 mots = 160 bits

Octet complet : 0x45 = 0b01000101
                └─┘ └─┘
                4   5
                │   └── IHL = 5
                └────── Version = 4

Champs obligatoires (20 octets) :
┌─────────────────────────────────────────────────────────────┐
│ - Version + IHL (1 octet)                                   │
│ - TOS (1 octet)                                             │
│ - Total Length (2 octets)                                   │
│ - Identification (2 octets)                                 │
│ - Flags + Fragment Offset (2 octets)                        │
│ - TTL (1 octet)                                             │
│ - Protocol (1 octet)                                        │
│ - Header Checksum (2 octets)                                │
│ - Source IP (4 octets)                                      │
│ - Destination IP (4 octets)                                 │
├─────────────────────────────────────────────────────────────┤
│ Total = 20 octets = 5 mots de 4 octets                      │
└─────────────────────────────────────────────────────────────┘
```

[:arrow_up: Up](#links)

---

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
IHL = 5 → 5 mots × 4 octets/mot = 20 octets

(look at file fields-overview.py)
Minimale value : 5 (5 mots × 4 octets = 20 octets)    <= without options
Maximale value : 15 (15 mots × 4 octets = 60 octets)  <= with all options

---

:anger: ihl = 5 mots of 4 octets or 32 bits => 20 octets or 160 bits

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


# len (Total Length)
16 bits (0-65535) but minimum 20 octets

! Force it manually (not recommended) !

Knowing where the package ends

len > MTU (Maximum Transmission Unit)

pkt = IP(len=10)  # Impossible (minimum 20 octets)


# id (Identification)
16 bits (0 to 65535)

The “Identification” field (ID) is used to group fragments from the same packet. When a packet is fragmented, all of its fragments are assigned the same identification number.

- Security issues => Idle scan, ID prediction, fragmentation attacks


# frag (Fragment Offset)
13 bits 
8 octets x 8 = 64 bits

Reconstruct the original order of the fragments = ID (same ID for all fragments) + MF (flag)

Fragment Offset is a key field for IP fragmentation, a mechanism that allows a packet that is too large to pass through a network to be split into smaller pieces.
This is a 13-bit field that indicates where this fragment is located within the original packet, measured in 8-byte (64-bit) blocks.

Identifies all fragments of the same packet.
You have a 4,000 octets packet to send, but the next router can only accept 1,500 octets packets (MTU = Maximum Transmission Unit).

...
Fragment Offset: 185 (1480 ÷ 8 = 185)
...

Blocks of 8 octets => Offset max: 8191 => Position max: 65528 octets (8191 × 8)


# ttl (time to live)
8 bits (0-255)

Hops => 64 (Linux/macOS), 128 (Windows), 255 (routeurs)

- ping -c 3 8.8.8.8
ttl=117 => 128-117 = 11 hops (routers)
(255-117 = 138 hops is not possible, max 128 or 64 routers)

- traceroute 8.8.8.8
traceroute to 8.8.8.8 (8.8.8.8), 64 hops max, 40 byte packets
 1  localregion (x.x.x.x)  6.322 ms  4.278 ms  4.220 ms
 2  cybl-ch-zrh-pln-001.cyberlink.ch (212.55.222.27)  12.204 ms  12.610 ms  12.237 ms
 3  cybl-ch-zrh-pcr-002.cyberlink.ch (213.158.128.158)  13.197 ms  13.132 ms  12.579 ms
 4  cybl-ch-gtg-pbr-001.cyberlink.ch (213.158.128.138)  14.155 ms  16.632 ms  13.969 ms
 5  swissix.google.com (91.206.52.74)  13.876 ms  13.008 ms
    cybl-ch-gtg-pbr-001.cyberlink.ch (213.158.128.138)  13.650 ms
 6  * * swissix.google.com (91.206.52.74)  15.580 ms
 7  * * *
 8  dns.google (8.8.8.8)  25.399 ms  14.157 ms  13.531 ms

Your PC → Google : 8 hops (traceroute)
Google → Your PC : 11 hops (ping)

Routers take different paths on the outbound and return legs. This is very common on the Internet.

255 remains the maximum possible value (since it is 8 bits), but it is rarely used on the public Internet.


# proto (Protocol)
8 bits

The protocol field indicates which higher-level protocol is contained in the IP packet data:
ICMP, TCP, UDP, ... (encapsulated protocol)

Number (decimal)    Number (hexa)   Protocol        Usage
--------------------------------------------------------------------------------------
1                   0x01            ICMP            Ping, traceroute, erreurs réseau
6                   0x06            TCP             Web (HTTP/HTTPS), Email, SSH, FTP
17                  0x11            UDP	DNS,        streaming, VoIP, gaming
2                   0x02            IGMP            Gestion des groupes multicast
47                  0x2F            GRE             Tunnels VPN (PPTP)
50                  0x32            ESP             IPSec (chiffrement)
51                  0x33            AH              IPSec (authentification)
80                                                  HTTP
443                                                 HTTPS
89                  0x59            OSPF            Routage interne
132                 0x84            SCTP            Téléphonie (alternative à TCP)

- Proto=6  (TCP) + port 80  → HTTP
- Proto=6  (TCP) + port 443 → HTTPS
- Proto=17 (UDP) + port 53  → DNS

# flags
1 bit
[Bit 0 (Reserved)] [Bit 1 (DF)] [Bit 2 (MF)]

# 0x40 = 64 in decimal = bit DF
0x40 = "DF" => flags=0x40 or flags="DF"


# chksum
If the header is corrupted, we don't know where to deliver the package!


# options
IP options are becoming obsolete because:

1. They are ineffective
2. They are dangerous (source routing)
3. They are not supported by NAT
4. IPv6 takes a different approach

:warning: If you see IHL > 5, be cautious: it’s either a very specific case or it’s potentially suspicious! :warning:
```

[:arrow_up: Up](#links)

---

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

Hexa	Binaire     Flags	      Nom commun
----------------------------------------
0x00	00000000	  (aucun)	-
0x01	00000001	  FIN         F
0x02	00000010	  SYN         S
0x04	00000100	  RST         R
0x08	00001000	  PSH         P
0x10	00010000	  ACK         A
0x20	00100000	  URG         U
0x12	00010010	  SYN+ACK	    SA (ou S/A)
0x14	00010100	  RST+ACK     RA
0x18	00011000	  PSH+ACK     PA
0x11	00010001	  FIN+ACK     FA
0x13	00010011	  FIN+SYN+ACK	(rare)
0x03	00000011	  FIN+SYN	    (très rare)
0x30	00110000	  URG+ACK	    UA
0x39	00111001	  URG+PSH+FIN	(rare)

# window

# chksum
Header + data => Comprehensive end-to-end verification

# urgptr
Urgent Pointer

# options
```

[:arrow_up: Up](#links)

---

## Summary of IP and TCP

```
Summary

Total length (len): 1500
HEADER IP: 20 octets
Data IP (TCP + HTTP): 1480 octets
  - HEADER TCP: 20 octets
  - Data HTTP: 1460 octets

┌─────────────────────────────────────────────────────────────────────┐
│                        PAQUET IP (1500 octets)                      │
├─────────────────────────────────────────────────────────────────────┤
│ ┌─────────────────────────────────────────────────────────────────┐ │
│ │                 HEADER IP (20 octets)                          │ │
│ │  proto=6 (TCP)                                                  │ │
│ └─────────────────────────────────────────────────────────────────┘ │
│ ┌─────────────────────────────────────────────────────────────────┐ │
│ │               DATA IP = SEGMENT TCP (1480 octets)            │ │
│ │ ┌─────────────────────────────────────────────────────────────┐ │ │
│ │ │         HEADER TCP (20-60 octets)                         │ │ │
│ │ │  sport=12345, dport=80, flags, seq, ack, etc.              │ │ │
│ │ └─────────────────────────────────────────────────────────────┘ │ │
│ │ ┌─────────────────────────────────────────────────────────────┐ │ │
│ │ │         DATA TCP = MESSAGE HTTP (1460 octets)           │ │ │
│ │ │  "GET / HTTP/1.0\r\n\r\n"                                  │ │ │
│ │ └─────────────────────────────────────────────────────────────┘ │ │
│ └─────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
```


[:arrow_up: Up](#links)

## ARP

```
ARP(
    hwtype=1,           # Hardware type (1 = Ethernet)
    ptype=0x0800,       # Protocol type (0x0800 = IPv4)
    hwlen=6,            # Hardware address length (6 octets pour MAC)
    plen=4,             # Protocol address length (4 octets pour IPv4)
    op=1,               # Opération (1 = who-has/request, 2 = is-at/reply)
    hwsrc=MAC_source,   # Adresse MAC source
    psrc=IP_source,     # Adresse IP source
    hwdst=MAC_dest,     # Adresse MAC destination
    pdst=IP_dest        # Adresse IP destination
)
```

ARP Fields

```
Champ   Type    Description                 Valeurs typiques
-------------------------------------------------------------------------------------------------------
hwtype  int	    Type de matériel            1 = Ethernet, 6 = IEEE 802, 15 = Frame Relay
ptype   int	    Type de protocole           0x0800 = IPv4, 0x0806 = ARP, 0x86DD = IPv6
hwlen   int	    Longueur adresse hardware   6 (pour Ethernet MAC)
plen    int	    Longueur adresse protocole  4 (pour IPv4)
op      int	    Opération ARP               1 = requête, 2 = réponse, 3 = RARP request, 4 = RARP reply
hwsrc   str     MAC source                  "aa:bb:cc:dd:ee:ff"
psrc    str     IP source                   "192.168.1.10"
hwdst   str     MAC destination             "ff:ff:ff:ff:ff:ff" (broadcast pour requête)
pdst    str     IP destination              "192.168.1.1"
```


[:arrow_up: Up](#links)

## SHOW vs SHOW2

```
pkt.show()  Au moment où vous construisez le paquet (valeurs "brutes" que vous avez mises)

pktshow2() Après que Scapy a calculé tous les champs automatiques (checksums, longueurs, etc.)

pkt.summary()
```

## sr sr1 srp srp1 send sendp

```
ans, unans = srp(Ether()/IP()/TCP())

reponse = srp1(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="192.168.18.1"), timeout=2)

if reponse:
    print(f"MAC de 192.168.18.1 : {reponse[ARP].hwsrc}")

sendp(Ether()/ARP())

ans,unans = sr(IP()/TCP())

pkt = sr1(IP()/TCP())

send(IP(dst="192.168.18.22")/TCP(dport=80, flags="R"))
```

[:arrow_up: Up](#links)