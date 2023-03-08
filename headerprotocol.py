#Function that takes a number and returns the type of the next header

def protocol(x):
    if(x == 1):
        header_type = 'ICMP'
    elif(x == 2048):
        header_type = 'IPv4'
    elif(x == 17):
        header_type = 'UDP'
    elif(x == 2054):
        header_type = 'ARP'
    elif(x == 34535):
        header_type = 'IPv6'
    elif(x == 34667):
        header_type = 'TCP/IP Compression'
    elif(x == 34508): 'LLDP'


#I am now realizing that there is a pretty consistent structure for the header of sampled packets.
#Every packet I've seen so far starts with Ethernet, specifically Ethernet II. Then, it goes to either
#a IPv4 or IPv6 subheader. Then the header ends with either a UDP or TCP subheader.
