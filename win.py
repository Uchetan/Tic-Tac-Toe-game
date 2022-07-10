def winner(a,lis,pla1,pla2):
    if lis[a]=='X':
        return pla1
    else:
        return pla2

def dec(lis,pla1,pla2):
    if lis[0]==lis[1]==lis[2]=='X'or lis[0]==lis[1]==lis[2]=='#':
        a=winner(0,lis,pla1,pla2)
        return a
    elif(lis[0]==lis[3]==lis[6]=='X'or lis[0]==lis[3]==lis[6]=='#'):
        a=winner(0,lis,pla1,pla2)
        return a
    elif(lis[0]==lis[4]==lis[8]=='X'or lis[0]==lis[4]==lis[8]=='#'):
        a=winner(0,lis,pla1,pla2)
        return a
    elif(lis[3]==lis[4]==lis[5]=='X'or lis[3]==lis[4]==lis[5]=='#'):
        a=winner(3,lis,pla1,pla2)
        return a
    elif(lis[6]==lis[7]==lis[8]=='X'or lis[6]==lis[7]==lis[8]=='#'):
        a=winner(6,lis,pla1,pla2)
        return a
    elif(lis[1]==lis[4]==lis[7]=='X'or lis[1]==lis[4]==lis[7]=='#'):
        a=winner(1,lis,pla1,pla2)
        return a
    elif(lis[2]==lis[5]==lis[8]=='X'or lis[2]==lis[5]==lis[8]=='#'):
        a=winner(2,lis,pla1,pla2)
        return a
    elif(lis[2]==lis[4]==lis[6]=='X'or lis[2]==lis[4]==lis[6]=='#'):
        a=winner(2,lis,pla1,pla2)
        return a
    else:
        return False
