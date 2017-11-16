#include"header.h"

/*************************************************************************
 * 				      SIMLE COMPUTER EMULATOR
 * _______________________________________________________________________
 *
 * This program will allow any user to input simple computer commands
 *  and run the input values. The program does this through a set of
 *  executable functions. First, the user is presented with a list of
 *  options. Among the options the user will find all necessary listings
 *  to run a simple computer program. After the user has made their choice
 *  the program follows the users pick into a switch statement which
 *  contain the entire program. After the user has made a selection the
 *  code flows into a while loop which contains a switch statement. Within
 *  this while loop switch statement the code executes every command the
 *  users has input into the simple computer. After the code has executed
 *  the switch statement the user is presented with the same option menu.
 *  The program repeats until a trigger allows the code to exit the while
 *  loop.
 * _______________________________________________________________________
 * INPUTS:
 * inFile				   - Allows the code to extract input from a file.
 * 							 The code executes the extraction & places
 * 							 relevant data into their respective
 * 							 positions & process its execution.
 * 	UserPick(pick)		   - This allows a user to manipulate a simple
 * 							 computer as they see fit. The user can make
 * 							 any relevant selection & can input any
 * 							 relevant values into the simple computer.
 *
 * OUTPUT:
 * outFile				   - This performs a saving mechanism. It is also
 * 							 a mechanism to output all relevant data into
 * 							 an output file.
 *
 *************************************************************************/

/*************************************************************************
 * 						FUNCTION DEFINITIONS
 *
 * 	PrintHeader				- Used to print the class header.
 * 	UserPick				- Allows the user to make a valid selection
 * 							  based on the main menu.
 * 	AddInput				- Allows the user to add input values into the
 * 							  input card.
 * 	ClearInputCard			- Used to simply & efficiently clear the input
 * 							  card.
 * 	ClearAll				- Simply clears the input & output cards &
 * 							  also clears main memory.
 * 	ClearMainProgram		- Used to efficiently clear the main memory of
 * 							  of the program.
 * 	SetProgramCounter		- Allows the user to set the program counter
 * 							  to a valid main memory cell.
 * 	MemComponents			- List all memory components; output, input &
 * 							  main memory cards.
 * 	ClearOutputCards		- Allows the user to clear the output card.
 * 	SetMainProgram			- Allows the user to set main memory.
 * 	Step					- A trace function which allows the user to
 * 							  essentially walk through a program step by
 * 							  step. Updates the CPU after every step.
 * 	processAccum			- A special function is of a repetitive
 * 							  nature in the code. This function allows
 * 							  the code to process a negative accumulator
 * 							  for accurate conversion from a string to
 * 							  an integer.
 * 	Input					- Allows the code to process any Op Code
 * 							  input which begins with 0 _ _ . This
 * 							  function is used as an example of how easily
 * 							  the "Step" function could have been
 * 							  broken up into separate functions which
 * 							  represent of the the starting digits.
 * 	SaveToSave				- This function prints all the contents of
 * 							  every memory cell into the text file
 * 							  "Save.txt". The function prints all memory
 * 							  into a user friendly format. This function
 * 							  executes automatically after the code has
 * 							  terminated. The manner of termination is
 * 							  irrelevant. This will always say the final
 * 							  values of the CPU & all memory.
 * 	SaveToOption			- This function saves the contents of the CPU
 * 							  & all memory into the text file "Option.txt".
 * 							  The purpose of this save is simply to be
 * 							  able to reload the values into the code. This
 * 							  function does not save the contents of all
 * 							  memory in a user friendly manner.
 * 	LoadFromFile			- This allows the code to load all the
 * 							  contents of "Option.txt" into the appropriate
 * 							  memory cells. This function loads the values
 * 							  from a text file which has had its values
 * 							  loaded onto it in a computer friendly
 * 							  manner.
 *
 *************************************************************************/




int main()
{
	string mainProgram[MAIN_PROGRAM];	//INPUT - CALC  : This is the main
										//				  memory of the
										//				  simple computer.
	int    mainProgramIndex;			//CALC		    : This allows the
										//				  code to keep
										//				  track of how
										//				  many inputs have
										//				  been entered.

	string inputCard[INPUT_CARD];		//INPUT - CALC  : This is the
										//				  input card of
										//				  the simple
										//				  computer.
	int    inputCardIndex;				//CALC		    : This allows the
										//				  code to keep
										//				  track of how
										//				  many inputs have
										//				  been entered.

	string outputCard[OUTPUT_CARD];		//CALC - OUTPUT : This is the
										//				  output card
										//				  of the simple
										//				  computer.
	int    outputCardIndex;				//CALC		    : This allows the
										//				  code to keep
										//				  track of how
										//				  many inputs have
										//				  been entered.

	string accumulator;					//CALC - OUTPUT : Keeps track of
										//				  of the value of
										//				  the accumulator.
	string iR;							//CALC - OUTPUT : Allows the users
										//				  to see which
										//				  instruction was
										//				  just executed.
	int    programCounter;				//INPUT - CALC  : Allows the user
										//				  to see where
										//				  the next instr-
										//				  uctions will be
										//				  executed.

	int    pick;						//INPUT - CALC  : Allows the user
										//				  to select
										//				  commands for the
										//				  emulator.
	int stepHolderInput;				//CALC			: Allows the code
										//				  to keep track
										//				  of how many
										//				  inputs have
										//				  been taken from
										//				  the input card.
	bool run;							//CALC			: Controls the
										//				  output stream of
										//				  the CPU
	ofstream outFile;					//CALC - OUTPUT : Allows the user
										//				  to save the
										//				  contents of all
										//				  memory.
	ofstream loadoutFile;				//CALC			: Used to save the
										//				  contents to all
										//				  memory in a way
										//				  which can then
										//			      be reloaded.
	ifstream inFile;					//INPUT - CALC  : Allows the user
										//				  to load a pro-
										//			      gram into the
										//				  emulator.

	//Default settings for the simple computer
	mainProgram[0] 	 = "001";
	accumulator 	 = "";
	programCounter   = 0;
	outputCardIndex  = 0;
	inputCardIndex   = 0;
	stepHolderInput  = 0;
	mainProgramIndex = 1;
	run 			 = false;

	inFile.open ("Option.txt");
	outFile.open("Save.txt");
	loadoutFile.open("Option.txt");

	//Printing the class header to the output file & cout console.
	PrintHeader(outFile, "Simple Computer Emulator", "Term Project");
	PrintHeader(cout, "Simple Computer Emulator", "Term Project");

	UserPick(pick);

	while(pick != -1)
	{
		switch(pick)
		{
		case 0: MemComponents(inputCard, mainProgram, outputCard);
		break;

		case 1: AddInput(inputCard, inputCardIndex);
		break;

		case 2: SetProgramCounter(programCounter);
		break;

		case 3: SetMainProgram(mainProgram, mainProgramIndex);
		break;

		case 4: ClearInputCard(inputCard, inputCardIndex);
		break;

		case 5: ClearMainProgram(mainProgram, mainProgramIndex);
		break;

		case 6: ClearOutputCards(outputCard, outputCardIndex);
		break;

		case 7: ClearAll(inputCard, inputCardIndex, mainProgram,
						 mainProgramIndex, accumulator, iR,
						 programCounter, outputCard, outputCardIndex);
		break;

		case 8: //Run simply makes sure that the CPU update is not
				//printed every single time, only after the program
				//has terminated.
				run = true;

				while(pick != -1)
				{
					Step(mainProgram, mainProgramIndex, inputCard,
						 inputCardIndex, outputCard, outputCardIndex,
						 accumulator, iR, programCounter, pick,
						 stepHolderInput, run);
				}
		break;

		case 9: Step(mainProgram, mainProgramIndex, inputCard,
					 inputCardIndex, outputCard, outputCardIndex,
					 accumulator, iR, programCounter, pick,
					 stepHolderInput, run);
		break;

		case 10: //Simply showing the CPU
				 cout << "\nCPU\n" << "----";
				 cout << "\nAccumulator: " << accumulator;
				 cout << "\nPC: " 		   << setw(2) << setfill('0')
													  << programCounter;
				 cout << "\nIR: " 		   << iR << endl;
				 cin.get();
		break;

		case 11: //This Save Option is for when the user wants to save
				 //all the contents of memory during an active run of
				 //of the simple computer emulator
				 SaveToOption(loadoutFile, iR, mainProgram,
							  programCounter, inputCard, outputCard,
							  accumulator);
		break;

		case 12: //Load from file
				LoadFromFile(inFile, mainProgram, inputCard, outputCard,
						     accumulator, iR, programCounter);
		break;
		case -1: break;
		break;
		}


		if(pick != -1)
		{
			//Program has not been terminated
			cout << endl << endl;
			UserPick(pick);
		}
		else
		{
			//This save option is used for when the simple computer
			//emulator has finished running. It saves the final state of
			//the CPU & all memory slots; input card, output card &
			//main memory.
			SaveToSave(outFile, iR, mainProgram,  programCounter,
					    inputCard, outputCard, accumulator);
		}
	}

	//Closing the files.
	outFile.close();
	inFile.close();
	loadoutFile.close();

	return 0;
}
