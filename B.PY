for i in range(int(input())):
    n = int(input())
    left = 3
    right = n
    if n==3:
        print(1,3,2)
        continue
    lst = [1]
    

    while left <= right:
        
        lst.append(left)
        lst.append(right)

        left+=1
        right-=1
    lst.append(2)
    if n%2!=0:
        lst.remove(left-1)
    print(*lst)
    


