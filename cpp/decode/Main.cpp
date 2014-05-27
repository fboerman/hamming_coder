//Hamming dencoding of bitstring
//copyright Frank Boerman 2014
//Main.cpp file

#include "Main.h"

using namespace std;

int isPowerOfTwo(int x)
{
	return ((x != 0) && ((x & (~x + 1)) == x));
}


int Decode(string BITSTRING)
{

	////check the inputarguments
	//if (argc < 2)
	//{
	//	cout << "Not enough inputarguments" << endl;
	//	return -1;
	//}

	//BITSTRING = argv[1];

	//calculate ammount of powers of 2 that are in the ammount of bits, aka find the ammount of parity bits
	//we do this by finding the highest power of 2 that can be fitted in the integer of length of bitstring
	PARITYNUM = ceil(log2(BITSTRING.length()));

	//cout << "Decoding bitstring " << BITSTRING << " with " << PARITYNUM << " paritybits and " << BITSTRING.length() - PARITYNUM << " databits." << endl;

	//iterate through bitstring and create paritystrings same as with encoding
	//however this time check if the parity is even, if not write a 1 to correcting bitstring
	string WRONGBIT = "", paritystring;
	int j;
	for (int i = 0; i < PARITYNUM; i++)
	{
		j = pow(2, i);
		//create the parts
		paritystring = "";

		int reli = 0;//holds index relative to the startposition
		//chop the string in parts of size of parityindex and take all th even parts
		//put these parts in the paritystring
		for (int z = j - 1; z < BITSTRING.length(); z += j)
		{
			if ((reli % 2) == 0)
			{
				paritystring = paritystring + BITSTRING.substr(z, j);
			}
			reli++;
		}
		//compute the paritybit and put it in the result string
		int parity = count(paritystring.begin(), paritystring.end(), '1') % 2;
		if (parity != 0)
		{
			WRONGBIT = "1" + WRONGBIT;
		}
		else
		{
			WRONGBIT = "0" + WRONGBIT;
		}

	}

	//now we know where the error is, flip the bit at this position, if its all zero do nothing
	int wrongbit = BinToDec(WRONGBIT);

	if (wrongbit != 0)
	{
		//flip the bit with this magic line
		BITSTRING[wrongbit - 1] = (char)(!(int)(BITSTRING[wrongbit - 1] - '0') + '0');

		cout << "Detected and corrected error in bitstring at position " << wrongbit << endl;
	}
	else
	{
		cout << "No error detected" << endl;
	}
	string DATABITSTRING = "";
	//delete all the parity bits to get the databitstring
	//loop through the string, and copy all chars at indexes that are not powers of 2
	for (int i = 0; i < BITSTRING.length(); i++)
	{
		if (!isPowerOfTwo(i+1))
		{
			DATABITSTRING = DATABITSTRING + BITSTRING[i];
		}
	}

	//cout << "Correct databitstring: " << DATABITSTRING << endl;
	//cout << "Symbol in bitstring: " << BinToDec(DATABITSTRING) << endl;

	return BinToDec(DATABITSTRING);
}

int main(int argc, char* argv[]) //input arguments: .exe/inputfile/lenght of bitword
{
	//check and parse inputarguments
	if (argc < 3)
	{
		cout << "Error: invalid input arguments" << endl;
		return -1;
	}

	string inputname = argv[1];
	int LENGTH = atoi(argv[2]);

	//open the file and grab the line with data
	ifstream file;
	string INPUTDATA;
	file.open(inputname);

	if (file.fail())
	{
		cout << "Error reading file " << inputname << endl;
		return -1;
	}

	getline(file, INPUTDATA);
	//open output file
	ofstream resstream("result.txt");
	ofstream datastream("data.txt");

	//iterate through the 8 bits parts and decode it bitword for bitword
	for (int i = 0; i < INPUTDATA.length(); i += 12)
	{
		string bitword = INPUTDATA.substr(i, 12);
		datastream << bitword << endl;
		resstream << (char)Decode(bitword);
	}
	datastream.close();
	resstream.close();
}