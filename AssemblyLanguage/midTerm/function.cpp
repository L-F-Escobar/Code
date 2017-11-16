#include"header.h"

//Simply prints out the class header into "Save.txt" & cout console.
void PrintHeader(ostream &outFile, string asName, string asType)
{
	outFile << left;
	outFile << "*********************************************************"
			   "******************\n";
	outFile << "Programmed by : Luis Fernando Escobar-Driver\n";
	outFile << setw(14) << "Student ID" << ": 638386\n";
	outFile << setw(14) << "Class" << ": CS3A --> MW --> 6:00 - 9:20pm\n";
	outFile << setw(14) << "Assignment " << ": " << asType << " --> "
												 << asName;
    outFile << "\n*******************************************************"
    		   "********************\n\n";
    outFile << right;
}



/*************************************************************************
 * This function allows the user to make a valid selection choice from a
 *  menu with valid options for a simple computer emulator. The selection
 *  options are clearly posted below. All invalid selections by the user
 *  are rejected & the user is prompted for a new selection.
 *************************************************************************/
void UserPick(int &pick)
{
	bool valid;

	cout << "Command List\n";
	cout << "---------------\n\n";
	cout << "#0 - List all memory components to the screen\n\n";
	cout << "#1 - Set Input Card\n\n";
	cout << "#2 - Set Program Counter\n\n";
	cout << "#3 - Set Main Memory\n\n";
	cout << "#4 - Clear input card\n\n";
	cout << "#5 - Clear Main Memory\n\n";
	cout << "#6 - Clear Output Cards\n\n";
	cout << "#7 - Clear All\n\n";
	cout << "#8 - Run\n\n";
	cout << "#9 - Step\n\n";
	cout << "#10- Show the CPU\n\n";
	cout << "#11- Save the contents of memory in their current form\n\n";
	cout << "#12- Load program from Option.txt\n\n";
	cout << "#-1  TO EXIT PROGRAM\n\n";

	cout << "\nEnter your selection: ";
	cin >> pick;

	do
	{
		valid = true;

		if(!(cin))
		{
			cin.clear();
			cin.ignore(numeric_limits<streamsize>::max(), '\n');

			cout << "\nPlease enter a NUMBER between -1 & 12\n";

			valid = false;
		}
		else if(pick > 12 || pick < -1)
		{
			cout << "\nINVALID selection. Please pick a number between "
													         "-1 & 12\n";
			valid = false;
		}


		if(!valid)
		{
			cout << "Please make your new selection: ";
			cin >> pick;
		}


	}while(!valid);
}//END


/*************************************************************************
 * This function allows the user to make a valid selection into main
 *  memory. The function will never allow the user to make a selection for
 *  cell #00. The function will reject any selection inconsistent with
 *  a simple computer emulator. The user is allowed to make any selection,
 *  a valid selection will be accepted and then modified if needed to
 *  meet a certain visual requirement. For example, the user can input the
 *  value "5", the code will take the value and input it into main memory
 *  as "005".
 *************************************************************************/
void AddInput(string intputCard[], int &inputCardIndex)
{
	int inputNumber;		//INPUT - CALC: Users selection
	bool valid;				//CALC		  : Used to control do while loops
	char another = 'Y';		//CALC		  : Defaulted on allowing the user
							//				to make a selection

	//While there is room on the input card go into the IF
	if(inputCardIndex < INPUT_CARD)
	{
		//This is the default selection.
		while(another == 'Y')
		{
			cout << "\nSet input card cell #" << inputCardIndex
											  << " to: ";
			cin >> inputNumber;

			do
			{
				valid = true;

				if(!(cin))
				{
					cin.clear();
					cin.ignore(numeric_limits<streamsize>::max(), '\n');
					valid = false;
					cout << "\nPlease enter a NUMBER between -999 & 999\n";
				}
				else if(inputNumber < -999 || inputNumber > 999)
				{
					cout << "\nINVALID selection. Please pick a number "
							     	 	 	 	   "between -999 & 999\n";
					valid = false;
				}

				if(!valid)
				{
					cout << "\nPlease make your new selection: ";
					cin >> inputNumber;
				}

			}while(!valid);//END OF DO-WHILE

			//This is to help convert negative numbers into their proper
			//string representation.
			ostringstream convert;
			if(inputNumber < 0)//-1 -2 ... -998 -999
			{
				//Making it positive for extraction
				inputNumber = inputNumber * -1;

				//This reintroduces the negative as a string
				//Making the negative strings 4 bits long
				convert << "-" << setw(3) << setfill('0') << inputNumber;

			}
			else//positive number
			{
				//Making this 3 bits long
				convert << setw(3) << setfill('0') << inputNumber;
			}

			cout << "\nInput has been registered!";
			cout << "\nSetting main memory cell #" << inputCardIndex
				 <<  " to: "  << convert.str();

			//THIS IS WHERE THE ADDING ONTO THE INPUT CARD ACTUALLY
			//TAKES PLACE
			intputCard[inputCardIndex] = convert.str();
			inputCardIndex++;//INCREMENTS INPUTCARD HOLDER
			convert.str(""); //Clearing the string for the next iteration


			cout << "\n\nWould you like to add another input(Y/N)? ";
			cin >> another;
			cin.ignore(1000,'\n');
			another = toupper(another);

			do
			{
				valid = true;

				if(!(cin))
				{
					cin.clear();
					cin.ignore(numeric_limits<streamsize>::max(), '\n');
					valid = false;
					cout << "\nPlease enter 'Y' or 'N'\n";
				}
				else if(another != 'Y' && another != 'N')
				{
					cout << "\nPlease enter Y/N!\n";
					valid = false;
				}

				if(!valid)
				{
					cout << "\nNew selection: ";
					cin >> another;
					another = toupper(another);
				}

			}while(!valid);//END OF DO WHILE
		}//END OF WHILE LOOP
	}//END OF IF
	//If there is no room in the input card execute the ELSE
	else
	{
		cout << "\nMemory is full!";
	}//END OF IF-ELSE
}//END


/*************************************************************************
 * This function allows the code to simply clear the input card & return
 *  it to its original default state. The inputCardIndex is also returned
 *  to its default state.
 *************************************************************************/
void ClearInputCard(string inputCard[], int &inputCardIndex)
{
	int holder;		//CALC : Used as an LCV for a For loop

	if(inputCardIndex == 0)
	{
		cout << "\nInput card is already empty";
	}
	else
	{
		for(holder = 0; holder < inputCardIndex; holder++)
		{
			inputCard[holder] = "";
		}

		cout << "\nInput card has been cleared!";
		inputCardIndex = 0;
	}
}//END


/*************************************************************************
 * This function allows the code to completely return every variable of
 *  the simple computer to its default state. This function clears out the
 *  input card, output card & main memory arrays. This function also
 *  returns the accumulator, iR & program counters to their original
 *  states.
 *************************************************************************/
void ClearAll(string inputCard[], int &inputCardIndex, string mainProgram[]
		  , int &mainProgramIndex, string &accumulator, string &iR,
		  int &programCounter, string outputCard[], int &outputCardIndex)
{
	int holder;		//CALC : Used as an LCV

	//Resetting the emulators default positions
	accumulator = "";
	iR = "";
	programCounter = 0;

							//inputCardIndex
	for(holder = 0; holder < 14; 				holder++)
	{
		inputCard[holder] = "";
	}
	inputCardIndex = 0;

	//Starts at 01 to protect cell 00
	for(holder = 1; holder < 99; holder++)
	{
		mainProgram[holder] = "";
	}
	mainProgramIndex = 1;


	for(holder = 0; holder < outputCardIndex; holder++)
	{
		outputCard[holder] = "";
	}
	outputCardIndex = 0;


	cout << "\nThe entire program has been cleared!";
}//END


/*************************************************************************
 * This function allows the code to simply clear the main memory array &
 *  return it to its original state. This functions also returns the
 *  mainProgramIndex to its original state.
 *************************************************************************/
void ClearMainProgram(string mainProgram[], int &mainProgramIndex)
{
	int holder;		//CALC : Used as an LCV for a For loop

		//This setup protects cell# 00
		//Since main memory can have very random cells in usage the
		//program simply empties out the entire main memory array.
		for(holder = 1; holder < 99; holder++)
		{
			mainProgram[holder] = "";
		}

		cout << "\nMain Memory has been cleared!";
		mainProgramIndex = 1;
}//END


/*************************************************************************
 * This function allows the user to change the program counters default
 *  state of 0. The user is give the option to change the program counter
 *  to any number consistent with the nature of the simple computer
 *  emulator.
 *************************************************************************/
void SetProgramCounter(int &programCounter)
{
	int holder;  	//INPUT - CALC : User choice on PC
	bool valid;		//CALC		   : Used to control do-while loop

	cout << "\nWhich cell should the program counter be set to: ";
	cin >> holder;

	do
	{
		valid = true;

		if(!(cin))
		{
			cin.clear();
			cin.ignore(numeric_limits<streamsize>::max(),'\n');

			cout << "\nPlease enter a NUMBER between 00 - 99\n";
			valid = false;
		}
		else if(holder > 99 || holder < 00)
		{
			cout << "\nPlease enter a number between 00 - 99\n";
			valid = false;
		}


		if(valid == false)
		{
			cout << "\nWhich cell should the program be set to: ";
			cin >> holder;
		}

	}while(!valid);

	programCounter = holder;

	cout << "\nThe Program Counter has been set to: " << setw(2)
		 << setfill('0') <<programCounter << endl;
}//END


/*************************************************************************
 * This function allows the code to simply print out every single memory
 *  array; the input card, output card & main memory.
 *************************************************************************/
void MemComponents(string inputCard[], string mainProgram[],
				   string outputCard[])
{
	int holder;			//CALC	: Used as a placeholder for outputting
						//		  all the string arrays

	cout << "\n\nListing Input Cards\n";
	for(holder = 0; holder < INPUT_CARD; holder++)
	{
		cout << "\nInput card cell #" << setw(2) << setfill('0')
									  << holder + 1  << ": ";
		cout << inputCard[holder];
	}

	cout << "\n\nListing Output Cards\n";
	for(holder = 0; holder < OUTPUT_CARD; holder++)
	{
		cout << "\nOutput Cell #" << setw(2) << setfill('0')
								  << holder + 1 << ": ";
		cout << outputCard[holder];
	}

	cout << "\n\nListing Main Memory\n";
	for(holder = 0; holder < MAIN_PROGRAM; holder++)
	{
		//This is to align the display of the 0-9 & 10-99 numbers
		if(holder < 10)
		{
			cout <<  "\nMain memory cell #" << setw(2) << holder << ": ";

			cout << mainProgram[holder];
		}
		else
		{
			cout <<  "\nMain memory cell #" << holder << ": ";
			cout << mainProgram[holder];
		}
	}
}//END


/*************************************************************************
 * This function allows the code to return the output card to its default
 *  state. This function entirely clears out the output card.
 *************************************************************************/
void ClearOutputCards(string outputCard[], int &outputCardIndex)
{
	int holder;		//CALC : Used as an LCV

	if(outputCardIndex == 0)
	{
		cout << "\nOutput cards are empty already!";
	}
	else
	{
		for(holder = 0; holder < outputCardIndex; holder++)
		{
			outputCard[holder] = "";
		}

		cout << "\nOutput Cards have been cleared!";
	}
}//END


/*************************************************************************
 * This function allows the users to input valid selections into the
 *  main memory array. It allows the user to make as many selections as
 *  they wish or up until there is no more memory left. The program takes
 *  all valid inputs and modifies, if need be, to fit a standard model
 *  of the way input should look. For example, if the user inputs "5" into
 *  a main memory cell, the code will take that input and place "005" into
 *  that main memory cell.
 *************************************************************************/
void SetMainProgram(string mainProgram[], int &mainProgramIndex)
{
	int    inputNumber;		//INPUT - CALC : User selection of the value
							//				 which will go into main
							//				 memory.
	bool   valid;			//CALC		   : Used to control do-while loop
	char anotherRun = 'Y';  //INPUT - CALC : Defaulted to allowing another
							//				 run. Allows the user to stop
							//				 making selection.
	char newCell 	= 'Y';  //INPUT - CALC : Defaulted to allowing a new
							//				 cell selection. Allows the
							//				 user to stop making selection

	//While there are still main memory cells that are open go into the IF
	if(mainProgramIndex < MAIN_PROGRAM)
	{
		//The default comes into play
		while(anotherRun == 'Y')
		{
			//The other default comes into play
			if(newCell == 'Y')
			{
				cout << "\nWhich cell would you like to start in: ";
				cin >> mainProgramIndex;

				//This do-while loop protects cell #00 & ensures a proper
				//numerical selection
				do
				{
					valid = true;

					if(!(cin))
					{
						cin.clear();
						cin.ignore(numeric_limits<streamsize>::max(),'\n');
						valid = false;
						cout << "\nPlease enter a NUMBER between 01 & 99";
					}
					else if(mainProgramIndex > 99 || mainProgramIndex < 1)
					{
						cout << "\nPlease enter a number between 01 & 99";
						valid = false;
					}

					if(!valid)
					{
						cout << "\n\nWhich cell would you like to begin "
								"in: ";
						cin >> mainProgramIndex;
					}

				}while(!valid);
			}

			cout << "\nEnter value into main memory cell #"
				 << mainProgramIndex << ": ";
			cin >> inputNumber;

			do
			{
				valid = true;

				if(!(cin))
				{
					cin.clear();
					cin.ignore(numeric_limits<streamsize>::max(), '\n');
					valid = false;
					cout << "\nPlease enter a NUMBER between -999 & 999\n";
				}
				else if(inputNumber < -999 || inputNumber > 999)
				{
					cout << "\nINVALID selection. Please pick a number "
												   "between -999 & 999\n";
					valid = false;
				}

				if(!valid)
				{
					cout << "\nPlease make your new selection: ";
					cin >> inputNumber;
				}

			}while(!valid);

			//This is to help convert negative numbers into their proper
			//string representation.
			ostringstream convert;
			if(inputNumber < 0)//-1 -2 ... -998 -999
			{
				//Making it positive for extraction
				inputNumber = inputNumber * -1;

				//This reintroduces the negative as a string
				//Making the negative strings 4 bits long
				convert << "-" << setw(3) << setfill('0') << inputNumber;
			}
			else//positive number
			{
				//Making this 3 bits long
				convert << setw(3) << setfill('0') << inputNumber;
			}

			cout << "\nInput has been registered!";
			cout << "\nSetting main memory cell #" << mainProgramIndex
				 <<  " to: "  << convert.str();

			//THIS IS WHERE THE ADDING ACTUALLY TAKES PLACE
			mainProgram[mainProgramIndex] = convert.str();
			//INCREMENTS INPUTCARD HOLDER
			mainProgramIndex++;
			//Clearing string stream variable for next use
			convert.str("");

			//Here is where "anotherRun" default can be changed
			cout << "\n\nContinue onto main memory cell #"
				 << mainProgramIndex << " (Y/N)?: ";
			cin >> anotherRun;
			cin.ignore(1000,'\n');
			anotherRun = toupper(anotherRun);

			do
			{
				valid = true;

				if((anotherRun != 'Y' && anotherRun != 'N'))
				{
					cout << "\nPlease enter Y/N! ";
					valid = false;
				}

				if(!valid)
				{
					cout << "\nNew selection: ";
					cin >> anotherRun;
					cin.ignore(1000,'\n');
					anotherRun = toupper(anotherRun);
				}

			}while(!valid);


			if(anotherRun == 'N')
			{
				//Here is where "newCell" default can be changed.
				//If the user has opted to not continue onto the next
				//cell && selected 'N' to the new cell, this tells the
				//code to exit.
				cout << "\nWould you like to begin in a new main memory"
						" cell (Y/N)?: ";
				cin >> newCell;
				cin.ignore(1000,'\n');
				newCell = toupper(newCell);

				do
				{
					valid = true;

					if((newCell != 'Y' && newCell != 'N'))
					{
						cout << "\nPlease enter Y/N! - TEST FOR Y/N";
						valid = false;
					}

					if(!valid)
					{
						cout << "\nNew selection: ";
						cin >> newCell;
						cin.ignore(1000,'\n');
						newCell = toupper(newCell);
					}

				}while(!valid);

				//This tells the code that the user does not want to
				//continue onto the next cell but still wants to input
				//values into the main memory cells.
				if(newCell == 'Y')
				{
					anotherRun = 'Y';
				}
			}
			else
			{
				newCell = 'N';
			}
		}
	}
	else
	{
		cout << "\nMain Memory is full!";
	}
}//END


/*************************************************************************
 * This function allows the entire simple computer to come together. After
 *  the user has made valid choices regarding their inputs into the
 *  memory card arrays, this function takes all the data and processed
 *  it for an accurate & efficient execution cycle. This function allows
 *  the code to run one execution cycle at a time, with an update of the
 *  CPU each time. It also allows the emulator to terminate & in what
 *  manner the termination took place. This step function takes the first
 *  digit of the values in main memory & based upon that decides which
 *  set of instructions should be executed. Every single one of the
 *  number inputs could itself be a separate function. The coder
 *  decided simply to just place the code into this one Step function,
 *  however, anyone could simply copy & past the code into an
 *  appropriately named function. The coder shows an example of this with
 *  the input function for the number "0".
 *************************************************************************/
void Step(string mainProgram[], int &mainProgramIndex, string inputCard[],
		  int &inputCardIndex, string outputCard[], int &outputCardIndex,
		  string &accumulator, string &iR, int &programCounter, int &pick,
		  int &stepHolderInput, bool run)
{
	string convert;			//CALC		  : Used to hold string
							//				representations of int values.
	string storage;         //CALC		  : Used to hold a string value
							//				for a conversion
	string accumHolder;		//CALC		  : Used to hold a temp copy of
							//				the accumulator
	string cellValue;		//CALC		  : Used to process an int value
							//				out of a string.
	int result;				//CALC		  : Used to hold int
							//				representations of string
							//				values.
	int tempPC;				//CALC		  : Used as a temp program counter
	int tempAccum;			//CALC		  : Used as a temp accumulator
	int tempMainMem;		//CALC		  : Used as a temp int
							//				represenation of a string
							//				value.
	bool valid;				//CALC 		  : Used to determine if an
							//				operation is valid.

	bool normal = false;	//CALC		  : Used as a normal termination
							//				trigger
	//DEFAULTS :: CALC
	bool unconditionalJump = false; //This tells the code that there has
									//been no unconditional jump.
	bool conditionalJump = false;   //This tells the code that there has
									//been no unconditional jump.

	//When a user wants to input into main memory
	if(mainProgram[programCounter][0] == '0')
	{
		Input(inputCard, valid, stepHolderInput, pick, iR, mainProgram,
			  programCounter, result);
	}
	//Output
	else if(mainProgram[programCounter][0] == '1')
	{
		//Checks to see if there is still room on the output card
		if(outputCardIndex < OUTPUT_CARD)
		{
			//Saving the string value of main memory into a variable which
			//will allow the program to convert that variable into an int
			storage = mainProgram[programCounter][1];
			storage = storage + mainProgram[programCounter][2];

			//Converting the saved string variable into an int, which
			//then functions as our temporary program counter
			istringstream convert(storage);
			convert >> tempPC;

			//Gathering the value of the specified memory cell
			cellValue = mainProgram[tempPC];

			//Saving that variable onto the output card
			outputCard[outputCardIndex] = cellValue;

			outputCardIndex++;
			//Setting the IR
			iR = mainProgram[programCounter];

			//Clearing for next run
			convert.str("");
			storage = "";
			cellValue = "";
		}
		else
		{
			cout << "\nOutput Memory Card Full. Program has halted\n";
			pick = -1;
		}
	}
	//Add
	else if(mainProgram[programCounter][0] == '2')
	{
		//Default position of the program is that the accumulator is not
		//negative. This is used to catch a negative accumulator &
		//accurately convert it to an int variable
		bool accumNeg = false;

		//Saving the string value of main memory into a variable which
		//will allow the program to convert that variable into an int
		storage = mainProgram[programCounter][1];
		storage = storage + mainProgram[programCounter][2];

		//Converting the saved string variable into an int
		istringstream convert(storage);
		convert >> tempPC;

		//This If loop is used to convert the Accumulator string value
		//into an int value which can be used to subtract properly
		if(accumulator == "")
		{
			//Used for first run when accumulator = "";
			accumulator = "0000";
		}
		else if(accumulator.size() == 5)//signifies a negative number
		{
			//Triggers the negative flag
			accumNeg = true;

			//Saving a copy of the accumulator & resetting the accumulator
			accumHolder = accumulator;
			accumulator = "";

			//This proceding piece of code takes the positive string
			//values and saves them while discarding the rest.
			//This is to catch negative Ones, Tens & Hundreds
			//This catches negative Tens
			if(accumHolder[2] == '-')
			{
				//This catches negative Ones
				if(accumHolder[3] == '-')
				{
					accumulator = accumulator + accumHolder[4];
				}
				else
				{
					accumulator = accumulator + accumHolder[3];
					accumulator = accumulator + accumHolder[4];
				}

			}
			else
			{
				//This catches negative Hundreds
				accumulator = accumHolder[2]; // 3 & 4
				accumulator = accumulator + accumHolder[3];
				accumulator = accumulator + accumHolder[4];
				accumHolder = "";
			}
		}//END of the negative fix

		//Now we can convert the accumulator into a positive int. This
		//type of conversion only works for positive conversions.
		//That is the reason for the preceding code. To extract only the
		//positive numbers while triggering the negative flag.
		istringstream accumConvert(accumulator);
		accumConvert >> tempAccum;

		//Converting the string value of the tempPC into an int.
		//Grabbing the value from main memory that will be subtracted
		//from the accumulator
		istringstream mainMemConvert(mainProgram[tempPC]);
		mainMemConvert >> tempMainMem;

		//If the negative flag has been triggered
		//This restores the negativity to the number.
		if(accumNeg == true)
		{
			tempAccum = -1 * tempAccum;
		}

		//The actual value is being calculated
		tempAccum = tempAccum + tempMainMem;

		ostringstream newAccum;
		//Used for proper emulating properties
		if(tempAccum >= 0)//positive
		{
			newAccum << setw(4) << setfill('0') << tempAccum;
		}
		else//negative
		{
			if(tempAccum <= -1000)
			{
				tempAccum = tempAccum * -1;
				newAccum << "1-" << setw(3) << setfill('0') << tempAccum;
			}
			else//under -1000
			{
				tempAccum = tempAccum * -1;
				newAccum << "0-" << setw(3) << setfill('0') << tempAccum;
			}
		}

		//Assigning the new values
		accumulator = newAccum.str();
		iR = mainProgram[programCounter];

		//Clearing out the variables for the next iteration
		convert.str("");
		accumConvert.str("");
		mainMemConvert.str("");
		newAccum.str("");
		storage = "";
		accumHolder = "";
	}
	//Subtract
	else if(mainProgram[programCounter][0] == '3')
	{
		//Default position of the program is that the accumulator is not
		//negative. This is used to catch a negative accumulator &
		//accurately convert it to an int variable
		bool accumNeg = false;

		//Saving the string value of main memory into a variable which
		//will allow the program to convert that value into an int
		storage = mainProgram[programCounter][1];
		storage = storage + mainProgram[programCounter][2];

		//Converting the saved string value into an int
		istringstream convert(storage);
		convert >> tempPC;

		//This If loop is used to convert the Accumulator string value
		//into an int value which can be used to subtract
		if(accumulator == "")
		{
			//Used for first run when accumulator = "";
			accumulator = "0000";
		}
		else if(accumulator.size() == 5)//Negative
		{
			//Trip the negative flag
			accumNeg = true;

			accumHolder = accumulator;
			accumulator = "";

			//This is to catch negative Ones & Tens & Hundreds
			//This catches negative Tens
			if(accumHolder[2] == '-')
			{
				//This catches negative Ones
				if(accumHolder[3] == '-')
				{
					accumulator = accumulator + accumHolder[4];
				}
				else
				{
					accumulator = accumulator + accumHolder[3];
					accumulator = accumulator + accumHolder[4];
				}
			}
			else
			{
				//This catches negative Hundreds
				accumulator = accumHolder[2]; // 3 & 4
				accumulator = accumulator + accumHolder[3];
				accumulator = accumulator + accumHolder[4];
				accumHolder = "";
			}
		}

			istringstream accumConvert(accumulator);
			accumConvert >> tempAccum;

			//Converting the string value of the tempPC into an int
			//Grabbing the value from main memory that will be subtracted
			//from the accumulator
			istringstream mainMemConvert(mainProgram[tempPC]);
			mainMemConvert >> tempMainMem;

			//If the negative flag has been tripped
			if(accumNeg == true)
			{
				tempAccum = -1 * tempAccum;
			}

			//Doing the subtraction after all the conversion have been
			//completed. This is the value of the new Accumulator
			tempAccum = tempAccum - tempMainMem;

			ostringstream newAccum;
			if(tempAccum >= 0)
			{
				newAccum << setw(4) << setfill('0') << tempAccum;
			}
			else//negative
			{
				if(tempAccum <= -1000)
				{
					tempAccum = tempAccum * -1;
					newAccum << "1-" << setw(3) << setfill('0') << tempAccum;
				}
				else//under -1000
				{
					tempAccum = tempAccum * -1;
					newAccum << "0-" << setw(3) << setfill('0') << tempAccum;
				}
			}

		//Assigning the new values
		accumulator = newAccum.str();
		iR = mainProgram[programCounter];

		//Clearing out the variables for the next iteration
		convert.str("");
		accumConvert.str("");
		mainMemConvert.str("");
		newAccum.str("");
		storage = "";
	}
	//Load into the accumulator
	else if(mainProgram[programCounter][0] == '4')
	{
		//Saving the string value of main memory into a variable which
		//will allow the program to convert that value into an int
		storage = mainProgram[programCounter][1];
		storage = storage + mainProgram[programCounter][2];

		//Converting the saved string value into an int
		istringstream convert(storage);
		convert >> tempPC;

		accumulator = "0" + mainProgram[tempPC];
		iR = mainProgram[programCounter];

		//Needed//
		convert.str("");
		storage = "";
	}
	//Store the accumulator
	else if(mainProgram[programCounter][0] == '5')
	{
		//Saving the string value of main memory into a variable which
		//will allow the program to convert that value into an int
		storage = mainProgram[programCounter][1];
		storage = storage + mainProgram[programCounter][2];

		//Converting the saved string value into an int
		istringstream convert(storage);
		convert >> tempPC;

		//Holds a copy of the accumulator to use for manipulations
		accumHolder = accumulator;

		//If its entirely empty
		if(accumHolder == "")
		{
			mainProgram[tempPC] = accumHolder;
		}
		else
		{
			if(accumulator.size() == 5)//negative accum string
			{
				accumHolder = accumulator[1];
				accumHolder = accumHolder + accumulator[2];
				accumHolder = accumHolder + accumulator[3];
				accumHolder = accumHolder + accumulator[4];

			}
			else//positive accum string
			{
				accumHolder = accumulator[1];
				accumHolder = accumHolder + accumulator[2];
				accumHolder = accumHolder + accumulator[3];
			}

			//Saving the value string into main memory
			mainProgram[tempPC] = accumHolder;
		}

		iR = mainProgram[programCounter];

		convert.str("");
		storage = "";
	}
	//Unconditional Jump
	else if(mainProgram[programCounter][0] == '6')
	{
		//Triggers the flag
		unconditionalJump = true;

		//Saving the string value of main memory into a variable which
		//will allow the program to convert that into an int
		storage = mainProgram[programCounter][1];
		storage = storage + mainProgram[programCounter][2];

		istringstream convert(storage);
		convert >> tempPC;

		//This is to grab the next mem cell & allow the code to place it
		//into mem cell# 99
		ostringstream conversion;
		conversion << setw(3) << setfill('0') << programCounter + 1;

		mainProgram[99] = conversion.str();
		iR = mainProgram[programCounter];
		programCounter = tempPC;

		//Clearing it out for next iteration
		convert.str("");
		conversion.str("");
		storage = "";
	}
	//Conditional Jump
	else if(mainProgram[programCounter][0] == '7')
	{
		bool accumNeg = false;
		//Making a copy of the accum which will never be changed
		string neverChange = accumulator;

		//A positive accumulator will slip by. A blank or negative one
		//will be adjusted in a manner which will allow a conversion
		//to an int
		if(accumulator == "")//Blank
		{
			accumulator = "0000";
		}
		else if(accumulator.size() == 5)//Negative
		{
			//Trip the flags
			accumNeg = true;
			conditionalJump = true;

			accumHolder = accumulator;
			accumulator = "";

			//This is to catch negative Ones & Tens & Hundreds
			//This catches negative Tens
			if(accumHolder[2] == '-')
			{
				//This catches negative Ones
				if(accumHolder[3] == '-')
				{
					accumulator = accumulator + accumHolder[4];
				}
				else
				{
					accumulator = accumulator + accumHolder[3];
					accumulator = accumulator + accumHolder[4];
				}

			}
			else
			{
				//This catches negative Hundreds
				accumulator = accumHolder[2];
				accumulator = accumulator + accumHolder[3];
				accumulator = accumulator + accumHolder[4];
				accumHolder = "";
			}
		}

		//This gives us the perfectly accurate accumulator conversion
		istringstream conversion(accumulator);
		conversion >> tempAccum;

		if(accumNeg == true)
		{
			//This gives us the perfectly accurate accumulator value
			tempAccum = -1 * tempAccum;
		}


		if(tempAccum <= -1)//Negative
		{
			//Saving the string value of main memory into a variable which
			//will allow the program to convert that value into an int
			storage = mainProgram[programCounter][1];
			storage = storage + mainProgram[programCounter][2];

			istringstream convert(storage);
			convert >> tempPC;

			iR = mainProgram[programCounter];
			programCounter = tempPC;
			accumulator = neverChange;

			//For next iteration
			convert.str("");
			storage = "";
			neverChange = "";
		}
		else//positive
		{
			iR = mainProgram[programCounter];
		}

		//Need to be clear for next iteration
		conversion.str("");
	}
	//Shift
	else if(mainProgram[programCounter][0] == '8')
	{
		string storageTwo; //CALC		: Stores the right shift string
						   //			  value
		int right;		   //CALC		: Stores the right shift int
						   //			  value
		int left;		   //CALC		: Stores the left shift int
						   //			   value
		string holder;	   //CALC		: Used as an LCV

		//This is the level of shift that needs to take place
		storage = mainProgram[programCounter][1];   //LEFT
		storageTwo = mainProgram[programCounter][2];//RIGHT

		//Moving numbers to the left:: Meaning introducing 0's to the
		//right
		istringstream convert(storage);
		convert >> left;

		//Moving numbers to the right:: Meaning introducing 0's to the
		//left
		istringstream rightShift(storageTwo);
		rightShift >> right;

		//Positive
		if(accumulator.size() == 4)
		{
			//Left shift first
			if(left != 0)
			{
				if(left == 1)
				{
					accumulator[0] = accumulator[1];
					accumulator[1] = accumulator[2];
					accumulator[2] = accumulator[3];
					accumulator[3] = '0';

				}
				else if(left == 2)
				{
					accumulator[0] = accumulator[2];
					accumulator[1] = accumulator[3];
					accumulator[2] = '0';
					accumulator[3] = '0';
				}
				else if(left == 3)
				{
					accumulator[0] = accumulator[3];
					accumulator[1] = '0';
					accumulator[2] = '0';
					accumulator[3] = '0';
				}
				else//(left >= 4)
				{
					accumulator[3] = '0';
					accumulator[2] = '0';
					accumulator[1] = '0';
					accumulator[0] = '0';
				}
			}

			if(right != 0)
			{
				//Left shift first, THEN right shift
				if(right == 1)
				{
					accumulator[3] = accumulator[2];
					accumulator[2] = accumulator[1];
					accumulator[1] = accumulator[0];
					accumulator[0] = '0';

				}
				else if(right == 2)
				{
					accumulator[3] = accumulator[1];
					accumulator[2] = accumulator[0];
					accumulator[1] = '0';
					accumulator[0] = '0';
				}
				else if(right == 3)
				{
					accumulator[3] = accumulator[0];
					accumulator[2] = '0';
					accumulator[1] = '0';
					accumulator[0] = '0';
				}
				else//(right >= 4)
				{
					accumulator[3] = '0';
					accumulator[2] = '0';
					accumulator[1] = '0';
					accumulator[0] = '0';
				}
			}//END OF THE RIGHT
		}
		else//(accumulator.size() == 5)//Negative
		{
			if(left != 0)
			{
				if(left == 1)
				{
					accumulator[0] = accumulator[2];
					accumulator[2] = accumulator[3];
					accumulator[3] = accumulator[4];
					accumulator[4] = '0';

					//Seeing if the accum is 1-000
					processAccum(accumulator);
				}
				else if(left == 2)
				{
					accumulator[0] = accumulator[2];
					accumulator[2] = accumulator[3];
					accumulator[3] = '0';
					accumulator[4] = '0';

					//Seeing if the accum is 1-000
					processAccum(accumulator);
				}
				else if(left == 3)
				{
					accumulator[0] = accumulator[2];

					//Seeing if the accum is 1-000
					processAccum(accumulator);
				}
				else//(left >= 4)
				{
					accumulator = "0000";
				}
			}

			//This will be for a right shift
			//Therefore 0's will enter the string from the left.
			if(right != 0)
			{
				if(right == 1)
				{
					accumulator[4] = accumulator[3];
					accumulator[3] = accumulator[2];
					accumulator[2] = accumulator[0];
					accumulator[0] = '0';

					//Seeing if the accum is 1-000
					processAccum(accumulator);
				}
				else if(right == 2)
				{
					accumulator[4] = accumulator[3];
					accumulator[3] = accumulator[2];
					accumulator[2] = '0';
					accumulator[0] = '0';

					//Seeing if the accum is 1-000
					processAccum(accumulator);
				}
				else if(right == 3)
				{
					accumulator[4] = accumulator[3];
					accumulator[3] = '0';
					accumulator[2] = '0';
					accumulator[0] = '0';

					//Seeing if the accum is 1-000
					processAccum(accumulator);
				}
				else//(right >= 4)
				{
					accumulator = "0000";

				}
			}//END OF THE RIGHT
		}

		iR = mainProgram[programCounter];

		//Needed
		storage = "";
		convert.str("");
		storageTwo = "";
		rightShift.str("");
		holder = "";
	}
	//Terminate program
	else if(mainProgram[programCounter][0] == '9')
	{
		normal = true;
		valid = false;
		pick = -1;

		//Saving the string value of main memory into a variable which
		//will allow the program to convert that value into an int
		storage = mainProgram[programCounter][1];
		storage = storage + mainProgram[programCounter][2];

		iR = mainProgram[programCounter];

		istringstream convert(storage);
		convert >> tempPC;

		programCounter = tempPC;

		storage = "";
	}

	//This makes sure the operations were valid
	if(valid == true)
	{
		//This will catch an empty main memory cell
		if(mainProgram[programCounter] != "")
		{
			//Resetting flags that need it OR inc the PC
			if(unconditionalJump == true)
			{
				unconditionalJump = false;
			}
			else if(conditionalJump == true)
			{
				conditionalJump = false;
			}
			else
			{
				programCounter++;
			}

			if(run != true)
			{
				cin.clear();
				cout << "\n\nCPU\n";
				cout << "------";
				cout << "\nIR: " << iR;
				cout << "\nProgram Counter: " << setw(2) << setfill('0')
										  << programCounter;
				cout << "\nAccumulator: " << accumulator;
			}
		}
		else
		{
				cout << "\nProgram Halted: Memory location being fetched "
					 "is empty\n";
				valid = false;
				pick = -1;
		}
	}

	if(normal == true)
	{
		cout << "\nProgram terminated normally.\n";
	}
}


/*************************************************************************
 * This function allows the 8 _ _ to accurately shift a negative
 *  accumulator. Negative accumulators would be of size 5. The accumulator
 *  in the simple computer functions very strangely when it was above
 *  1000. This piece of code works by allowing this code to match the
 *  strange nature of the simple computer it is intended to mimic. Since
 *  this piece of code was of a repetitive nature it was best to simply
 *  make a function out of it.
 *************************************************************************/
void processAccum(string &accumulator)
{
	//This is to shift a negative accumulator accurately
	//Seeing if the accum is over 1-000
	if(accumulator[4] == '0' )
	{
		if(accumulator[3] == '0')
		{
			if(accumulator[2] == '0')
			{
				if(accumulator[0] != '0')
				{
					accumulator = "1000";
				}
				else
				{
					accumulator = "0000";
				}
			}
		}
	}
}


/*************************************************************************
 * This function allows the code to accurately and efficiently process
 *  all 0 _ _ inputs. The function achieves this by first making sure that
 *  there is an input in the input card to retrieve. If there is a
 *  retrievable input from the input card the code will proceed to
 *  updating the IR. Then the code will take the string value of the main
 *  memory cell and converts it into an integer which will then be used as
 *  a temporary program counter. When the temporary program counter has
 *  been achieved the code simply inserts the string value of the input
 *  card into the main program memory cell.
 *************************************************************************/
void Input(string inputCard[], bool &valid, int &stepHolderInput,
		   int &pick, string &iR, string mainProgram[],
		   int &programCounter, int &result)
{
	//If the input card is empty
	if(inputCard[stepHolderInput] == "")
	{
		cout << "\nProgram Halted: Input Card is empty\n";
		valid = false;
		pick = -1;
		iR = mainProgram[programCounter];
		programCounter++;
	}
	else
	{
		//Clearing the string and setting IR to previous cell
		iR = "";
		iR = mainProgram[programCounter];


		//Converting the string convert into an int & saving it
		//into "result"
		istringstream stringToInt(mainProgram[programCounter]);
		stringToInt >> result;

		//This is where the code takes the "0##" & uses that info
		//to locate the proper main memory cell to input the value
		if(result != 0)
		{
			mainProgram[result] = inputCard[stepHolderInput];

			//Resets for next run
			stepHolderInput++;
			valid = true;
		}
		else
		{
			cout << "\nProgram Halted: Memory location being fetched "
					 "is <= zero\n";
			valid = false;
			pick = -1;
		}

		//Reset for potential next run.
		stringToInt.str("");
	}
}


/*************************************************************************
 * This function allows the code to accurately and efficiently print all
 *  the contents of every memory cell into an out file named "Save.txt".
 *  This functions role is to print the final contents of the entire
 *  simple computer emulator after the program has terminated, thus saving
 *  the final values for every part of the code. Unlike function
 *  "SaveToOption", this function executes automatically after the
 *  termination of the code & prints all the content of the emulator in
 *  a user friendly manner.
 *************************************************************************/
void SaveToSave(ostream &outFile, string iR, string mainProgram[],
				int programCounter, string inputCard[],
				string outputCard[], string accumulator)
{
	int holder;		//CALC	: Functions as a LCV.

	outFile << "Accumulator: " << accumulator;
	outFile << "\n\nIR: " << iR;
	outFile << "\n\nProgram Counter: " << setw(2) << setfill('0')
												  << programCounter;

	outFile << "\n\n\nMain Memory cells\n";
	outFile << "------------------";
	for(holder = 0; holder < 100; holder++)
	{
		//Saving all contents of memory for a user to look at.
		outFile << "\nCell #" << setw(2) << setfill('0') << holder << ": "
									     << mainProgram[holder];
	}

	outFile << "\n\n\nInput Card Cells\n";
	outFile << "----------------";
	for(holder = 0; holder < 15; holder++)
	{
		outFile << "\nCell #" << setw(2) << setfill('0') << holder + 1
										 << ": " << inputCard[holder];
	}

	outFile << "\n\n\nOutput Card Cells\n";
	outFile << "-----------------";
	for(holder = 0; holder < 15; holder++)
	{
		outFile << "\nCell #" << setw(2) << setfill('0') << holder + 1
									     << ": " << outputCard[holder];
	}
}


/*************************************************************************
 * This function allows the code to accurately and efficiently print all
 *  the contents of every memory cell into an out file named "Option.txt".
 *  Unlike function "SaveToFile", this function allows the user to save
 *  the memory of the entire simple computer at any time during run time.
 *  This allows the user to save a copy of the contents of all memory
 *  any time while the program is active. This functions main purpose
 *  is for the saved content of all memory to be saved in a fashion
 *  which the code can read from the saved text file back into the
 *  code, to then be executed. This function does not save the contents
 *  of all the memory if a user friendly manner. Rather, this function
 *  saves the content of all memory in a computer friendly manner.
 *************************************************************************/
void SaveToOption(ostream &loadoutFile, string iR, string mainProgram[],
				int programCounter, string inputCard[],
				string outputCard[], string accumulator)
{
	int holder;		//CALC	: Functions as a LCV.

	loadoutFile << accumulator << endl;
	loadoutFile << iR << endl;
	loadoutFile << programCounter << endl;

	for(holder = 0; holder < 100; holder++)
	{
		//Saving all contents of memory for a user to look at.
		loadoutFile << mainProgram[holder] << endl;
	}

	for(holder = 0; holder < 15; holder++)
	{
		loadoutFile << inputCard[holder] << endl;
	}

	for(holder = 0; holder < 15; holder++)
	{
		loadoutFile  << outputCard[holder] << endl;
	}

	cout << "\nSaved to file Option.txt\n";
}


/*************************************************************************
 * This function works in conjunction with function SaveToOption. This
 *  function allows the code to take the saved contents of all memory,
 *  regardless of what is currently in the memory, and save the values
 *  from the text file, accurately, into memory.
 *************************************************************************/
void LoadFromFile(ifstream &inFile, string mainProgram[],
				  string inputCard[], string outputCard[],
				  string &accumulator, string &iR, int &programCounter)
{
	int holder;

	getline(inFile, accumulator);
	getline(inFile, iR);
	inFile >> programCounter;
	inFile.ignore(1000,'\n');

	cout << "\nReading from file Option.txt!";

	//Grabbing the contents of the text file and placing the values into
	//main memory.
	for(holder = 0; holder < 99; holder++)
	{
		getline(inFile, mainProgram[holder]);
	}

	inFile.ignore(1000,'\n');

	//Grabbing the contents of the text file and placing the values into
	//the input card.
	for(holder = 0; holder < 14; holder++)
	{
		getline(inFile, inputCard[holder]);
	}
}
