for i in range(int(input())):
    n,x = map(int,input().split())

    lst = list(map(int,input().split()))

    diff = 0 

    for j in range(1,n):
        if lst[j]-lst[j-1]>diff:
            diff = lst[j]-lst[j-1]
    end = (x-lst[-1])*2
    beg = lst[0]
    
    print(max(diff,end,beg)) 
