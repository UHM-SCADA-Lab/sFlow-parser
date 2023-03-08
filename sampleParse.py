import datashift
import arp
import udp
import tcp
import ipv4
import ipv6
from ethernetII import ethernetIIParser as ethIIParser
import icmpv6
import headerprotocol
import decimalToHex

#Parse the samples
#We do not need counter samples data
#Printing/storing the flow sample data
def sampleParser(data, i, sample_type):
    sample_length = datashift.datashift(data, i + 4, 4)
    x = 0
    i += 8
    seq_num = sampling_rate = sample_pool = dropped_packets = input_interface = output_interface = flow_record = [0] * 4
    src_idClass = 0
    index = [0] * 3
    if(sample_type == 1):
        print('Flow sample (', sample_type,'):')
        next_type = 0
        for x in range(sample_length):
            if(x == 0):
                #print('I = ', i)
                print('\tSample length: ', sample_length)
                seq_num = datashift.datashift(data, i, len(seq_num))
                print('\tSequence Number: ', seq_num)
            if(x == 4):
                src_idClass = datashift.datashift(data, i + x, 1)
                index = datashift.datashift(data, i + x + 1, 3)
                print('\tSource ID class: ', src_idClass)
                print('\tIndex: ', index)
            if(x == 8):
                sampling_rate = datashift.datashift(data, i + x, len(sampling_rate))
                print('\tSampling rate: 1 out of ', sampling_rate, ' packets')
            if(x == 12):
                sample_pool = datashift.datashift(data, i + x, len(sample_pool))
                print('\tSample pool: ', sample_pool, ' total packets')
            if(x == 16):
                dropped_packets = datashift.datashift(data, i + x, len(dropped_packets))
                print('\tDropped packets: ', dropped_packets)
            if(x == 20):
                input_interface = datashift.datashift(data, i + x, len(input_interface))
                print('\tInput interface (ifIndex): ', input_interface)
            if(x == 24):
                output_interface = datashift.datashift(data, i + x, 4) 
                print('\tOutput interface: ', output_interface)
            if(x == 40):
                next_type = datashift.datashift(data, i + x, 4)
                if(next_type == 1):
                    print('\tHeader Protocol: Ethernet (1)')
                else:
                    print('\tHeader Protocol: Unkown')
            if(x == 56):
                print('\t\tEthernetII Header: ')
                ethernetII = ethIIParser(data, i+x)
                print('\t\t\tDestination: ', ethernetII.destination)
                print('\t\t\tSource: ', ethernetII.source)
                print('\t\t\tType: ',ethernetII.type)
            if(ethernetII.type == hex(2048)):
                print('\t\tIPv4 Header: ')
                ipv4 = ipv4.ipv4(data, i+70)
                print('\t\t\t
    elif(sample_type == 2):
        print('Counters sample (', sample_type,')')
    else: 
        print('Unknown sample (', sample_type,')')


    #print('I before adding length: ', i)
    i += (sample_length)
    #print('I after adding length: ', i)
    return i;
#We need to have our code look through each packet and find the piece of information that says what type of packet comes next.
