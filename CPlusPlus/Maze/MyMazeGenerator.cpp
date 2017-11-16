#include <ics46/factory/DynamicFactory.hpp>
#include "MyMazeGenerator.hpp"

ICS46_DYNAMIC_FACTORY_REGISTER(MazeGenerator, MyMazeGenerator, "My Maze Generator (Required)");


//Default constructor
MyMazeGenerator::MyMazeGenerator()
{
	rows = 0;
	cols = 0;
	cellMatrixPtr = NULL;
}

//Default destructor
MyMazeGenerator::~MyMazeGenerator() {cleanUpCellMatrixPtrs(cellMatrixPtr);}

void MyMazeGenerator::generateMaze(Maze& maze) {
	maze.addAllWalls(); 

	rows = maze.getHeight();
	cols = maze.getWidth();

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

	recursiveDepthFirstMazeGenerator(maze, cellMatrixPtr, 
									 generateRandomInt(0,rows-1), 
									 generateRandomInt(0,cols-1));
}


void MyMazeGenerator::recursiveDepthFirstMazeGenerator(Maze& maze, 
													   cell **currentCell,
													   int row, int col) {
	currentCell[row][col].visited = true;

	while(validNeighbors(currentCell,row, col))
	{
		//Push cell onto the stack which has just been visited.	
		stackCells.push(currentCell[row][col]);
		//Check neighbor cells & return a random direction from 
		//among the neighbors who have not been visited.
		direction = getDirectionToNeighbors();
		//Remove the wall between the current cell & the next cell
		maze.removeWall(col, row, direction);
		//Helper function to update the row and col numbers to the next cell.
		newRowCols(row, col, direction);
		//Clear the random vector : holds all the eligable directions.
		randomChoice.clear();

		recursiveDepthFirstMazeGenerator(maze, currentCell, row, col);
	}

	//The function reaches this part of code when there are no valid
	//neighbor cells to dig to. Commence process to go back cells until
	//we find one that has valid neighbors.
	if(stackCells.size() > 0)
	{	
		//Retrieve the popped cells location.
		row = stackCells.top().r;
		col = stackCells.top().c;
		//Pop cell.
		stackCells.pop();
	}
	else{return({});}
}

//Allows row & col to be updated to correspond with the passed
//direction. Returns both row & col.
void MyMazeGenerator::newRowCols(int &row, int &col, Direction direction)
{
	switch(direction)
	{
		case Direction::up : row--;//up
		break;
		case Direction::down : row++;//down
		break;
		case Direction::left: col--;//left
		break;
		default: col++;//right
		break;
	}
}


//Will return a random valid direction from randomChoice vector. 
//randomChoice vector has only valid elements, all its elements are
//shuffled and element 0 will be returned.
Direction MyMazeGenerator::getDirectionToNeighbors()
{	
	std::random_shuffle(randomChoice.begin(), randomChoice.end());

	return(randomChoice[0]);
}


//Determines if there are any valid cells to dig to.
//As it determines which neighbor cells are valid, if any, 
//function fills randomChoice vector with valid neighoboring
//cell directions. Returns true if valid neighbor cells are present.
bool MyMazeGenerator::validNeighbors(cell **matrixCellPtr, int row, int col)
{
	bool up, down, left, right;
	up = false;
	down = false;
	right = false;
	left = false;

	//This set of code only determines out of bounds and does not check 
	//whether the cell has been visited.
	//If a direction is out of bounds that direction will equal false,
	//meaning not a valid direction route.
	up = (row > 0) ? true : false; //[row-1][col]
	down = (row < rows-1) ? true : false; //[row+1][col]
	left = (col > 0) ? true : false; //[row][col-1]
	right = (col < cols -1) ? true : false;//[row][col+1]


	//This code takes the infomation gained from above. 
	//If the location is valid, check whether the possible
	//next cell has already been visited.
	if(up)
	{	
		if(matrixCellPtr[row-1][col].visited == false)
		{
			//Possible next cell is within bounds & has not
			//been visited. Add it to the vector.
			randomChoice.push_back(getDirection(0));
		}
		else
		{
			//The move is no longer valid if already visited
			up = false;
		}
	}

	if(down)
	{	
		if(matrixCellPtr[row+1][col].visited == false)
		{
			randomChoice.push_back(getDirection(1));
		}
		else
		{
			down = false;//The move is no longer valid if already visited
		}
	}

	if(left)
	{	
		if(matrixCellPtr[row][col-1].visited == false)
		{
			randomChoice.push_back(getDirection(2));
		}
		else
		{
			left = false;
		}
	}

	if(right)
	{	
		if(matrixCellPtr[row][col+1].visited == false)
		{
			randomChoice.push_back(getDirection(3));
		}
		else
		{
			right = false;
		}
	}

	//If any neighbor cell is valid = ? true : false 
	return(up|down|left|right);
}


//Helper function to help generate any positive random number from 
//parameters
unsigned int MyMazeGenerator::generateRandomInt(int lowBound, int highBound) 
{
	//Distirbution of selected value. 
	std::uniform_int_distribution<int> distribution{lowBound, highBound};
	//Return random selection.
	return (distribution(engine));
}


//Uses an int parameter to return the corresponding hard coded class enum
//direction.
Direction MyMazeGenerator::getDirection(int randomInt) { 

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

void MyMazeGenerator::cleanUpCellMatrixPtrs(cell **matrixCellPtr)
{
	for(int i{0}; i < rows; i++) {delete [] matrixCellPtr[i];}
	delete [] matrixCellPtr;
}	
