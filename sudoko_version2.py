# why the 2nd version is better?Because its recursion can be stopped when an ans is 
# first discovered among many answers

mat = list()

mat = [[5,1,7,6,0,0,0,3,4],
        [2,8,9,0,0,4,0,0,0],
        [3,4,6,2,0,5,0,9,0],
        [6,0,2,0,0,0,0,1,0],
        [0,3,8,0,0,6,0,4,7],
        [0,0,0,0,0,0,0,0,0],
        [0,9,0,0,0,0,0,7,8],
        [7,0,3,4,0,0,5,6,0],
        [0,0,0,0,0,0,0,0,0]]



def findNextCellToFill(mat, i, j):
    for x in range(i,9):
        for y in range(j,9):
            if mat[x][y] == 0:
                return x,y
    for x in range(0,9):
        for y in range(0,9):
                if mat[x][y] == 0:
                    return x,y
        
    # inorder to stop the other recursion
    # here it means that every thing is filled
    return -1,-1


# for checking the valdity
def isValid(mat, i, j, e):
    rowOk = all([e != mat[i][x] for x in range(9)])
    if rowOk:
        columnOk = all([e != mat[x][j] for x in range(9)])
        if columnOk:
            # finding the top left x,y co-ordinates of the section containing the i,j cell
            secTopX, secTopY = 3 *(i//3), 3 *(j//3) #floored quotient should be used here. 
            for x in range(secTopX, secTopX+3):
                for y in range(secTopY, secTopY+3):
                    if mat[x][y] == e:
                        return False
            return True
    return False
    
    
       

def solveSudoku(mat, i=0, j=0):
    i,j = findNextCellToFill(mat, i, j)
    if i == -1:
        return True
    for e in range(1,10):
        if isValid(mat,i,j,e):
            mat[i][j] = e
            if solveSudoku(mat, i, j):
                return True
            # Undo the current cell for backtracking
            mat[i][j] = 0
    return False




solveSudoku(mat)

for i in range(9):
    print(mat[i])