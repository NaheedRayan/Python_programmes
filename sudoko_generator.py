import random


mat = list()

mat = [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]


# this is for default value
def findNextCellToFill_no(mat):
    
    for x in range(0,9):
        for y in range(0,9):
                if mat[x][y] == 0:
                    return x,y
        
    # inorder to stop the other recursion
    # here it means that every thing is filled
    return -1,-1

# for 1st diaognal part
def findNextCellToFill_no1(mat):
    
    for x in range(0,3):
        for y in range(0,3):
                if mat[x][y] == 0:
                    return x,y
        
    # inorder to stop the other recursion
    # here it means that every thing is filled
    return -1,-1

# for 2nd diaognal part
def findNextCellToFill_no2(mat):
    
    for x in range(3,6):
        for y in range(3,6):
                if mat[x][y] == 0:
                    return x,y
        
    # inorder to stop the other recursion
    # here it means that every thing is filled
    return -1,-1

# for 3rd diaognal part
def findNextCellToFill_no3(mat):
    
    for x in range(6,9):
        for y in range(6,9):
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
    




def solveSudoku(mat , i = 0 , j = 0 , n = 0) :
    if n == 1 :
        i,j = findNextCellToFill_no1(mat)
    elif n == 2 :
        i,j = findNextCellToFill_no2(mat)
    elif n == 3:
        i,j = findNextCellToFill_no3(mat)
    elif n == 4:
        i,j = findNextCellToFill_no(mat)


    if i == -1:
        return True 
    for p in range(1,10):
        e = random.randrange(1,10)
        if isValid(mat,i,j,e):
            mat[i][j] = e
            if solveSudoku(mat, i, j,n):
                return True
            # Undo the current cell for backtracking
            mat[i][j] = 0
    return False
    

# for 1st diaognal part
solveSudoku(mat ,  0 ,  0 ,  1)
# for 2nd diaognal part 
solveSudoku(mat ,  0 ,  0 ,  2)
# for 3rd diaognal part 
solveSudoku(mat ,  0 ,  0 ,  3)
# this is for solving the whole 
solveSudoku(mat ,  0 ,  0 ,  4) 

# solveSudoku(mat)

for i in range(9):
    print(mat[i])