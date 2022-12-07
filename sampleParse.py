import datashift

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
        for x in range(sample_length):
            if(x == 0):
                #print('I = ', i)
                print('Sample length: ', sample_length)
                seq_num = datashift.datashift(data, i, len(seq_num))
                print('Sequence Number: ', seq_num)
            if(x == 4):
                src_idClass = datashift.datashift(data, i + x, 1)
                index = datashift.datashift(data, i + x + 1, 3)
                print('Source ID class: ', src_idClass)
                print('Index: ', index)
            if(x == 8):
                sampling_rate = datashift.datashift(data, i + x, len(sampling_rate))
                print('Sampling rate: 1 out of ', sampling_rate, ' packets')
            if(x == 12):
                sample_pool = datashift.datashift(data, i + x, len(sample_pool))
                print('Sample pool: ', sample_pool, ' total packets')
            if(x == 16):
                dropped_packets = datashift.datashift(data, i + x, len(dropped_packets))
                print('Dropped packets: ', dropped_packets)
            if(x == 20):
                input_interface = datashift.datashift(data, i + x, len(input_interface))
                print('Input interface (ifIndex): ', input_interface)
            if(x == 24):
                print('Output interface: ')
    elif(sample_type == 2):
        print('Counters sample (', sample_type,')')
    else: 
        print('Unknown sample (', sample_type,')')


    #print('I before adding length: ', i)
    i += (sample_length)
    #print('I after adding length: ', i)
    return i;

