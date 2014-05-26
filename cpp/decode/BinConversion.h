//converts decimal to binary and vice versa as described here:
//http://stackoverflow.com/questions/2548282/decimal-to-binary-and-vice-versa
//header file

#ifndef BINCONVERSION_H
#define BINCONVERSION_H

#include <string>
//functions
std::string DecToBin(int number);
int BinToDec(std::string number);

#endif