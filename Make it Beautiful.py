from collections import deque

for i in range(int(input())):

    n = int(input())

    a = deque(map(int,input().split()))

    if len(set(a))==1:
        print("NO")
        continue

   

    a = deque(reversed(a))


    ans = a.copy()

    for j in range(1,n):

        if a[j-1]==a[j]:
            ans.append(ans.popleft())
        else:
            break
    print("YES")
    print(*ans)




