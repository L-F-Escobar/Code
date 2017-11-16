/*
 * header.h
 *
 *  Created on: Aug 31, 2015
 *      Author: Luis
 */

#ifndef HEADER_H_
#define HEADER_H_

#include<iostream>
#include<iomanip>
#include<string>

//For Files
#include<fstream>

//For cin fail
#include<limits>
#include<sstream>

//For toupper
#include<stdio.h>
#include<ctype.h>
#include<cstring>

using namespace std;

const int MAIN_PROGRAM = 100;
const int INPUT_CARD   = 15;
const int OUTPUT_CARD  = 15;

//PROTOTYPES BEGIN
/*************************************************************************
* PrintHeader:
* 	This function simply prints my class header directly into an output
* 	file.
*
* RETURNS: my class header
**************************************************************************/
void PrintHeader(ostream &outFile, string asName, string asType);


/*************************************************************************
* UserPick:
* 	This function allows the user to make a choice as to what they want to
* 	input into the simple computer emulator. This function allows the user
* 	to make valid choices. Also allows the user to exit the entire
* 	program.
*
* RETURNS: the choice of the user
**************************************************************************/
void UserPick(int &pick);


/*************************************************************************
* AddInput:
* 	This function allows the user to add values into the input card. This
* 	function allows the user to make only valid inputs into the input
* 	card. It also informs the user when the input card is empty.
*
* RETURNS: a value into the input card
**************************************************************************/
void AddInput(string inputCard[], int &inputCardIndex);


/*************************************************************************
* ClearInputCard:
* 	This function allows the code to completely clear the input card.
*
* RETURNS: a blank input card array
**************************************************************************/
void ClearInputCard(string inputCard[], int &inputCardIndex);


/*************************************************************************
* ClearAll:
* 	This function allows the code to completely clear the input card, the
* 	output card & main memory.
*
* RETURNS: a blank input card, output card & main memory array
**************************************************************************/
void ClearAll(string inputCard[], int &inputCardIndex,
			  string mainProgram[], int &mainProgramIndex,
			  string &accumulator, string &iR, int &programCounter,
			  string outputCard[], int &outputCardIndex);


/*************************************************************************
* ClearMainProgram:
* 	This function allows the code to completely clear main memory.
*
* RETURNS: a blank main memory array
**************************************************************************/
void ClearMainProgram(string mainProgram[], int &mainProgramIndex);


/*************************************************************************
* SetProgramCounter:
* 	The program counter is always set to 0 by default. This function
* 	allows a user to change the default setting of the program counter
* 	to any valid selection within the emulator.
*
* RETURNS: a program counter value
**************************************************************************/
void SetProgramCounter(int &programCounter);


/*************************************************************************
* MemComponents:
* 	This function allows the user to visibly observe the values in all
* 	memory cells; input, output & main memory.
*
* RETURNS: all memory components and their respective values.
**************************************************************************/
void MemComponents(string inputCard[], string mainProgram[],
				   string outputCard[]);


/*************************************************************************
* ClearOutputCards:
* 	This function allows the user to completely empty out the output card
* 	array.
*
* RETURNS: an empty output card array
**************************************************************************/
void ClearOutputCards(string outputCard[], int &outputCardIndex);


/*************************************************************************
* SetMainProgram:
* 	This function allows the user to input values into main memory. The
* 	user can input as many values as they wish until main memory runs out
* 	of space.
*
* RETURNS: values into main memory.
**************************************************************************/
void SetMainProgram(string mainProgram[], int &mainProgramIndex);


/*************************************************************************
* Step:
* 	This function allows the code to usher in one iteration of the simple
* 	computer.
*
* RETURNS: 1 iteration of the simple computer emulator
**************************************************************************/
void Step(string mainProgram[], int &mainProgramIndex, string inputCard[],
		  int &inputCardIndex, string outputCard[], int &outputCardIndex,
		  string &accumulator, string &iR, int &programCounter, int &pick,
		  int &stepHolderInput, bool run);


/*************************************************************************
* processAccum:
* 	This function allows the code to accurately convert a negative
* 	accumulator value into an integer. It has a repetitive nature so it has
* 	been made into its own function.
*
* RETURNS: a readable accumulator which can be accurately converted into
* 		   an integer.
**************************************************************************/
void processAccum(string &accumulator);


/*************************************************************************
* Input:
* 	This function allows the code to process all "0##" instructions
* 	accurately and efficiently.
*
* RETURNS: an accurate instruction execution into main memory from the
* 		   input card.
**************************************************************************/
void Input(string inputCard[], bool &valid, int &stepHolderInput,
		   int &pick, string &iR, string mainProgram[],
		   int &programCounter, int &result);


/*************************************************************************
* SaveToFile:
* 	This function allows the code to save all memory components to an
* 	out file "Save.txt". This allows the code to save all the contents
* 	of memory in a user friendly manner. This executes only after the
* 	code terminates.
*
* RETURNS: this returns all the contents of memory; the input card, the
* 		   output card & main memory, to an output file after the program
* 		   has been terminated. The file it is saved to is "Save.txt".
**************************************************************************/
void SaveToSave(ostream &outFile, string iR,
				string mainProgram[], int programCounter,
				string inputCard[], string outputCard[],
				string accumulator);


/*************************************************************************
* SaveToOption:
* 	This function allows the code to save all memory components to an
* 	out file "Option.txt". This allows the code to print all the contents
* 	of memory in a computer friendly manner. The primary function for this
* 	is to re load the contents back into memory.
*
* RETURNS: this returns all the contents of memory; the input card, the
* 		   output card & main memory, to an output file. The file it is
* 		   saved to is "Option.txt".
**************************************************************************/
void SaveToOption(ostream &loadoutFile, string iR, string mainProgram[],
				int programCounter, string inputCard[],
				string outputCard[], string accumulator);


/*************************************************************************
* LoadFromFile:
* 	This function allows the code to load all the saved contents of
* 	memory accurately & efficiently. This function loads from text file
* 	"Option.txt". This text file has had its contents saved into it
* 	in a computer friendly manner to make extraction more efficient.
*
* RETURNS: this returns all the contents of memory; the input card, the
* 		   output card & main memory, back into the code, from the text
* 		   file "Option.txt".
**************************************************************************/
void LoadFromFile(ifstream &inFile, string mainProgram[],
				  string inputCard[], string outputCard[],
				  string &accumulator, string &iR, int &programCounter);


#endif /* HEADER_H_ */
