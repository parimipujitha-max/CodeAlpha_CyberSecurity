from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):

    print("\n========== Packet Captured ==========")

    if packet.haslayer(IP):

        # Source and Destination IP
        print("Source IP:", packet[IP].src)
        print("Destination IP:", packet[IP].dst)

        # Protocol
        if packet.haslayer(TCP):
            print("Protocol: TCP")

        elif packet.haslayer(UDP):
            print("Protocol: UDP")

        else:
            print("Protocol: Other")

        # Packet Summary
        print("Packet Summary:", packet.summary())

print("Starting Packet Sniffer...")

# Capture 10 packets
sniff(prn=packet_callback, count=10)

print("\nSniffing Finished.")