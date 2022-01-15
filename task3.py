def f(I,Familiar):
    Iw='You won'
    Fw='You lose'
    if(I==Familiar):
        print('Draw')
    elif(I==0 and Familiar==1) or(I==1 and Familiar==2) or (I==2 and Familiar ==0):
        return Iw
    else:
        return Fw

from random import randint
x=['rock','scissors','paper']
I_word=str(input('rock scissors paper?\n'))
I_move=x.index(I_word)

F_move = randint(0,2)
F_word=x[F_move]

print('Familiar move-',F_word,'\n',f(I_move,F_move))    