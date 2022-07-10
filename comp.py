import random
import win
import list_print as pr


def com_play(pla1,lis):
    pla2='Comp'
    i=0
    while True:
        if i%2==0:
            while True:
                try:
                    a=int(input(pla1+" your turn : "))
                    if lis[a-1]=="X" or lis[a-1]=="#":
                        print('Already Entered , enter any other number : ')
                    else:
                        lis[a-1]='X'
                        break
                except Exception as e:
                    print(e)
        else :
            print(pla2+" your turn : ",end="")
            while True:
                try:
                    a=random.choice(lis)
                    if lis[a-1]=="X" or lis[a-1]=="#":
                        pass
                    else:
                        print(a)
                        lis[a-1]='#'
                        break
                except Exception as e:
                    print(e)
        a1=win.dec(lis,pla1,pla2)
        if a1!=False:
           return a1
        full=False
        for j in lis:
            if type(j)==int:
                full=True
        if full==False:
            return "Draw"
        pr.pri(lis)
        i+=1
