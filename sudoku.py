from math import floor
from time import time

def timing(func):
    def wrapper(*arg, **kw):
        time_start = time()
        res = func(*arg, **kw)
        time_end = time()
        return (time_end - time_start), res, func.__name__
    return wrapper

board = [
[".", "7", ".", "5", ".", ".", ".", "1", "9"],
[".", ".", ".", "4", ".", "8", ".", ".", "."],
["3", ".", ".", ".", "1", ".", ".", "2", "."],
["7", ".", ".", ".", ".", ".", ".", ".", "8"],
[".", "4", ".", ".", "2", ".", ".", ".", "."],
[".", ".", "9", ".", ".", ".", ".", ".", "2"],
["2", ".", ".", "7", ".", ".", "9", "6", "1"],
[".", ".", ".", "2", ".", ".", ".", ".", "5"],
["5", "9", ".", ".", "6", ".", ".", "7", "."]
]

@timing
def solveSudoku(board):
    size = 9;
    boxSize = 3;
        
    def findEmpty(board):
        for r in range(0, size, 1):
            for c in range(0, size, 1):
                if board[r][c] == '.':
                    return [r,c]
        return None
    
    def validate(num, pos, board):
        r, c = pos
        
        #Check rows
        for i in range(0, size, 1):
            if board[i][c] == num and i != r:
                return False
        #Check cols
        for i in range(0, size, 1):
            if board[r][i] == num and i != c:
                return False
        
        #Check boxSize
        boxRow = floor(r/boxSize) * boxSize;
        boxCol = floor(c/boxSize) * boxSize;
        
        for i in range (boxRow, boxRow + boxSize):
            for j in range(boxCol, boxCol + boxSize):
                if board[i][j] == num and i != r and j != c:
                    return False
        
        return True
            
    def solve():
        currPos = findEmpty(board)
        
        if currPos == None:
            return True
        
        for i in range(1, size + 1, 1):
            currNum = str(i)
            isValid = validate(currNum, currPos, board)
            
            if isValid == True:
                x, y = currPos
                board[x][y] = currNum
                
                if solve():
                    return True
                
                board[x][y] = '.'
                
        return False
        
    solve();
    return board

print(solveSudoku(board), end = ' ')