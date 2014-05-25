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
    parser.add_argument('--symbol', nargs='?', const=1, type=int, default=77, help='integer of symbol that has to be encoded')
    parser.add_argument('--length', nargs='?', const=1, type=int, default=8, help='minimum length of databits')


    #parse the input arguments
    SYMBOL = parser.parse_args().symbol
    LENGTH = parser.parse_args().length

    # #clip the value of the symbol
    # if SYMBOL > 127:
    #     SYMBOL = 127
    # elif SYMBOL < 0:
    #     SYMBOL = 0

    #we always do 4 parity bits because we have a byte word (8 bits can store all the symbols, actually 7 is already correct, but the assignment
        #specified 8)
    #so result is always 12 bits long

    #build the result string
    #the original bits
    bsymbol = BitString(SYMBOL)
    #append to 8 bits length
    for i in range(0,LENGTH-FindBits(SYMBOL)):
        bsymbol = '0' + bsymbol

    # bsymbol = 'xx' + bsymbol[:1] + 'x' + bsymbol[1:4] + 'x' + bsymbol[4:]

    bsymbol = list(bsymbol)
    #add the parity bits by slicing the string, by iterative trying to fit it in
    i = 0
    while 1:
        j = pow(2,i)
        if j > len(bsymbol):
            break
        bsymbol.insert(j-1,'x')
        i += 1

    bsymbol = "".join(bsymbol)
    #count number of parities
    PARITYNUM = bsymbol.count('x')

    #calculate the parity bits
    #dictionary to store parity strings
    parities = {}
    for i in range(0,PARITYNUM):
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
    for i in range(0,PARITYNUM):
        j = pow(2,i)
        #because strings are immutable, temporary convert it to a list
        #than assign the parity bit at the parity position
        bsymbol = list(bsymbol)
        bsymbol[j-1] = str(parities[j].count('1') % 2)
        bsymbol = "".join(bsymbol)#convert back to string

    #and finally print the result!
    print(bsymbol)