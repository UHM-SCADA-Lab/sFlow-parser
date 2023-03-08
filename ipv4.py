#Set parse IPv4 header
import datashift
import ipaddress
class IPv4:
    def __init__(self):
        self.version = 0
        self.length = 0
        self.source_address = '0.0.0.0'
        self.destination_address = '0.0.0.0'
        self.protocol = 0

def ipv4(data, i):
    version = 0
    length = 0
    source_address = destination_address =[0]*4
    protocol = 0
    i0 = i
    Ipv4 = IPv4()
    version = data[i] & 240 >> 4
    length = (data[i] & 15)*4
    
    #IPv4 object for returning
    Ipv4 = IPv4()
    Ipv4.version = version
    Ipv4.length = length

    for i in range (i0+length):
        if(i == i0+9):
            protocol = data[i]
            Ipv4.protocol = data[i]
            if(protocol == 17):
                print('Protocol: UDP (17)')
            elif(protocol == 6):
                print('Protocol: TCP (6)')
            else:
                print('Protocol: Unkown (', protocol,')')
        if(i == i0+12):
            source_address = datashift.datashift(data, i, 4)
            source_address = ipaddress.IPv4Address(source_address)
            Ipv4.source_address = source_address
            print('Source Address:', source_address)
        if(i == i0+16):
            destination_address = datashift.datashift(data, i, 4)
            destination_address = ipaddress.IPv4Address(destination_address)
            Ipv4.destination_address = destination_address
            print('Destination Address: ', destination_address)

    return Ipv4


data = [0] * 20
data[0] = 69
data[1] = 0
data[2] = 0
data[3] = 73
data[4] = 140
data[5] = 109
data[6] = 64
data[7] = 0
data[8] = 255
data[9] = 17
data[10] = 2
data[11] = 152 
data[12] = 10
data[13] = 1
data[14] = 1
data[15] = 162
data[16] = 224
data[17] = 0
data[18] = 0
data[19] = 251
test = ipv4(data, 0)
#print(test.version)
#print(test.length)
#print(test.protocol)
#print(test.source_address)
#print(test.destination_address)
