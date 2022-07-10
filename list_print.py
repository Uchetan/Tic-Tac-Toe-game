def pri(lis):
    j=1
    a=1
    for i in lis:
        if j%3 == 0:
            print("",i)
            if a<=2:
                for k in range(0,3):
                    print('  -',end='')
            a+=1
            print()
        else:
            print('',i,end=' |')
        j+=1