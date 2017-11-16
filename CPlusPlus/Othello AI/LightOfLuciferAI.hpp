#include "OthelloAI.hpp"//includes utility & memory
#include <iostream>		//io stream
#include <iomanip>		//io manipulation
#include <algorithm> 	//std::random_shuffle
#include <vector>		//std::vector
#include <stack> 		//std::stack


 namespace lfescoba
 {
 	class LightOfLuciferAI : public OthelloAI
 	{
 	public:
 		LightOfLuciferAI();
 		virtual std::pair<int, int> chooseMove(const OthelloGameState& state);

 	private:
 		unsigned int tempMax;
 		unsigned int tempMin;
 		unsigned int max;
 		unsigned int min;
 		unsigned int rows;
 		unsigned int cols;
 		//Holds a permant value of what the max depth is.
 		int maxDepth;
 		// Used to store & return (max-min)
 		int score;			
 		//This bool colorToken variable is used to determine the color of the AI. 
 		//False = black therefore true = white
 		bool colorToken;
 		//Used to help determine what color the AI is. 
 		//True = triggerered therefore False = untriggered
 		//Will only trigger once - when chooseMoves activates for the 1st time
 		bool colorTokenTrigger;
 		//Used to help the search function determine when its the AI's turn
 		//and when its the opponents turn.
 		//True = AI's turn therefore False = opponents turn
 		bool searchToken;
 		//Used to determine which of the indexes in validMovesRoot vector the AI
 		//should select.
 		int validMoveRootIndex;

 		//Holds all the possible valid moves of the current Othello Game State's root.
 		//Holds all possible nodes from root.
 		std::vector<std::pair<int, int>> validMovesRoot;

 		//Performs recursive depth-first searches of an Othello Gametree.
 		//Search goes depth levels deep.
 		int search(std::unique_ptr<OthelloGameState>& clone, int depth, 
 				   		bool searchToken);
 		//Is passed a current Othello Game State clone and returns by reference
 		//a vector pair of all the valid moves - or the next nodes down the tree.
 		void GetValidMoves(std::unique_ptr<OthelloGameState>& clone,
 						std::vector<std::pair<int, int>>& validMoves);

 		//Implemented the most basic evaluation - the one provided on the assignment.
 		//eval(state) = number of tiles belonging to me - number of times belonging
 		//to my opponent.
 		int evaluation(const std::unique_ptr<OthelloGameState>& clone, const int depth, 
 				   		const bool searchToken);

 	};
 }