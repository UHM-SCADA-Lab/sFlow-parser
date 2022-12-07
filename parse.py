import socket
import hexdump
import os
import time
import sampleParse
import datashift
import ms2time
import ipaddress

#Establish connection to IP address 10.1.1.6
UDP_IP = "10.1.1.6"
UDP_PORT = 6343
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Declare variables
version = address_type = address = sub_agent = seq_number = sysuptime = numsamples = sample_type = [0]*4
samples = 0

#Parse the entire data packet and print it out 
sock.bind(("", UDP_PORT))
while True: 
    data, addr = sock.recvfrom(2048)
    print ("received message length:", len(data)-16)
    hexdump.hexdump(data)
    for i in range(len(data)):
        if i == 0:
            version1 = datashift.datashift(data, i, len(version))
            print('Datagram Version: ', version1)
        if i == 4: 
            address_type1 = datashift.datashift(data, i, len(address_type))
            print('Agent Address Type: ', address_type1)
        if i == 8: 
            address = datashift.datashift(data, i, 4)
            address = ipaddress.IPv4Address(address)
            print('Agent Address:', address)
        if i == 12:
            sub_agent1 = datashift.datashift(data, i, len(sub_agent))
            print('Sub-Agent ID: ', sub_agent1)
        if i == 16:
            seq_number1 = datashift.datashift(data, i, len(seq_number))
            print('Sequence Number: ', seq_number1)
        if i == 20:
            sysuptime1 = datashift.datashift(data, i, len(sysuptime))
            (d, h, m, s) = ms2time.ms2time(sysuptime1)
            print('SysUptime: ', sysuptime1, 'ms', '(', d, 'days', h, 'hours', m, 'minutes', s, 'seconds', ')')
            print('Data len: ', len(data)-16)
        if i == 24:
            numsamples1 = datashift.datashift(data, i, len(numsamples))
            print('NumSamples: ', numsamples1)
            samples = numsamples1
        if i >= 28 and i < len(data):
            while (samples > 0):
                #print('i: ', i)
                sample_type1 = datashift.datashift(data, i, len(sample_type))
                i = sampleParse.sampleParser(data, i, sample_type1)
                #print('I after sample: ', i)
                samples -= 1
        #Insert more if statements for different data samples
    #Reset i, wait for 0.5 seconds and then clear the screen
    i = 0
    time.sleep(2)
    os.system('clear')
