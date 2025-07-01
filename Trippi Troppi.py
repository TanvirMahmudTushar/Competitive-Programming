for i in range(int(input())):

    s = input()

    lst = s.split()

    ans = ''

    for j in range(len(lst)):

        ans+=lst[j][0]
    print(ans)