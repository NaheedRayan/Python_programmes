
mat = list() 


# This is a sudoko and we will solve it
mat =  [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]



# a function for testing weather it is possible to input a value n
def possible(x,y,n):
    # for checking the coloumn
    for i in range(9):
        if mat[x][i] == n :
            return False

    # for checking the row
    for i in range(9):
        if mat[i][y] == n :
            return False

    # now for checking the grid
    x0 = (x//3)*3
    y0 = (y//3)*3
    for coloumn in range(3):
        for row in range(3):
            if mat[x0 + row][y0 + coloumn] == n:
                return False

    # if none of this happens it returns true
    return True


# print(possible(8,2,6))


# now a recursive function for solving
def solve():
    for row in range(9):
        for coloumn in range(9):
            if mat[row][coloumn] == 0:
                for n in range(1 ,10):
                    if possible(row ,coloumn , n ) == True:
                        mat[row][coloumn] = n 
                        # here we will call the solve again
                        solve()
                        # what if its not valid then it will backtrack
                        mat[row][coloumn] = 0
                        
                return
    printing_the_mat()
    input("want more?")


# for printing the matrix
def printing_the_mat():
    for l in mat:
        print(l)



solve()

