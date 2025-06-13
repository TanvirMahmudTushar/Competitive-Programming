for i in range(int(input())):
    
    n = int(input())
    a = list(map(int, input().split()))

    f = a[0]

    l = a[-1]

    d = 1 - n * n

    u = l - f * n

    if d == 0 or u % d != 0:
        print("NO")
        continue

    y = u // d
    x = f - y * n

    if x < 0 or y < 0:

        print("NO")
        continue

    flg = True

    for i in range(n):

        if a[i] != x * (i + 1) + y * (n - i):

            flg = False
            break

    if flg:
        print("YES")
    else:
        print("NO")
  
