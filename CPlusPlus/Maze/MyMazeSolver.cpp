#include <ics46/factory/DynamicFactory.hpp>
#include "MyMazeSolver.hpp"

ICS46_DYNAMIC_FACTORY_REGISTER(MazeSolver, MyMazeSolver, "My Maze Solver (Required)");


//Default constructor
MyMazeSolver::MyMazeSolver() {
	rows = 0;
	cols = 0;
	currentCellPair.first = 0;
	currentCellPair.second = 0;
	cellMatrixPtr = NULL;
}

//Default destructor
MyMazeSolver::~MyMazeSolver() {
	cleanUpCellMatrixPtrs(cellMatrixPtr);
}

//Provided method. Takes a const maze object and a referenced mazeSolution. 
//Those parameters are used to call the recursive depth first search function.
void MyMazeSolver::solveMaze(const Maze& maze, MazeSolution& mazeSolution) 
{
	rows = mazeSolution.getHeight();
	cols = mazeSolution.getWidth();
	currentCellPair = mazeSolution.getCurrentCell();


	//Declaring a 2D array of cell using pointers.
	//Declares an array of cell pointers to cell pointers
	cellMatrixPtr = new cell* [rows];

	//Loop through all the cell rows and assign them an array of 
	//cell of size cols
	for(int row{0}; row < rows; row++)
	{	
		//Creating a cell array of row x col
		cellMatrixPtr[row] = new cell[cols];

		//Default initilization for each cell
		for(int col{0}; col < cols; col++)
		{
			cellMatrixPtr[row][col].visited = false;
			cellMatrixPtr[row][col].r = row;
			cellMatrixPtr[row][col].c = col;
		}
	}

	//Calling the recursive function.
	recursiveDepthFirstMazeSolver(maze, cellMatrixPtr, mazeSolution, 0, 0);
}


//CLeans up the 2D pointer to a pointer maxtrix. This prevents any 
//memory leaks.
void MyMazeSolver::cleanUpCellMatrixPtrs(cell **matrixCellPtr)
{
	for(int i{0}; i < rows; i++) {delete [] matrixCellPtr[i];}
	delete [] matrixCellPtr;
}	


//Helper function to help generate any positive random number from 
//parameters
unsigned int MyMazeSolver::generateRandomInt(int lowBound, int highBound) 
{
	//Distirbution of selected value. 
	std::uniform_int_distribution<int> distributionSolver{lowBound, highBound};
	//Return random selection.
	return (distributionSolver(engineSolver));
}

//Recursive depth first maze solver algorithm.
void MyMazeSolver::recursiveDepthFirstMazeSolver(const Maze& maze, cell **currentCell,
								   MazeSolution& mazeSolution,
								   int row, int col)
{
	currentCell[row][col].visited = true;

	while(validNeighbors(currentCell,row, col, maze) && !(mazeSolution.isComplete()))
	{
		if(mazeSolution.isComplete()) {return({});}

		//Check neighbor cells & return a random direction from 
		//among the neighbors who have not been visited.
		direction = getDirectionToNeighbors();

		//Push cell onto the stack which has just been visited.	
		stackCells.push(currentCell[row][col]);

		//Extend the movement in the randomly selected direction.
		mazeSolution.extend(direction);

		//Update the new row & col indexes
		currentCellPair = mazeSolution.getCurrentCell();
		row = currentCellPair.second;
		col = currentCellPair.first;

		//Clear the random vector : holds all the eligable directions.
		randomChoice.clear();

		//Recursive call
		recursiveDepthFirstMazeSolver(maze, currentCell, mazeSolution, row, col);
	}

	if(mazeSolution.isComplete()) {return({});}

	//The function reaches this part of code when there are no valid
	//neighbor cells to dig to. Commence process to go back cells until
	//we find one that has valid neighbors.
	if(stackCells.size() > 0)
	{	
		//No viable cells to move to, therefore back up and update the
		//row & col indexes.
		mazeSolution.backUp();
		currentCellPair = mazeSolution.getCurrentCell();
		row = currentCellPair.second;
		col = currentCellPair.first;
	}
	else{return({});}
}


//Determines if there are any valid cells to dig to.
//As it determines which neighbor cells are valid, if any, 
//function fills randomChoice vector with valid neighoboring
//cell directions. Returns true if valid neighbor cells are present.
bool MyMazeSolver::validNeighbors(cell **matrixCellPtr, int row, int col, 
								  const Maze& maze)
{
	bool up, down, left, right;
	up = false;
	down = false;
	right = false;
	left = false;

	row = currentCellPair.second;
	col = currentCellPair.first;

	//This set of code only determines out of bounds and does not check 
	//whether the cell has been visited.
	//If a direction is out of bounds that direction will equal false,
	//meaning not a valid direction route.
	up = (row > 0) ? true : false; //[row-1][col]
	down = (row < rows-1) ? true : false; //[row+1][col]
	left = (col > 0) ? true : false; //[row][col-1]
	right = (col < cols -1) ? true : false;//[row][col+1]

	//This code takes the infomation gained from above. 
	//If the direction is valid, check whether the possible
	//next cell has already been visited.
	if(up)
	{	
		//If the cell has not been visited it may be a valid cell to jump to
		if(matrixCellPtr[row-1][col].visited == false)
		{
			//Check if there is a wall 
			if((maze.wallExists(col, row, Direction::up) == false))
			{
				//Possible next cell is within bounds & has not
				//been visited. Add it to the vector.
				randomChoice.push_back(getDirection(0));
			}
			else {up = false;}//Wall exists, therefore not a valid move
		}
		else {up = false;}//Cell has already been visited.
	}//End of determining if the up direction is valid.


	if(down)
	{	
		if(matrixCellPtr[row+1][col].visited == false)
		{
			//Check if there is a wall 
			if((maze.wallExists(col, row, Direction::down) == false))
			{
				//Possible next cell is within bounds & has not
				//been visited. Add it to the vector.
				randomChoice.push_back(getDirection(1));
			}
			else {down = false;}//Wall exists, therefore not a valid move
		}
		else {down = false;}//The move is no longer valid if already visited
	}


	if(left)
	{	
		if(matrixCellPtr[row][col-1].visited == false)
		{
			//Check if there is a wall 
			if((maze.wallExists(col, row, Direction::left) == false))
			{
				//Possible next cell is within bounds & has not
				//been visited. Add it to the vector.
				randomChoice.push_back(getDirection(2));
			}
			else {left = false;} //Wall exists, therefore not a valid move
		} 
		else {left = false;}
	}

	if(right)
	{	
		if(matrixCellPtr[row][col+1].visited == false)
		{
			//Check if there is a wall 
			if((maze.wallExists(col, row, Direction::right) == false))
			{
				//Possible next cell is within bounds & has not
				//been visited. Add it to the vector.
				randomChoice.push_back(getDirection(3));
			}
			else {right = false;}//Wall exists, therefore not a valid move
		}
		else {right = false;}
	}

	//If any neighbor cell is valid = ? true : false 
	return(up|down|left|right);
}

//Will return a random valid direction from randomChoice vector. 
//randomChoice vector has only valid elements, all its elements are
//shuffled and element 0 will be returned.
Direction MyMazeSolver::getDirectionToNeighbors()
{	
	std::random_shuffle(randomChoice.begin(), randomChoice.end());

	return(randomChoice[0]);
}

//Uses an int parameter to return the corresponding hard coded class enum
//direction.
Direction MyMazeSolver::getDirection(int randomInt) { 

	switch(randomInt)
	{
		case 0 : //std::cout << "\nup"; 
		return Direction::up;
		break;
		case 1: //std::cout << "\ndown"; 
		return Direction::down;
		break;
		case 2: //std::cout << "\nleft";
		return Direction::left;
		break;
		default : //std::cout << "\nright";
		return Direction::right;
		break;
	}
}