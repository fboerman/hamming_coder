__author__ = 'williewonka'
#script that encodes a given symbol using hamming code

#import modules
import argparse
from math import ceil, log2

#function definitions

#Yield successive n-sized chunks from l
def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

#find number of bits needed for a symbol
def FindBits(symbol):
    if symbol == 0:
        return 0
    else:
        return ceil(log2(symbol))

#gives string of bits of given symbol
def BitString(symbol):
    return str(bin(symbol))[2:]

if __name__ == '__main__': #python version of main()
    #define input arguments
    parser = argparse.ArgumentParser(description="encodes byte word of given symbol using hamming code")
    parser.add_argument('--symbol', nargs='?', const=1, type=int, default=12, help='integer of ascii symbol (0-127)')

    #parse the input arguments
    SYMBOL = parser.parse_args().symbol
    #clip the value of the symbol
    if SYMBOL > 127:
        SYMBOL = 127
    elif SYMBOL < 0:
        SYMBOL = 0

    #we always do 4 parity bits because we have a byte word (8 bits can store all the symbols, actually 7 is already correct, but the assignment
        #specified 8)
    #so result is always 12 bits long

    #build the result string
    #the original bits
    bsymbol = BitString(SYMBOL)
    #append to 8 bits length
    for i in range(0,8-FindBits(SYMBOL)):
        bsymbol = '0' + bsymbol
    #add the parity bits by slicing the string
    bsymbol = 'xx' + bsymbol[:1] + 'x' + bsymbol[1:4] + 'x' + bsymbol[4:]

    #calculate the parity bits
    #dictionary to store parity strings
    parities = {}
    for i in range(0,4):
        j = pow(2,i)
        parities[j] = ''
        #first create a string by using the use-skip method described here: https://www.youtube.com/watch?v=TYwrHiQ2-G4
        #create chunks and select all the parts with even index number
        z = 0
        for c in chunks(bsymbol[j-1:],j):#start at the number of the parity!
            if z % 2 == 0:
                parities[j] += c
            z += 1

    #now that we have the paritystrings, finally calculate the parity itself and put it in the result string
    for i in range(0,4):
        j = pow(2,i)
        #because strings are immutable, temporary convert it to a list
        #than assign the parity bit at the parity position
        bsymbol = list(bsymbol)
        bsymbol[j-1] = str(parities[j].count('1') % 2)
        bsymbol = "".join(bsymbol)#convert back to string

    #and finally print the result!
    print(bsymbol)