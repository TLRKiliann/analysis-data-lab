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

- [ICMP-Lab](#icmp-lab)
- [tcpdump CMD](#tcpdump-cmd)

## ICMP-Lab

- icmp-lab.py => tcpdump CMD with Scapy

In another terminal, you can use these CMD with tcpdump

```
request:
sudo tcpdump -i en1 -c 1 -v -X 'icmp[icmptype] != icmp-echoreply'

reply:
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
```
