import pygame,os
from pygame.locals import *
import time
import random



# for creating the window at center
os.environ['SDL_VIDEO_CENTERED'] = '1'

size = 660, 800
width, height = size
GREEN = (50, 255, 50)
DARK_GREEN = (0, 150, 0)
WHITE = (255 , 255 , 255)
ORANGE = (242, 130, 2)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (191, 85, 236)
BLACK = (0,0,0)

pygame.init()
screen = pygame.display.set_mode(size)
running = True

mousex = 0 # used to store x coordinate of mouse event
mousey = 0 # used to store y coordinate of mouse event


# This is a empty sudoko and we will generate it
mat =  [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]

# this matrix is temporary
temp_mat = [[0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]]





# making a list of squares(rect)
list_of_rect = list() 
for i in range(60,541,60):
        for j in range(60,541,60):
            rect = Rect(j,i,60,60)
            list_of_rect.append(rect)

# print(list_of_rect)

# setting the color of the screen
screen.fill(WHITE)
pygame.display.update()

# for creating the sudoku text
font = pygame.font.SysFont("Arial Black", 24)
img = font.render('Sudoku', True, PURPLE)
screen.blit(img, (280, 20))
pygame.display.update()

# for creating the name text
font = pygame.font.SysFont("Arial Black", 16)
img = font.render('Made by Naheed Rayan', True, BLACK)
screen.blit(img, (225, 770))
pygame.display.update()


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
            secTopX, secTopY = 3 *(i//3), 3 *(j//3) #flooORANGE quotient should be used here. 
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
    
# here we are populating the board
# for 1st diaognal part
solveSudoku(mat ,  0 ,  0 ,  1)
# for 2nd diaognal part 
solveSudoku(mat ,  0 ,  0 ,  2)
# for 3rd diaognal part 
solveSudoku(mat ,  0 ,  0 ,  3)
# this is for solving the whole 
solveSudoku(mat ,  0 ,  0 ,  4) 


# printing the matrix
def printing(mat):
    for i in range(9):
        print(mat[i])

printing(mat)
print("\n")


# now removing items from the temp matrix
cnt = 0 
b = True 
while(b):
    x = random.randint(0,8)
    y = random.randint(0,8)

    if cnt == 35:
        b = False
    if temp_mat[x][y] == 0 :
        cnt+=1
        temp_mat[x][y] = mat[x][y]

printing(temp_mat)
    




# for printing the populated board
def populated_board():
    for i in range(9):
        for j in range(9):
            if temp_mat[i][j] != 0:
                font = pygame.font.SysFont(None, 35)
                img = font.render(str(temp_mat[i][j]), True, BLUE)
                screen.blit(img, (((j+1)*60) +20, ((i+1)*60)+20))
                pygame.display.update()
# # printing the populated board
populated_board() 


# for the submit button
def submit_button():
    # rect_m = Rect(420,660,120,60)
    rect_m = Rect(240,660,180,60)
    pygame.draw.rect(screen, DARK_GREEN, rect_m, 0)

    # submit text
    font = pygame.font.SysFont(None, 35)
    img = font.render(' Submit', True, WHITE)
    screen.blit(img, (rect_m.left +40, rect_m.top+16))
    pygame.display.update()

submit_button()



screen_refreshing = True

# the running loop
while running:
    # if the quit is clicked
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        # if mouse is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            # if its inside the boundary of the submit button  then it will work
            if(mousex >= 660 and mousex <= 660 and mousey >= 240 and mousey <= 360):
                rect_m = Rect(240,660,180,60)
                pygame.draw.rect(screen, GREEN, rect_m, 0)
                # submit text
                font = pygame.font.SysFont(None, 35)
                img = font.render(' Submit', True, WHITE)
                screen.blit(img, (rect_m.left +40, rect_m.top+16))
                pygame.display.update()


                # this is for the win and lose box
                rect_win_lose = Rect(30,240,600,240)
                if(mat == temp_mat):
                    print("Winner")
                    pygame.draw.rect(screen, GREEN, rect_win_lose, 0)
                    pygame.display.update()
                    screen_refreshing = False 

                    font = pygame.font.SysFont(None, 100)
                    img = font.render(' You WIN .', True, WHITE)
                    screen.blit(img, (rect_win_lose.left +110, rect_win_lose.top+60))
                    pygame.display.update()

                    font = pygame.font.SysFont(None, 50)
                    img = font.render("Press 'Q' to quit.", True, WHITE)
                    screen.blit(img, (rect_win_lose.left +180, rect_win_lose.top+180))
                    pygame.display.update()
                       
                else :
                    print("You lose")
                    pygame.draw.rect(screen, RED, rect_win_lose, 0)
                    pygame.display.update()
                    screen_refreshing = False 

                    font = pygame.font.SysFont(None, 100)
                    img = font.render('Game Over!', True, WHITE)
                    screen.blit(img, (rect_win_lose.left +110, rect_win_lose.top+60))
                    pygame.display.update()

                    font = pygame.font.SysFont(None, 50)
                    img = font.render("Press 'Q' to quit.", True, WHITE)
                    screen.blit(img, (rect_win_lose.left +180, rect_win_lose.top+180))
                    pygame.display.update()
                    
                time.sleep(.25)
                # print(mousex/60 , mousey/60 )
         
        # for quiting the game when q is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q :
                running = False      

        if(mousex >= 60 and mousex <= 540 and mousey >= 60 and mousey <= 540):
            if event.type == pygame.KEYDOWN:
                if(temp_mat[int(mousex/60)-1][int(mousey/60)-1] == 0):
                    if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                        temp_mat[int(mousex/60)-1][int(mousey/60)-1] = 1 
                    if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                        temp_mat[int(mousex/60)-1][int(mousey/60)-1] = 2 
                    if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                        temp_mat[int(mousex/60)-1][int(mousey/60)-1] = 3 
                    if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                        temp_mat[int(mousex/60)-1][int(mousey/60)-1] = 4 
                    if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                        temp_mat[int(mousex/60)-1][int(mousey/60)-1] = 5 
                    if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                        temp_mat[int(mousex/60)-1][int(mousey/60)-1] = 6 
                    if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                        temp_mat[int(mousex/60)-1][int(mousey/60)-1] = 7 
                    if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                        temp_mat[int(mousex/60)-1][int(mousey/60)-1] = 8 
                    if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                        temp_mat[int(mousex/60)-1][int(mousey/60)-1] = 9 

                
                # print("\n")
                # printing(temp_mat)       



    if screen_refreshing:
        for i in range(81):
            rect1 = list_of_rect[i] 
            pygame.draw.rect(screen, ORANGE, rect1, 3)

        # for adding position numbers in the grid
        # font = pygame.font.SysFont(None, 18)
        # img = font.render(str(i), True, ORANGE)
        # screen.blit(img, (rect1.left +3, rect1.top+3))
    
    # pygame.draw.rect(screen, BLUE, list_of_rect[4], 3)
    # pygame.display.update()

    # getting the cordinates of the mouse    
    if event.type == MOUSEMOTION:
        mousey, mousex = event.pos
        mousex = (mousex//60)*60
        mousey = (mousey//60)*60

        if screen_refreshing:
            # if its inside the boundary of the board only then it will draw the green square
            if(mousex >= 60 and mousex <= 540 and mousey >= 60 and mousey <= 540):
                rect_m = Rect(mousey,mousex,60,60)
                pygame.draw.rect(screen, GREEN, rect_m, 3)
                pygame.display.update()
            
        # print(mousex,mousey)

    if screen_refreshing:  
        # # printing the populated board
        populated_board()           
        submit_button()
        
        
    

pygame.quit()