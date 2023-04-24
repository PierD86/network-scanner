from scapy.all import ARP, Ether, srp
import sys
import argparse
import socket
import sys

def take_inputs():
    for line in sys.stdin:
        return line.split()

if __name__ == "__main__":
    #args = find_args()
    #target_ip = vars(args)['target']
    print("enter the target IP address in the form 192.168.1.1/24")
    target_ip = take_inputs()
    target_ip = str(target_ip[0])


    print('\n------------------------------------------------')
    print(f'scanning the following target IP: {target_ip}')
    print('------------------------------------------------\n')

    # IP Address for the destination
    # create ARP packet
    arp = ARP(pdst=target_ip)
    # create the Ether broadcast packet
    # ff:ff:ff:ff:ff:ff MAC address indicates broadcasting
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    # stack them
    packet = ether/arp

    result = srp(packet, timeout=3, verbose=0)[0]

    # a list of clients, we will fill this in the upcoming loop
    clients = []

    for sent, received in result:
        # for each response, append ip and mac address to `clients` list
        try:
            clients.append({'ip': received.psrc,
                            'mac': received.hwsrc,
                            'hostname': socket.gethostbyaddr(received.psrc)[0]})
        except:
            clients.append({'ip': received.psrc,
                            'mac': received.hwsrc,
                            'hostname': ''})

    # print clients
    print("Available devices in the network:")
    print("IP" + " "*20+"MAC" + " "*18+"HOSTNAME")
    for client in clients:
        try:
            print("{:16} {}     {}".format(client['ip'], client['mac'], client['hostname']))
        except:
            print("{:16}  {}".format(client['ip'], client['mac']))

    input("\nPress ENTER to exit")