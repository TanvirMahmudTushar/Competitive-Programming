for i in range(int(input())):
    n, k = map(int,input().split())
    ans = []

    for j in range(k):
        ans.append(1)
    for gg in range(n-k):
        ans.append(0)
    res = ''
    for zz in ans:
        res+=str(zz)
    print(res)

    