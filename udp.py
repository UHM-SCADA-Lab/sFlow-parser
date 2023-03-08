import datashift
import decimalToHex
# Parse UDP Headers

class UDP:
    def __init__(self):
        self.source_port = 0
        self.dest_port = 0
        self.length = 0
        self.checksum = 0

def udp(data, i):
    udp = UDP()
    udp.source_port = [0] * 2
    udp.dest_port = [0] * 2
    udp.length = [0] * 2
    udp.checksum = [0] * 2
    j = 0
    udp.source_port = datashift.datashift(data, i, 2)
    udp.dest_port = datashift.datashift(data, i + 2, 2)
    udp.length = datashift.datashift(data, i + 4, 2)
    udp.checksum[0] = decimalToHex.decimalToHex(data[i+6])
    udp.checksum[1] = decimalToHex.decimalToHex(data[i+7])
    udp.checksum = (''.join(map(str,udp.checksum)), '(Hex)')
    print('Source Port:', udp.source_port)
    print('Destination Port:', udp.dest_port)
    print('Length:', udp.length)
    print('Checksum:', udp.checksum)
    return udp

#Test Case
data = [0] * 8
data[0] = 20
data[1] = 233
data[2] = 20
data[3] = 233
data[4] = 0
data[5] = 45
data[6] = 123
data[7] = 28

x = udp(data,0)
#print(x.source_port)
#print(x.dest_port)
#print(x.length)
#print(x.checksum)
