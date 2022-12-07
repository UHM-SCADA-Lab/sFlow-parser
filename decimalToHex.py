#Convert decimals to hex for printing
#Takes one byte of data and returns both hex numbers for that byte
conversion_table = { 0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F' }
def decimalToHex(decimal):
    #print("function", decimal)
    hexadecimal = ''
    if( decimal == 0 and hexadecimal == ''):
        return '00'
    if( decimal == 0 ):
        hexadecimal = hexadecimal + '0'
    while(decimal > 0):
        remainder = decimal % 16
        #print("decimal value:", decimal)
        #print("remainder", remainder)
        if(decimal < 16 and hexadecimal == ''):
            hexadecimal = conversion_table[remainder] + hexadecimal
            hexadecimal = '0' + hexadecimal
        else:
            hexadecimal = conversion_table[remainder] + hexadecimal
        decimal = decimal // 16
    return hexadecimal
