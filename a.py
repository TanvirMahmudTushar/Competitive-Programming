for i in range(int(input())):
    n,x = map(int,input().split())
    lst = list(map(int,input().split()))

    for j in range(n):
        if lst[j] == 1:
            if 1 in lst[j+x:n]:
                print("NO")
                break
    else:
        print("YES")