# Background:  in Chess, a King can move from any square to
# any adjacent square.  A King’s Tour is a series of legal King
# moves so that every square is visited exactly once. 
# We can represent a Kings Tour in a 2d list where the 
# numbers represent the order the squares are visited, going 
# from 1 to N2.  For example, consider these 2d lists:

#    [ [  3, 2, 1 ],    	[ [  1, 2, 3 ],  	[ [ 3, 2, 1 ],
#  	[  6, 4, 9 ],      	[  7, 4, 8 ],    	[ 6, 4, 0 ],
#  	[  5, 7, 8 ] ]     	[  6, 5, 9 ] ]   	[ 5, 7, 8 ] ]

# The first is a legal Kings Tour but the second is not, 
# because there is no way to legally move from the 7 to the 8, 
# and the third is not, because it contains a 0 which is out
#  of range.  With this in mind, write the function 
# isKingsTour(board) that takes a 2d list of integers, 
# which you may assume is NxN for some N>0, and 
# returns True if it represents a legal Kings Tour 
# and False otherwise.
def knightsTour(l, rows, cols):
    row = len(l)
    col = len(l[0])
    if (l[(rows+1) % row][(cols+1) % col] == l[rows][cols]+1) or (l[(rows+1) % row][abs(cols-1) % col] == l[rows][cols]+1) or (l[abs(rows-1) % row][abs(cols+1) % col] == l[rows][cols]+1) or (l[(rows+1) % row][(cols-1) % col] == l[rows][cols]+1) or (l[(rows) % row][abs(cols-1) % col] == l[rows][cols]+1) or(l[abs(rows) % row][(cols+1) % col] == l[rows][cols]+1) or (l[abs(rows-1) % row][abs(cols) % col] == l[rows][cols]+1) or (l[abs(rows+1) % row][(cols) % col] == l[rows][cols]+1):
        return True
    return False
def isKingsTour(board):
    # Your code goes here...
        # Your code goes here...
    for i in range(len(board)*len(board[0])):
        for j in range(len(board)):
            for k in range(len(board[0])):
                if i == board[j][k]:
                    if not knightsTour(board, j, k):
                        return False
    return True

assert(isKingsTour([[3,2,1],[6,4,9],[5,7,8]]))==True
assert(isKingsTour([[1,2,3],[7,4,8],[6,5,9]]))==False
assert(isKingsTour([[3,2,1],[6,4,0],[5,7,8]]))==False
print("ALL Test cases Passed")
#    [ [  3, 2, 1 ],    	[ [  1, 2, 3 ],  	[ [ 3, 2, 1 ],
#  	[  6, 4, 9 ],      	[  7, 4, 8 ],    	[ 6, 4, 0 ],
#  	[  5, 7, 8 ] ]     	[  6, 5, 9 ] ]   	[ 5, 7, 8 ] ]