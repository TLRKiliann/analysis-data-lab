#!/usr/bin/env python3

from scapy.layers.http import HTTP_Client, load_layer, http_request

width = 60
http_txt = "HTTP GET Requests"
print(width * "#")
print()
print(http_txt.center(width))
print()
print(width * "#")

print("\nHTTP_Client")

# Create client & send a GET request
client = HTTP_Client()
response = client.request("http://example.com")
print(response)
client.close()

print("\nhttp_request")

load_layer("http")
# Send a GET request to "www.google.com" with the root path "/"
http_request("www.google.com", "/")