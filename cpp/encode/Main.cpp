//Hamming encoding of bitstring
//copyright Frank Boerman 2014
//Main.cpp file

#include "Main.h"

using namespace std;


int main(int argc, char* argv[])//arguments: .exe path/symbol/minimum length of databitstring
{
	//check the inputarguments
	if (argc < 3)
	{
		cout << "Not enough inputarguments" << endl;
		return -1;
	}
	
	//save the inputarguments
	LENGTH = atoi(argv[2]);
	DATABITSTRING = DecToBin(atoi(argv[1]));

	//append to LENGHTH bits length
	int orilen = DATABITSTRING.length();
	for (int i = 0; i < (LENGTH - orilen); i++)
	{
		DATABITSTRING = "0" + DATABITSTRING;
	}
	
	cout << "Encoding bitstring " << DATABITSTRING << endl;

	//add the parity bits by slicing the string, by iterative trying to fit it in
	int i = 0;
	int j;
	while (true)
	{
		j = (int)pow(2, i);
		if (j > DATABITSTRING.length())
		{
			break;
		}
		DATABITSTRING.insert(j - 1, "x");
		i++;
	}
	//find number of parity bits
	PARITYNUM = count(DATABITSTRING.begin(), DATABITSTRING.end(), 'x');

	cout << "Adding " << PARITYNUM << " parity bits" << endl;

	//iterate through the bitstring and create the parity string, calculate parity, and put it in resultstring
	string RESULT = DATABITSTRING;

	string paritystring;

	for (int i = 0; i < PARITYNUM; i++)
	{
		j = pow(2, i);
		//create the parts
		paritystring = "";

		int reli = 0;//holds index relative to the startposition
		//chop the string in parts of size of parityindex and take all th even parts
		//put these parts in the paritystring
		for (int z = j - 1; z < DATABITSTRING.length(); z += j)
		{
			if ((reli % 2) == 0)
			{
				paritystring = paritystring + DATABITSTRING.substr(z, j);
			}
			reli++;
		}
		//compute the paritybit and put it in the result string
		int parity = count(paritystring.begin(), paritystring.end(), '1') % 2;
		RESULT[j - 1] = (char)(((int)'0') + parity);

	}

	cout << "Resulting encoded bitstring " << RESULT << endl;
	return 0;
}