# Python 3

from IPython.display import clear_output
def replace_list(values):
    row1=[' ',' ',' ']
    row2=[' ',' ',' ']
    row3=[' ',' ',' ']
    counter=0
    counter1=0

    for x in range(len(values)):

        if x<3:
            row1[x]=values[x]
        elif x>2 and x<6:
            row2[counter]=values[x]
            counter=counter+1
        else:
            row3[counter1]=values[x]
            counter1=counter1+1
    return row1,row2,row3
def display_board(row1,row2,row3):
    clear_output()
    print (row1[0]+' | '+row1[1]+' | '+row1[2])
    print ('--|---|--')
    print (row2[0]+' | '+row2[1]+' | '+row2[2])
    print ('--|---|--')
    print (row3[0]+' | '+row3[1]+' | '+row3[2])

def choice():
    checker1=True
    while checker1:
        choice_one_fake=input("Pick a position (1-9): ")

        if choice_one_fake.isdigit() and int(choice_one_fake) in range(1,10):
            checker1=False
        else:
            print ("Invalid choice")
    return int(choice_one_fake)-1

def replace(turn,position,values):
    if turn:
        values[position]='O'
    else:
        values[position]='x'
    return values

def gameon_check():
    checker=True
    while checker:
        question=input('Play again (Y/N): ')
        if question.upper()=='Y':
            return True

        elif question.upper()=='N':
            return False

        else:
            print ('Invalid input')

def win(turn,row1,row2,row3):

    if (row1[0]!=' ' and (row1[0]==row2[0]==row3[0])) or (row1[2]!=' ' and (row1[2]==row2[2]==row3[2])) or (row1[1]!=' ' and (row1[1]==row2[1]==row3[1])):
        if turn%2==0:
            print ('Player 1 won!')
        else:
            print ('Player 2 won!')
        return True
    elif (len(set(row1))==1 and row1[0]!=' ') or (len(set(row2))==1 and row2[0]!=' ') or (len(set(row3))==1 and row3[0]!=' '):
        if turn%2==0:
            print ('Player 1 won!')
        else:
            print ('Player 2 won!')
        return True
    elif (row1[0]!=' ' and row1[0]==row2[1]==row3[2]) or (row3[0]!=' ' and row3[0]==row2[1]==row1[2]):
        if turn%2==0:
            print ('Player 1 won!')
        else:
            print ('Player 2 won!')
        return True
    elif ' ' not in row1 and ' ' not in row2 and ' ' not in row3:
        print ("Draw! None won.")
        return True
    else:
        return False

game_on=True
while game_on:
    # Game Starts
    values=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
    rows=replace_list(values)
    display_board(rows[0],rows[1],rows[2])

    win_check=False
    player=1
    while win_check==False:

        # Ask which box he wants to select and check if that's already been taken
        taken=False
        while not taken:
            ask=choice()
            if values[ask]!=' ':
                print ("That box has already been selected!")
            else:
                taken=True
        # replace that box
        if player%2==0:
            values[ask]='O'
        else:
            values[ask]='X'
        player=player+1

        rows=replace_list(values)
        clear_output()
        display_board(rows[0],rows[1],rows[2])
        win_check=win(player,rows[0],rows[1],rows[2])
    game_on=gameon_check()
