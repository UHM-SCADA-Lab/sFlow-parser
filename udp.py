import datashift
import decimalToHex
# Parse UDP Headers
def udp(data, i):
    source_port = [0] * 2
    dest_port = [0] * 2
    length = [0] * 2
    checksum = [0] * 2
    j = 0
    source_port = datashift.datashift(data, i, 2)
    dest_port = datashift.datashift(data, i + 2, 2)
    length = datashift.datashift(data, i + 4, 2)
    checksum[0] = decimalToHex.decimalToHex(data[i+6])
    checksum[1] = decimalToHex.decimalToHex(data[i+7])
    print('Source Port:', source_port)
    print('Destination Port:', dest_port)
    print('Length:', length)
    print('Checksum:', ''.join(map(str, checksum)), '(Hex)')

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
udp(data, 0)

