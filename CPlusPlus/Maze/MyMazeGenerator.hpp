#ifndef MYMAZEGENERATOR_H_
#define MYMAZEGENERATOR_H_

#include "MazeGenerator.hpp"
#include "Direction.hpp"
#include "Maze.hpp"
//#include "MyHeader.hpp"
#include <iostream>//io stream
#include <iomanip>//io manipulation
#include <random>//std::random
#include <algorithm>//for random_shufle on vectors
#include <vector>//std::vector
#include <stack>//std::stack

//Creates source of entropy object
std::random_device device;

//Seed the object
std::default_random_engine engine{device()};


class MyMazeGenerator : public virtual MazeGenerator
{
	public:
		MyMazeGenerator();
		virtual ~MyMazeGenerator();
		virtual void generateMaze(Maze& maze) override;


	private:

		//Structure which is a single cell in the maze.
		//Contains the location of the cell on the maze.
		//Contains whether the cell has been visited.
		struct cell {
			bool visited;
			int r;
			int c;
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
		//Total rows on the cell array
		int rows;
		//Total columns on the cell array
		int cols;

		//The recursive depth first maze generator algorithm
		void recursiveDepthFirstMazeGenerator(Maze& maze, cell **currentCell, 
											  int row, int col);

		//Helper function to help generate a positive bounded int.
		unsigned int generateRandomInt(int lowBound, int highBound);

		//Uses an int parameter to return the corresponding hard coded class enum
		//direction.
		Direction getDirection(int randomInt);

		//Safely and fully deallocates the pointer to a pointer 2d array of cells.
		void cleanUpCellMatrixPtrs(cell **matrixCellPtr);

		//Determines if there are any valid cells to dig to.
		//As it determines which neighbor cells are valid, if any, 
		//function fills randomChoice vector with valid neighoboring
		//cell directions. Returns true if valid neighbor cells are present.
		bool validNeighbors(cell **matrixCellPtr,int row, int col);

		//Will return a random valid direction from randomChoice vector. 
		//randomChoice vector has only valid elements, all its elements are
		//shuffled and element 0 will be returned.
		Direction getDirectionToNeighbors();
		
		//Updates the row and col indexes 
		void newRowCols(int &row, int &col, Direction direction);

};

#endif /* MYMAZEGENERATOR_H_ */