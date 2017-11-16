#ifndef MYMAZESOLVER_H_
#define MYMAZESOLVER_H_

#include "MazeSolver.hpp"
#include "MazeSolution.hpp"
//#include "Direction.hpp"//in MazeSolution.hpp
#include "Maze.hpp"

//#include "MyHeader.hpp"
#include <iostream>//io stream
#include <iomanip>//io manipulation
#include <random>//std::random
#include <algorithm>//for random_shufle on vectors
#include <vector>//std::vector
#include <stack>//std::stack

//Creates source of entropy object
std::random_device deviceSolver;

//Seed the object
std::default_random_engine engineSolver{deviceSolver()};


class MyMazeSolver : public virtual MazeSolver
{

public:
	MyMazeSolver();
	virtual ~MyMazeSolver();
	virtual void solveMaze(const Maze& maze, MazeSolution& mazeSolution) override;

private:
	//Structure which is a single cell in the maze.
	//Contains the location of the cell on the maze.
	//Contains whether the cell has been visited.
	struct cell {
		int r;
		int c;
		bool visited;
	};
	//A std stack of cells. Will stack cells which have 
	//been visited.
	std::stack<cell> stackCells;
	//2D pointer to a pointer cell array which contains
	//all the cumulative cells.
	cell **cellMatrixPtr;
	//Used to contain all the valid directions the current
	//cell can travel to. The vector is shuffle and index
	//0 is returned.
	std::vector<Direction> randomChoice;

	//Used to hold a direction.
	Direction direction;
	//Gets the current pair of the mazeSolution object
	std::pair<int, int> currentCellPair;
	int rows;// = mazeSolution.getHeight();
	int cols;// = mazeSolution.getWidth();

	//Safely and fully deallocates the pointer to a pointer 2d array of cells.
	void cleanUpCellMatrixPtrs(cell **matrixCellPtr);

	//Helper function to help generate a positive bounded int.
	unsigned int generateRandomInt(int lowBound, int highBound);

	//Depth first recursive search maze solver algorithm
	void recursiveDepthFirstMazeSolver(const Maze& maze, cell **currentCell,
										  MazeSolution& mazeSolution,
										  int row, int col);

	//Determines if there are any valid cells to dig to.
	//As it determines which neighbor cells are valid, if any, 
	//function fills randomChoice vector with valid neighoboring
	//cell directions. Returns true if valid neighbor cells are present.
	bool validNeighbors(cell **matrixCellPtr,int row, int col, const Maze& maze);

	//Will return a random valid direction from randomChoice vector. 
	//randomChoice vector has only valid elements, all its elements are
	//shuffled and element 0 will be returned.
	Direction getDirectionToNeighbors();

	//Uses an int parameter to return the corresponding hard coded class enum
	//direction.
	Direction getDirection(int randomInt);
};




#endif /* MYMAZESOLVER_H_ */