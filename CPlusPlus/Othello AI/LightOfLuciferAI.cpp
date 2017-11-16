#include <ics46/factory/DynamicFactory.hpp>
#include "LightOfLuciferAI.hpp"

ICS46_DYNAMIC_FACTORY_REGISTER(OthelloAI, lfescoba::LightOfLuciferAI, "LightOfLuciferAI(Required)");

lfescoba::LightOfLuciferAI::LightOfLuciferAI()
{
	tempMax = 0;
	tempMin = 0;
	validMoveRootIndex = 0;
	maxDepth = 0;
	score = 0;
	max = 0;
	min = 0;
	rows = 0;
	cols = 0;
	colorToken = false;//FALSE = BLACK | TRUE = WHITE
	colorTokenTrigger = false;//NOT TRIGGERED
	searchToken = true;
}

//Chooses a move for the AI from the current game state from its returned value.
std::pair<int, int> lfescoba::LightOfLuciferAI::chooseMove(const OthelloGameState& state)
{	
	rows = state.board().height();
	cols = state.board().width();
	max = 0;
	min = 0;
	int result = 0;
	int depth = 3;
	maxDepth = depth;

	// Get board root
	std::unique_ptr<OthelloGameState> clone = state.clone(); 
	// Gets the passed in clones' possible nodes.
	GetValidMoves(clone, validMovesRoot);

	//One time trigger to identify the color of the AI.
	if(!colorTokenTrigger)
	{	
		//This allows the code to identify which color it is. 
		//If there are an even amonut of chips on the board it is black.
		//Else white.
		int totalScore = state.whiteScore() + state.blackScore();
		colorTokenTrigger = !colorTokenTrigger;

		//If there are an even amounts of chips on the board its blacks turn.
		//If there are an odd amounts of chips on the board its whites turn.
		//The color token is never changed again.
		//(False|0) = AI is BLACK && (True|1) = AI is WHITE
		if(totalScore%2 == 1) {colorToken = true;}
	}

	//Its the AIs turn if code is here.
	searchToken = true;

	//Get a current game state root
	std::unique_ptr<OthelloGameState> cloneTemp = state.clone();

	//ENTER RECURSIVE FUNCTION HERE 
	result = search(cloneTemp, depth, searchToken);

	//Make a move om the current game state.
	return(std::make_pair(validMovesRoot[result].second, validMovesRoot[result].first));
}


//Recursive depth-first run-time stack tree search.
//Uses the run-time stack of store clones of game states.
//The maximum amount of nodes stored on the run-time stack is equal to the 
//depth passed in. Each game state clone generates only the portion of the game
//tree necessary to make a heaurisic search possible. Goes depth levels deep.
//The search token is used to swap whos turn it is, as the function continues 
//to find the best node selection for itself. 
int lfescoba::LightOfLuciferAI::search(std::unique_ptr<OthelloGameState>& clone, 
					int depth,  bool searchToken)
{	//Local variables.
	std::unique_ptr<OthelloGameState> cloneTemp = clone->clone();
	std::unique_ptr<OthelloGameState> cloneMakeMove = clone->clone();

	//The search has reached its deepest level.
	if(depth == 0)
	{
		score = evaluation(clone, depth, searchToken);
		return(score);
	}
	else
	{	//The searchToken will always be true by default on 1st run since this
		//function can only be called on AI's turn from chooseMove().
		//After the 1st run the searchToken will negate itself to simulate
		//taking turns between an AI and its opponent.
		if(searchToken)
		{
			//Will hold all sub-trees of a clone game state root.
			std::vector<std::pair<int, int>> validMoves;
			//Passes in a vector and the current game state root.
			//"Gathers" all the subtrees of the root.
			GetValidMoves(cloneTemp, validMoves);
			//Is used to store all the max scores from final 
			//game states.
			std::vector<int> maxVector;
			//Allows to visit each leaf within each subtree of the clones root
			std::vector<std::pair<int, int>>::iterator i = validMoves.begin();

			//While there are still final game states to score.
			while(i != validMoves.end())
			{	//Proceed with the game state by maing a move.
				cloneMakeMove->makeMove(*&(i->second), *&(i->first));
				//Inc the iterator.
				++i;

				//Captures the returned score.
				int returnedMax = 0;

				//Returns an evaluation score & is the recursive call.
				//Will allow an AI to recursively search depth levels deep
				//of a game tree from the clones current game state root.
				//Will flip the search Token.
				returnedMax = search(cloneMakeMove, depth - 1, !(searchToken));

				//Push score onto the vector.
				maxVector.push_back(returnedMax);

				//Iterator the game state to the previous game state.
				//At this point the recursive call has returned 
				//and we are looking for nodes on cloneTemp->clone()s
				//game state, cloneTemp is on the run-time stack.
				cloneMakeMove = cloneTemp->clone();
			}

			//Will return the index of the largest score.
			validMoveRootIndex = 0;
			max = 0;

			//Wil find the max score from maxVector.
			for(int maxIndex = 0; maxIndex < maxVector.size(); maxIndex++)
			{	
				if(max < maxVector[maxIndex])
				{
					max = maxVector[maxIndex];
					//Set the index to the max score.
					validMoveRootIndex = maxIndex;
				}
			}
			//Return the index of the max score. This will be used
			//with vector validMovesRoot to obtain the next move
			//to make for the best possible score.
			return validMoveRootIndex;
		}
		//Simulate an opponents turn.
		else// ((searchToken == False) || (!searchToken)) ~ illustration
		{
			//Will hold all sub-trees of a clone game state root.
			std::vector<std::pair<int, int>> opponentValidMoves;
			//Passes in the vector and the current game state root.
			//"Gathers" all the subtrees of the root.
			GetValidMoves(clone, opponentValidMoves);
			//Is used to store all the min scores from final 
			//game states.
			std::vector<int> minVector;
			//Allows to visit each leaf within each subtree of the clones root
			std::vector<std::pair<int, int>>::iterator i = opponentValidMoves.begin();

			//While there are still final game states to score.
			while(i != opponentValidMoves.end())
			{	//Proceed with the game state by maing a move.
				cloneMakeMove->makeMove(*&(i->second), *&(i->first));

				//Inc the iterator.
				++i;			

				//Captures the returned score.
				int returnedMin = 0;

				//Returns an evaluation score & is the recursive call.
				//Will allow an AI to recursively search depth levels deep
				//of a game tree from the clones current game state root.
				returnedMin = search(cloneMakeMove, depth - 1, !(searchToken));
				
				//Push score onto the vector.
				minVector.push_back(returnedMin);

				//Iterator the game state to the previous game state.
				//At this point the recursive call has returned 
				//and we are looking for nodes on cloneTemp->clone()s
				//game state, cloneTemp is on the run-time stack.
				cloneMakeMove = cloneTemp->clone();
			}

			//Will return the index of the smallest score.
			validMoveRootIndex = 0;
			min = 0;

			//Wil find the min score from minVector.
			for(int minIndex = 0; minIndex < minVector.size(); minIndex++)
			{	
				if(min > minVector[minIndex])
				{	
					min = minVector[minIndex];
					//Set the index to the min score.
					validMoveRootIndex = minIndex;
				}
			}
			//Return the index of the max score. This will be used
			//with vector validMovesRoot to obtain the next move
			//to make for the best possible score.
			return validMoveRootIndex;
		}
	}
}

//Simply helps to obtain all the sub-tree nodes of the passed in clone and
//returns the information in a pair vector.
void lfescoba::LightOfLuciferAI::GetValidMoves(std::unique_ptr<OthelloGameState>& clone,
							std::vector<std::pair<int, int>>& validMoves)
{
	int rowIndex;
	int colIndex;
	validMoves.clear();

	for(rowIndex = 0; rowIndex < rows; rowIndex++)
	{
		for(colIndex = 0; colIndex < cols; colIndex++)
		{
			if(clone->isValidMove(colIndex, rowIndex))
			{
				//No need for std::make_pair if emaplce is used. Here for ref only
				//Would need for pushback.
				validMoves.emplace_back(std::make_pair(rowIndex, colIndex));
			}
		}
	}
}

//The most simply evalution possible.
//eval(state) = number of tiles belonging to me - number of times belonging
//to my opponent.
int lfescoba::LightOfLuciferAI::evaluation(const std::unique_ptr<OthelloGameState>& clone, const int depth, 
 				   		const bool searchToken)
{
	tempMax = 0;
	tempMin = 0;

	//~~Useful notes to keep in mind for the evaluation of the best score.~~
	//If the search token == False then that means that 
	//the AI player just made a move.
	//If the search token == True then that means that 
	//the Opponent player just made a move.
	//The color token is never changed after it has been initialized.
	//(False|0) = AI is BLACK && (True|1) = AI is WHITE

	//If the search token == False then that means that 
	//the AI player made the last move
	if(searchToken == false)
	{	
		//If the color token is False then that means that
		//the AI player is the black players.
		if(colorToken == false)
		{	//If code is in here then the AI is black
			tempMax = clone->blackScore();
			tempMin = clone->whiteScore();
			return(tempMax-tempMin);
		}
		//Else the AI player is the white player.
		else
		{	//If code is in here then the AI is white
			tempMax = clone->whiteScore();
			tempMin = clone->blackScore();
			return(tempMax-tempMin);
		}
	}
	//Else the Opponent made the last move.	
	else
	{	//~~We have to be careful here.~~
		//What we are doing is helping the AI make the best choice for 
		//itself. The opponent has just made the last move. What we are 
		//doing is helping the AI choose the best route forward from the
		//original game state root. Therefore, we only need to return the
		//AI color score. The higher it is, the more chips the AI has on
		//the board.

		//If the color token is False then that means that
		//the Opponent player is the black players. Therefore, 
		//send the white score to help AI choose its best route.
		if(colorToken == false)
		{	//If code is in here then the Opponent is black
			tempMin = clone->whiteScore();
			return(tempMin);
		}
		//Else the Opponent player is the white player. Therefore,
		//send blacks score to help AI choose its best route.
		else
		{	//If code is in here then the Opponent is white
			tempMin = clone->blackScore();
			return(tempMin);
		}
	}
}


