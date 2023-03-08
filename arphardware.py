#Function replaces a number with the arp hardware type 

def hardwaretype(num):
    if isinstance(num, int) == True:
        if num == 0:
            hardwaretype = 'Reserved'
        elif num == 1:
            hardwaretype = 'Ethernet'
        elif num == 2:
            hardwaretype = 'Experimental Ethernet'
        elif num == 3: 
            hardwaretype = 'Amateur Radio AX.25'
        elif num == 4:
            hardwaretype = 'Proteon ProNET Token Ring'
        elif num == 5:
            hardwaretype = 'Chaos'
        elif num == 6:
            hardwaretype = 'IEEE 802 Networks'
        elif num == 7:
            hardwaretype = 'ARCNET'
        elif num == 8:
            hardwaretype = 'Hyperchannel'
        elif num == 9:
            hardwaretype = 'Lanstar'
        elif num == 10:
            hardwaretype = 'Autonet Short Address'
        elif num == 11:
            hardwaretype = 'LocalTalk'
        elif num == 12:
            hardwaretype = 'LocalNet'
        elif num == 13:
            hardwaretype = 'Ultra link'
        elif num == 14:
            hardwaretype = 'SMDS'
        elif num == 15:
            hardwaretype = 'Frame Relay'
        elif num == 16:
            hardwaretype = 'Asynchronous Transmission Mode (ATM)'
        elif num == 17: 
            hardwaretype = 'HDLC'
        elif num == 18:
            hardwaretype = 'Fibre Channel'
        elif num == 19: 
            hardwaretype = 'Asynchronous Transmission Mode (ATM)'
        elif num == 20:
            hardwaretype = 'Serial Line'
        elif num == 21: 
            hardwaretype = 'Asynchronous Transmission Mode (ATM)'
        elif num == 22:
            hardwaretype = 'MIL-STD-188-220'
        elif num == 23:
            hardwaretype = 'Metricom'
        elif num == 24:
            hardwaretype = 'IEEE 1394.1995'
        elif num == 25:
            hardwaretype = 'MAPOS'
        elif num == 26:
            hardwaretype = 'Twinaxial' 
        elif num == 27:
            hardwaretype = 'EUI-64'
        elif num == 28:
            hardwaretype = 'HIPARP'
        elif num == 29:
            hardwaretype = 'IP and ARP over ISO 7816-3'
        elif num == 30:
            hardwaretype = 'ARPsec'
        elif num == 31:
            hardwaretype = 'IPsec tunnel'
        elif num == 32: 
            hardwaretype = 'InfiniBand(TM)'
        elif num == 33: 
            hardwaretype = 'TIA-102 Project 25 Common Air Interface (CAI)'
        elif num == 34:
            hardwaretype = 'Wiegand Interface'
        elif num == 35: 
            hardwaretype = 'Pure IP'
        elif num == 36: 
            hardwaretype = 'HW_EXP1'
        elif num == 37:
            hardwaretype = 'HFI'
        elif num == 38:
            hardwaretype = 'Unified Bus (UB)'
        elif 39 <= num <= 255:
            hardwaretype = 'Unassigned'
        elif num == 256:
            hardwaretype = 'HW_EXP2'
        elif num == 257: 
            hardwaretype = 'AEthernet'
        elif 258 <= num <= 65534:
            hardwaretype = 'Unassigned'
        elif num == 65535:
            hardwaretype = 'Reserved'
        return hardwaretype   
    else:
        print('Error: Hardware type number must be an integer value.\n')

