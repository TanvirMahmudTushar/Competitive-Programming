for i in range(int(input())):
    n, k = map(int,input().split())
    lst = list(map(int,input().split()))

    if k in lst:
        print("YES")
    else:
        print("NO")