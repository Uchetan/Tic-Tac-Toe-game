import comp
import win
import list_print as pr
lis=[1,2,3,4,5,6,7,8,9]
pr.pri(lis)
inp=input("Do You want to play with Computer User (Y or N):")
pla1=input("Enter Your name : ")
if inp =='N' or inp=='n':
    pla2=input('Enter Your name : ')
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
            while True:
                try:
                    a=int(input(pla2+" your turn : "))
                    if lis[a-1]=="X" or lis[a-1]=="#":
                        print('Already Entered , enter any other number : ')
                    else:
                        lis[a-1]='#'
                        break
                except Exception as e:
                    print(e)
        a1=win.dec(lis,pla1,pla2)
        if a1!=False:
            print("\t\t",a1,"Won the game !!!!!")
            pr.pri(lis)
            break
        full=False
        for j in lis:
            if type(j)==int:
                full=True
        if full==False:
            print("\t\tThis match is Draw !!!!!")
            pr.pri(lis)
            break
        pr.pri(lis)
        i+=1
else:
    win=comp.com_play(pla1,lis)
    if win !="Draw":
        print("\t\t",win,"Won the game !!!!!")
    else:
        print("\t\tMatch is Draw !!!!!")