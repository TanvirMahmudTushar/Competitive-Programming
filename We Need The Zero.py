for i in range(int(input())):

    n = int(input())

    lst = list(map(int,input().split()))

    ans = lst[0]

    for j in range(1,n):

        ans^=lst[j]
    if ans==0:
        print(0)
    
    elif n%2 != 0:
        print(ans)
    else:
        print(-1)


