//converts decimal to binary and vice versa as described here:
//http://stackoverflow.com/questions/2548282/decimal-to-binary-and-vice-versa
//cpp file

#include "BinConversion.h"

using namespace std;

string DecToBin(int number)
{
	if (number == 0) return "0";
	if (number == 1) return "1";

	if (number % 2 == 0)
		return DecToBin(number / 2) + "0";
	else
		return DecToBin(number / 2) + "1";
}

int BinToDec(string number)
{
	int result = 0, pow = 1;
	for (int i = number.length() - 1; i >= 0; --i, pow <<= 1)
		result += (number[i] - '0') * pow;

	return result;
}
