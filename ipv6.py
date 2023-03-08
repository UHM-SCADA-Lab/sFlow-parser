#Set parse IPv6 header
import datashift
import decimalToHex
import ipaddress

class IPv6:
    def __init__(self):
        self.version = 0
        self.length = 0
        self.protocol = 0
        self.source_address = 0
        self.destination_address = 0 

def ipv6(data, i):
    version = 0
    length = 40
    source_address = [0]*16
    destination_address =[0]*16
    protocol = 0
    i0 = i

    version = data[i] & 240 >> 4

    #IPv6 Object
    Ipv6 = IPv6()
    Ipv6.version = version
    Ipv6.length = length

    print('Version:', version) 
    for i in range (i0+length):
        if i == i0+6:
            protocol = data[i]
            Ipv6.protocol = protocol
            if protocol == 17:
                print('Next Header: UDP (17)')
            elif protocol == 6: 
                print('Next Header: TCP (6)') 
            else:
                print('Protocol: Unkown (', protocol,')')
        #I googled a code to read a decimal number and convert to an ip address
        if i == i0+8:
            source_address = datashift.datashift(data, i, 16)
            source_address = ipaddress.IPv6Address(source_address)
            Ipv6.source_address = source_address
            print('Source Address:', source_address)
        if i == i0+24:
            destination_address = datashift.datashift(data, i, 16)
            destination_address = ipaddress.IPv6Address(destination_address)
            Ipv6.destination_address = destination_address
            print('Destination Address:', destination_address)
    return Ipv6

#Test:
data = [0] * 40
data[0] = 0x60
data[1] = 0x03
data[2] = 0xc5
data[3] = 0x3e
data[4] = 0x01
data[5] = 0xcb
data[6] = 0x11
data[7] = 0xff
data[8] = 0xfe
data[9] = 0x80
data[10] = 0x00
data[11] = 0x00
data[12] = 0x00
data[13] = 0x00
data[14] = 0x00
data[15] = 0x00
data[16] = 0x08
data[17] = 0xbd
data[18] = 0xc5
data[19] = 0xd8
data[20] = 0x7c
data[21] = 0xd1
data[22] = 0xb3
data[23] = 0xcb
data[24] = 0xff
data[25] = 0x02
data[26] = 0x00
data[27] = 0x00
data[28] = 0x00
data[29] = 0x00
data[30] = 0x00
data[31] = 0x00
data[32] = 0x00
data[33] = 0x00
data[34] = 0x00
data[35] = 0x00
data[36] = 0x00
data[37] = 0x00
data[38] = 0x00
data[39] = 0xfb
x = ipv6(data, 0)
#print(x.version)
#print(x.length)
#print(x.protocol)
#print(x.source_address)
#print(x.destination_address)
