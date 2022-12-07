#Used for adding bytes of hex data together
def datashift(data, i, length):
    r = 0
    while length > 0:
        r = r | data[i] << (length - 1) * 8 
        length -= 1
        i += 1
    return r


