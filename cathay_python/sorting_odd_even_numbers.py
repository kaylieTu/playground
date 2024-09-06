def mixed_number():
    try:
        n= list(input("Please Enter numbers: "))   
        length=len(n)
        evenlist=[]
        oddlist=[]
        s=""
        for i in range(length):
            new_num=int(n[i])
            if new_num % 2 ==0 :
                evenlist.append(new_num)
            else:
                oddlist.append(new_num)
                evenlist.sort()
        oddlist.sort(reverse=True)
        oddlist.extend(evenlist)
        for i in range(len(oddlist)):
            s=s+str(oddlist[i])
        return print(s)
    except ValueError:
        return print("It's not a number!")

mixed_number()