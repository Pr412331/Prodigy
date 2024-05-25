import pyshark

def packetSniff(packet):
    try:
        srcIP = packet.ip.src
        dstIP = packet.ip.dst
        protocols = packet.transport_layer
        print(f"Source IP: {srcIP} ---> Destination IP: {dstIP}, Protocol: {protocols}")
        
        if protocols == 'TCP':
            print("TCP Payload Data: ", packet.tcp.payload)
        elif  protocols == 'UDP':
            print("UDP Payload Data: ", packet.udp.payload)
    except AttributeError:
        pass

def main():
    capture = pyshark.LiveCapture(interface='wlan0', bpf_filter='ip')
    capture.apply_on_packets(packetSniff)

if __name__=="__main__":
    main()