#include<bits/stdc++.h>
#include <Windows.h>

using namespace std ;


char board[3][3] = 
    { 
        { ' ', ' ', ' ' }, 
        { ' ', ' ', ' ' }, 
        { ' ', ' ', ' ' } 
    }; 

int Move_row ,Move_coloumn ;

char player= 'X' , opponent = 'O';
// This function returns true if there are moves 
// remaining on the board. It returns false if 
// there are no moves left to play. 

bool isMovesLeft(char board[3][3]) 
{ 
    for (int i = 0; i<3; i++) 
        for (int j = 0; j<3; j++) 
            if (board[i][j]==' ') 
                return true; 
    return false; 
} 

// This is the evaluation function as discussed 
// in the previous article ( http://goo.gl/sJgv68 ) 

int evaluate(char b[3][3]) 
{ 
    // Checking for Rows for X or O victory. 
    for (int row = 0; row<3; row++) 
    { 
        if (b[row][0] == b[row][1] && b[row][1] == b[row][2]) 
        { 
            if (b[row][0]==player) 
                return +10; 
            else if (b[row][0]==opponent) 
                return -10; 
        } 
    } 
    // Checking for Columns for X or O victory. 
    for (int col = 0; col<3; col++) 
    { 
        if (b[0][col] == b[1][col] && b[1][col] == b[2][col]) 
        {
            if (b[0][col]==player) 
                return +10; 
            else if (b[0][col]==opponent) 
                return -10; 
        } 
    } 
    // Checking for Diagonals for X or O victory. 
    if (b[0][0]==b[1][1] && b[1][1]==b[2][2]) 
    { 
        if (b[0][0]==player) 
            return +10; 
        else if (b[0][0]==opponent) 
            return -10; 
    } 
    if (b[0][2]==b[1][1] && b[1][1]==b[2][0]) 
    { 
        if (b[0][2]==player) 
            return +10; 
        else if (b[0][2]==opponent) 
            return -10; 
    } 
    // Else if none of them have won then return 0 
    return 0; 
} 

// This is the minimax function. It considers all 
// the possible ways the game can go and returns 
// the value of the board 

int minimax(char board[3][3], int depth, bool isMax) 
{ 
    int score = evaluate(board); 
    // If Maximizer has won the game return his/her 
    // evaluated score 
    if (score == 10) 
        return score; 

    // If Minimizer has won the game return his/her 
    // evaluated score 
    if (score == -10) 
        return score; 

    // If there are no more moves and no winner then 
    // it is a tie 

    if (isMovesLeft(board)==false) 
        return 0; 

    // If this maximizer's move 
    if (isMax) 
    { 

        int best = -1000; 
        // Traverse all cells 
        for (int i = 0; i<3; i++) 
        { 
            for (int j = 0; j<3; j++) 
            { 
                // Check if cell is empty 
                if (board[i][j]==' ') 
                { 
                    // Make the move 

                    board[i][j] = player; 
                    // Call minimax recursively and choose 
                    // the maximum value 

                    best = max( best, minimax(board, depth+1, !isMax) ); 

                    // Undo the move 
                    board[i][j] = ' '; 
                } 
            } 
        } 
        return best; 
    } 

  

    // If this minimizer's move 

    else
    { 
        int best = 1000; 
        // Traverse all cells 
        for (int i = 0; i<3; i++) 
        { 
            for (int j = 0; j<3; j++) 
            { 
                // Check if cell is empty 
                if (board[i][j]==' ') 
                { 
                    // Make the move 
                    board[i][j] = opponent; 

                    // Call minimax recursively and choose 
                    // the minimum value 
                    best = min(best, minimax(board, depth+1, !isMax)); 
                    // Undo the move 
                    board[i][j] = ' '; 
                } 
            } 
        } 
        return best; 
    } 
} 
// This will return the best possible move for the player 

void findBestMove(char board[3][3]) 
{ 
    int bestVal = -1000;  
    Move_row = -1 ;
    Move_coloumn = -1 ;

    // Traverse all cells, evaluate minimax function for 
    // all empty cells. And return the cell with optimal 
    // value. 

    for (int i = 0; i<3; i++) 
    { 
        for (int j = 0; j<3; j++) 
        { 
            // Check if cell is empty 
            if (board[i][j]==' ') 
            { 
                // Make the move 
                board[i][j] = player; 
                // compute evaluation function for this 
                // move. 
                int moveVal = minimax(board, 0, false); 
                
                // Undo the move 
                board[i][j] = ' '; 
                
                // If the value of the current move is 
                // more than the best value, then update 
                // best/ 

                if (moveVal > bestVal) 
                { 
                    Move_row = i; 
                    Move_coloumn = j; 
                    bestVal = moveVal; 
                } 
            } 
        } 
    } 
    //printf("The value of the best Move is : %d\n\n", bestVal); 
    
} 




void printBoard(char board[3][3] )
{
    cout << " " <<board[0][0] << " | " << board[0][1] << " | " << board[0][2] <<endl ;
    cout << "---+---+---" << endl ;
    cout << " " <<board[1][0] << " | " << board[1][1] << " | " << board[1][2] <<endl ;
    cout << "---+---+---" <<endl ;
    cout << " " <<board[2][0] << " | " << board[2][1] << " | " << board[2][2] <<endl ;

}
char turn = 'O' ;
void getting_input(int x)
{
    switch (x)
    {
    case 1:
        board[0][0] = turn ;
        break;
    case 2:
        board[0][1] = turn ;
        break;
    case 3:
        board[0][2] = turn ;
        break;
    case 4:
        board[1][0] = turn ;
        break;
    case 5:
        board[1][1] = turn ;
        break;
    case 6:
        board[1][2] = turn ;
        break;
    case 7:
        board[2][0] = turn ;
        break;
    case 8:
        board[2][1] = turn ;
        break;
    case 9:
        board[2][2] = turn ;
        break;
    default:
        break;
    }
}






int main()
{
    cout << "--------Welcome to the Tic Tac Toe game --------" <<endl ;
    cout << "\n\nPostions for The board :\n" ;
    cout << " 1 | 2 | 3 \n---+---+---\n 4 | 5 | 6 \n---+---+---\n 7 | 8 | 9 \n\n" ;
    

    

    int winner = 0 ;//by default draw

    for(int i = 1 ; i <= 9 ;i++)
    {
        printBoard(board) ;
        int x(0) ;
        if( i%2 == 1 )
        {
            cout << "\nPlayer 1 turn.\nPlease select a position\n";
            int x ;
            cin >> x ;
            getting_input(x);
            
            //cin >> x >> y;
            //board[x][y] = turn ;
        }
        else 
        {    
            //cout << "AI's turn.\nPlease select a position\n";
            cout << "\nAI is thinking.......\n" ;
            Sleep(3000) ;//sleeping for 3 sec
            
            findBestMove(board);
            //cout << x <<endl ;
            
            board[Move_row][Move_coloumn] = turn ;
            
        }
        x = evaluate(board) ;
         if(x == 10)
            {
                winner = 1 ;
                break ;//for AI
            }
            else if(x == -10)
            {
                winner = 2 ;
                break ;//for player 
            }
        if (turn == 'X')
                turn = 'O' ;
            else
                turn = 'X' ;

        
    }
        printBoard(board) ;
        if(winner == 0)
        {
            cout << "Its a draw . Still you cant beat me\n" ;
        }
        else if(winner == 1 )
        {
            cout << "AI won\n" ;
        }
        else cout << "Player won\n" ;
    printf("------Game Over------") ;

    return 0 ;
}




