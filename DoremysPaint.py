for i in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    lst.sort()
    
    if n == 2:
        print('Yes')
    elif n==3 and len(set(lst))==2:
        print("Yes")
    elif len(set(lst)) == 1:
        print("Yes")
    elif len(set(lst)) >=3:
        print("No")
    elif lst.count(lst[0])==lst.count(lst[-1]):
        print("Yes")
    elif lst.count(lst[0])==lst.count(lst[-1])-1:
        print("Yes")
    elif lst.count(lst[0])-1==lst.count(lst[-1]):
        print("Yes")
    
    else:
        print("No")

    
    


    