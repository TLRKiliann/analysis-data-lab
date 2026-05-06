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

# ihl

# tos

# flags
[Bit 0 (Reserved)] [Bit 1 (DF)] [Bit 2 (MF)]

# 0x40 = 64 in decimal = bit DF
0x40 = "DF" => flags=0x40 or flags="DF"

# chksum

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

# dataofs

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

# urgptr
Urgent Pointer

# options
```

## SHOW() vs SHOW2()

```
show()	Les champs que vous avez définis	Au moment où vous construisez le paquet (valeurs "brutes" que vous avez mises)
show2()	Les champs tels qu'ils seront réellement envoyés	Après que Scapy a calculé tous les champs automatiques (checksums, longueurs, etc.)
```