board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def boardPrint(board): # this function is just used to print the board in a neat way
    for i in range(len(board)):
        if i % 3 == 0 and i != 0: # for every third line, it'll get spaced out
                print(" - - - - - - - - - - - - - ")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 8:
                print(" | ", end = "")
            if j == 8:
                print(str(board[i][j]) + " | ") # if the last int in the line is being printed we want to skip the line so end="" is not needed
            else:
                print(str(board[i][j]) + " ", end = "")


def findEmptyCell(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i, j) #these are then used as position in isValid function, returned as a tuple in form (row, col)
    
    return None


def isValid(board, num, position):
    #checking each individual number in column of the position we are inserting in
    for i in range(len(board)): 
        if board[position[0]][i] == num and position[1] != i:
            return False #if location of number is not the same that inserted in, then return false becasue its not valid then

    #checking each individual number in row of the position we are inserting in
    for i in range(len(board)): 
        if board[i][position[1]] == num and position[1] != i:
            return False #if location of number is not the same as that inserted in, then return false becasue its not valid then

    #checking each individual number in 3x3 box of the position we are inserting in
    boxRow = position[0] // 3 #integer division of row
    boxCol = position[1] // 3 #integer division of column  
    for i in range(boxRow*3, boxRow + 3):  # we do multiply 3 since from the integer division we get either 0, 1 or 2. Now multiplying by 3 will get us 0, 3, or 6 which will be the column location of the first integer in that box
        for j in range(boxCol*3, boxCol + 3): # same thing for this case however doing it here allows us to get the position of the row.
            if board[i][j] == num and (i, j) != position: 
                return False #if location of number is not the same that inserted in, then return false becasue its not valid then

    return True

def solveBoard(board):
    emptyCell = findEmptyCell(board)
    
    # findEmptyCell returns None when there are no more empty cells
    if emptyCell == None:
        return True
    else:
        row, column = emptyCell
        for i in range(1, 10): # iterating from 1-9, these will be inputs into the board
            if isValid(board, i, (row, column)) == True: #if that number is valid for that position, add it to that position
                board[row][column] = i
                if solveBoard(board) == True: # recursively call solveBoard once again, which will find the next empty cell and find a number for that which works
                    return True # returns True if that number works for that location
                else:
                    board[row][column] = 0 # if no solution is found, then the algorithm backtracks and resets the the position to 0 and tries the next number in the loop
        return False # when the function returns false it then backtracks to find the next possible number which can work in that position


if __name__ == "__main__":
    boardPrint(board)
    solveBoard(board)
    print("\n\n")
    boardPrint(board)