import decimalToHex
import datashift


class EthernetII:
    def __init__(self):
        self.destination = 0
        self.source = 0
        self.type = 0

#Used to parse Ethernet II header
def ethernetIIParser(data, i):
    destination =  [0] * 6
    source = [0] * 6
    eth_type = [0] * 2
    eth_type = hex(datashift.datashift(data, i+12, 2))
    j = 0
    k = 0
    l = 0
    while j < 14:
        if(j < 6):
            #print('if: ', data[i+j])
            destination[j] = decimalToHex.decimalToHex(data[i + j])
            #print('destination: ', destination[j])
        elif(j < 12):
            #print('elif: ', data[i+j])
            source[k] = decimalToHex.decimalToHex(data[i+j])
            #print('source: ', source[k])
            k += 1
        else: 
            #print('else: ', data[i+j])
            #eth_type[l] = (decimalToHex.decimalToHex(data[i + j]))
            #print('eth_type: ', eth_type[l])
            l += 1
        j += 1
    #print('Destination: ', ':'.join(map(str, destination)))
    #print('Source: ', ':'.join(map(str, source)))
    #print('Type: ', eth_type)
    #print('Type: ( 0x', ''.join(map(str, eth_type)), ')')
    
    ethII = EthernetII()
    ethII.destination = ':'.join(map(str, destination))
    ethII.source = ':'.join(map(str, source))
    ethII.type = eth_type
    #ethII.type = ''.join(map(str, eth_type))
    return ethII
# Test Case
data = [0] * 14
data[0] = 1
data[1] = 0
data[2] = 94
data[3] = 0
data[4] = 0
data[5] = 251
data[6] = 16
data[7] = 148
data[8] = 187
data[9] = 197
data[10] = 48
data[11] = 58 
data[12] = 8
data[13] = 0
x = ethernetIIParser(data, 0);
#print(x.destination)
#print(x.source)
#print(x.type)
