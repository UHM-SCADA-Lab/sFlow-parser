#Set parse IPv4 header
import datashift
import ipaddress

def ipv4(data, i):
    version = 0
    length = 0
    source_address = destination_address =[0]*4
    protocol = 0
    i0 = i

    version = data[i] & 240 >> 4
    length = (data[i] & 15)*4
    for i in range (i0+length):
        if(i == i0+9):
            protocol = data[i]
            if(protocol == 17):
                print('Protocol: UDP (17)')
            elif(protocol == 6):
                print('Protocol: TCP (6)')
            else:
                print('Protocol: Unkown (', protocol,')')
        if(i == i0+12):
            source_address = datashift.datashift(data, i, 4)
            source_address = ipaddress.IPv4Address(source_address)
            print('Source Address:', source_address)
        if(i == i0+16):
            source_address = datashift.datashift(data, i, 4)
            source_address = ipaddress.IPv4Address(source_address)
            print('Source Address:', source_address)
    return length


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
ipv4(data, 0)
