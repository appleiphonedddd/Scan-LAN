from scapy.all import ARP, Ether, srp
import webbrowser

def scan():

    IP_range = "192.168.1.0/24"

    # IP Address for the destination
    # create ARP package

    arp = ARP(pdst=IP_range)

    # create the Ether broadcast packet
    # ff:ff:ff:ff:ff:ff MAC address indicates broadcasting

    ether = Ether(dst ="ff:ff:ff:ff:ff:ff")

    # stack them

    packet = ether/arp

    result = srp(packet, timeout=3, verbose=0)[0]

    # a list of clients, we will fill this in the upcoming loop

    clients = []

    for sent,received in result:

    # for each response, append ip and mac address to "clients" list

        clients.append({"ip":received.psrc, "mac":received.hwsrc})

    print("Available devices in the network:")
    print("IP" + " "*18+"MAC")
    
    for clients in clients:
        print("{:16}     {}".format(clients["ip"], clients["mac"]))

def website():
    webbrowser.open("UI.html")

if __name__ == "__main__":
    website()