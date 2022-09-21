def sudoku_grid_correct(x):
    def row_correct(sudoku, row_no):
        new=[]
        for value in sudoku[row_no]:
            if value not in new or value==0:
                new.append(value)
        if len(new)==len(sudoku[row_no]):
            return True
        else:
            return False
    def block_correct(sudoku, row_no, column_no):
        block=[]
        for row in range(row_no, row_no+3):
            for col in range(column_no, column_no+3):
                value=sudoku[row][col]
                if value not in block or value==0:
                    block.append(value)
        if len(block)==9:
            return True
        else:
            return False
    def column_correct(sudoku, column_no):
        newc=[]
        for value in sudoku:
            if value[column_no] not in newc or value[column_no]==0:
                newc.append(value[column_no])
        if len(newc)==9:
            return True
        else:
            return False
    for r in range (0,9):
        if row_correct(x, r)==False:
            return False
    for c in range(0,9):
        if column_correct(x,c)==False:
            return False
    for r in range (0,9,3):
        for c in range(0,9,3):
            if block_correct(x,r,c)==False:
                return False
    for i in x:
        for v in i:
            if v==0:
                return False
    return True
def print_sudoku(sudoku: list):
    i=0
    r=0
    b=0
    for item in sudoku:
        for value in item:
                i+=1
                if r==3:
                    print()
                    r=0
                    b+=1
                    if b==3:
                        print()
                        if value==0:
                            print('_ ', end='')
                        elif value>0:
                            print (f'{value} ', end='')
                        b=0
                        continue
                    elif value==0:
                        print('_ ', end='')
                    elif value>0:
                        print (f'{value} ', end='')
                elif i==3:
                    if value==0:
                        print('_ ', end=' ')
                    elif value>0:
                        print (f'{value} ', end=' ')
                    i=0
                    r+=1
                elif value==0:
                    print('_ ', end='')
                elif value>0:
                    print (value, end=' ')
def add_number(sudoku,x,y,number):

    row=sudoku[x]
    row[y]=number
def select_difficulty():
    while True:  
        setting=input('Please choose Hard, Extremely Hard, or Impossible: ')
        if setting.lower()=='hard':
            problem=[
        [7,9,8,0,1,5,0,0,0],
        [2,0,0,3,0,0,1,9,7],
        [3,0,0,0,4,9,0,5,2],
        [5,0,7,6,0,3,9,0,0],
        [0,4,3,0,9,0,0,0,1],
        [0,8,0,0,7,4,5,3,6],
        [4,3,6,9,0,0,0,1,0],
        [0,2,9,4,0,0,3,7,0],
        [0,0,0,8,3,2,6,4,0]]
            print()
            break
        if setting.lower()=='extremely hard':
            problem=[
        [0,1,4,0,0,0,0,0,0],
        [0,0,0,0,6,5,0,0,0],
        [0,0,0,9,2,0,1,5,0],
        [0,5,0,0,3,0,4,6,0],
        [0,0,3,0,4,0,0,0,0],
        [0,0,2,6,0,1,7,0,5],
        [0,7,0,0,0,0,5,1,3],
        [1,0,0,0,0,0,0,9,0],
        [0,0,0,3,0,6,0,7,0]]
            print()
            break
        if setting.lower()=='impossible':
            problem=[
        [0,3,0,0,0,0,1,0,0],
        [8,0,1,0,0,6,0,7,0],
        [0,5,0,0,8,0,0,0,0],
        [0,0,0,0,0,7,0,0,9],
        [4,0,2,0,6,0,5,0,0],
        [0,8,0,0,0,0,0,0,0],
        [0,0,0,2,0,0,0,5,0],
        [1,0,6,0,4,0,2,0,0],
        [0,0,3,0,0,0,0,0,0]]
            print()
            break
        else:
            print()
            print('Please choose from the options!')
            print()
        continue
    return problem 
def play_game():
    print()
    print('Welcome to Sudoku. To make a selection, please choose the row, column, and number. ')
    print('To remove a selection please reselect the square and enter 0 for the number.')
    print("The puzzle will stop once you solve it or you enter a value that's not possible.")
    print('Have fun! :)')
    print()
    print()
    sudoku  = select_difficulty()
    print_sudoku(sudoku)
    print()
    while sudoku_grid_correct(sudoku)==False:
        print()
        x=int(input('Row:'))
        if x<=0:
            print('Thanks for playing!')
            print()
            break
        y=int(input('Column:'))
        if y<=0:
            print('Thanks for playing!')
            print()
            break
        number=int(input('Number:'))
        if number<0:
            print('Thanks for playing!')
            print()
            break
        add_number(sudoku,x-1,y-1,number)
        print()
        print('New Grid:')
        print_sudoku(sudoku)
        print()
        print()
    if sudoku_grid_correct(sudoku)==True:
        print('Congratulations! You found the correct solution!')


play_game()
