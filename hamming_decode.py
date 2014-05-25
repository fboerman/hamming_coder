__author__ = 'williewonka'
#script that decodes a given bit word encoded in hamming code, and corrects any single time errors

#import modules
import argparse
from math import ceil, log2

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

if __name__ == '__main__': #pythons equivalent of main()
    parser = argparse.ArgumentParser(description="script that decodes a given bitstring encoded in hamming code, and corrects any single time errors")
    parser.add_argument('--bitstring', nargs='?', const=1, type=str, default='', help='12-bit hamming encoded bitstring')

    #parse arguments
    BITSTRING = parser.parse_args().bitstring

    #calculate ammount of powers of 2 that are in the ammount of bits, aka find the ammount of parity bits
    #we do this by finding the highest power of 2 that can be fitted in the integer of length of bitstring
    paritynum = ceil(log2(len(BITSTRING)))

    print("Decoding bitstring " + BITSTRING + " with " + str(paritynum) + " paritybits and " + str(len(BITSTRING) - paritynum) + " databits")

    #build the parity strings same way as when encoding
    parities = {}
    for i in range(0,paritynum):
        j = pow(2,i)
        parities[j] = ''
        z = 0
        for c in chunks(BITSTRING[j-1:],j):#start at the number of the parity!
            if z % 2 == 0:
                parities[j] += c
            z += 1

    #check if the parities are even, if so that 0 in the check, if not than add a 1 to the check
    check = ''
    for i in range(0,paritynum):
        j = pow(2,i)
        if parities[j].count('1') % 2 != 0:
            check = '1' + check
        else:
            check = '0' + check

    #now we know where the error is, flip the bit at this position, if its all zero do nothing
    wrongbit = int(check,2) #convert binary to integer
    #if the index is not zero, flip the bit at that index number
    if wrongbit != 0:
        #same as with encoding, convert temporary to a list and than flip the bit
        correctstring = list(BITSTRING)
        if correctstring[wrongbit-1] == '0':
            correctstring[wrongbit-1] = '1'
        else:
            correctstring[wrongbit-1] = '0'
        correctstring = ''.join(correctstring)

        print("Detected and corrected error in bitstring at position " + str(wrongbit))
    else:#no error
        correctstring = BITSTRING
        print("No error detected")

    #now the string is corrected, extract the information from it
    #we do this by throwing away all the parity bits
    #convert the bitstring to list and put empty chars at the positions of the parity bits, this will erase that position when joining again
    databitstring = list(correctstring)
    for i in range(0,paritynum):
        j = pow(2,i)
        databitstring[j-1] = ""
    #join again and convert back to decimal and print it
    databitstring = "".join(databitstring)
    print("Correct databitstring: " + databitstring)
    data = int(databitstring,2)
    print("Symbol in bitstring: " + str(data))