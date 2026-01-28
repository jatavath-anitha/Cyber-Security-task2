print("Hello, this is my Task 1")
from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

print("Starting network sniffer...")
sniff(prn=packet_callback, count=10)