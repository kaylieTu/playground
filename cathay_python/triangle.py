def tiangle_maker(n):
    for i in range(1,n+1):
        for k in range(2*(n-i)):
            print("", end =" ")
        if 1 < i < n:
            print("*", end =" ")
            for j in range(1,(2*(i-1)-1)*2 +1):
                print(" ",end="")
            print("*",end="")
        else:
            for j in range(1,i+1):
                if j == 1:
                    print("*",end=' ')
                else:  
                    print("  "+"*",end=' ')
        print()
        
tiangle_maker(5)
