for i in range(int(input())):
    n,m = map(int,input().split())
    x = input()
    s = input()
    ans = 0

    for j in range(6):
        if s in x:
            print(ans)
            break
        else:
            ans+=1
            x+=x
    else:
        print(-1)




