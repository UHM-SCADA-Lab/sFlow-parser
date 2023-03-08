###############################################################
######### Parse Address Resolution Protocol Headers ###########
###############################################################

#Progress:
    #Still have to write the rest of the code to get sender and targ
    #et ip addresses. I plan on using the imported 'ipaddress'
    #function I used in 'ipv4.py'.
    #Then I will create the print statements for all of the 
    #variables and test it with a set of data from Wireshark.

import datashift
import decimalToHex
import ipaddress
import arphardware

class ARP:
    def __init__(self):
        self.hardware_type = 0
        self.protocol_type = '0x000'
        self.hardware_size = 0
        self.protocol_size = 0
        self.opcode = 0
        self.sender_mac = '00:00:00:00:00:00'
        self.sender_ip = '0.0.0.0'
        self.target_mac = '00:00:00:00:00:00'
        self.target_ip = '0.0.0.0'
        self.length = 0

def arp(data, i):
    arp = ARP()

    arp.length = 28
    arp.hardware_type = datashift.datashift(data,i,2)
    arp.protocol_type = hex(datashift.datashift(data, i+2, 2))
    arp.hardware_size = data[i+4]
    arp.protocol_size = data[i+5]
    arp.opcode = datashift.datashift(data, i+6, 2) 
    arp.sender_ip = datashift.datashift(data, i+14, 4)
    arp.sender_ip = ipaddress.IPv4Address(arp.sender_ip)
    arp.target_ip = datashift.datashift(data, i+24, 4)
    arp.target_ip = ipaddress.IPv4Address(arp.target_ip)
    arp.sender_mac = [0]*6
    arp.target_mac = [0]*6

    j = 0
    k = 0
    l = 0
    while (j < 28):
        if (7 < j < 14):
            arp.sender_mac[k] = decimalToHex.decimalToHex(data[i + j])
            k += 1
        if (17 < j < 24): 
            arp.target_mac[l] = decimalToHex.decimalToHex(data[i + j])
            l += 1
        j += 1
    
    arp.hardware_type = arphardware.hardwaretype(arp.hardware_type)
    arp.sender_mac = ':'.join(map(str, arp.sender_mac))
    arp.target_mac = ':'.join(map(str, arp.target_mac))

    print('Hardware type: ', arp.hardware_type)
    print('Protocol type: ', arp.protocol_type)
    print('Hardware size: ', arp.hardware_size)
    print('Protocol size: ', arp.protocol_size)
    print('Opcode: ', arp.opcode)
    print('Sender MAC address: ', arp.sender_mac)
    print('Sender IP address: ', arp.sender_ip)
    print('Target MAC address: ',arp.target_mac)
    print('Target IP address: ', arp.target_ip)
    
    return arp
    
data = [0]*28
data[0] = 0
data[1] = 1
data[2] = 8
data[3] = 0
data[4] = 6
data[5] = 4
data[6] = 0
data[7] = 1
data[8] = 184
data[9] = 39
data[10] = 235
data[11] = 60
data[12] = 45
data[13] = 96
data[14] = 10
data[15] = 1
data[16] = 44
data[17] = 4
data[18] = 0
data[19] = 0
data[20] = 0
data[21] = 0
data[22] = 0
data[23] = 0
data[24] = 10
data[25] = 1
data[26] = 44
data[27] = 3

#arp = arp(data, 0)
#print(arp.hardware_type)
#print(arp.protocol_type)
#print(arp.hardware_size)
#print(arp.protocol_size)
#print(arp.opcode)
#print(arp.sender_mac)
#print(arp.sender_ip)
#print(arp.target_mac)
#print(arp.target_ip)
#print(arp.length)
