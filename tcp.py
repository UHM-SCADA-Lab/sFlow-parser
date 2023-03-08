##########################################################
################### Parse TCP Packet Headers #############


import datashift
import decimalToHex

class TCP:
    def __init__(self):
        self.source_port = 0
        self.destination_port = 0
        self.length = 0

def tcp(data, i):
    tcp = TCP()

    tcp.length = 20
    tcp.source_port = datashift.datashift(data, i, 2)
    tcp.destination_port = datashift.datashift(data, i+2, 2)
    print('Source Port: ', tcp.source_port)
    print('Destination Port: ', tcp.destination_port)

    return tcp

#Test
data = [0]*20
data[0] = 25
data[1] = 233
data[2] = 220
data[3] = 179
data[4] = 0
data[5] = 0
data[6] = 0
data[7] = 0
data[8] = 114
data[9] = 174
data[10] = 203
data[11] = 28
data[12] = 80
data[13] = 20
data[14] = 0
data[15] = 0
data[16] = 183
data[17] = 98
data[18] = 0
data[19] = 0

tcp = tcp(data, 0)
#print(tcp.length)
#print(tcp.source_port)
#print(tcp.destination_port)
