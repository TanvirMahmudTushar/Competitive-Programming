for i in range(int(input())):
    ans = 0
    for j in range(10):
        lst = list(input())

        lst1 = lst[0:5]
        lst2 = lst[5:]
        lst2 = lst2[::-1]
       

        for gg in range (len(lst1)):
            if lst1[gg]=='X':
                ans +=(gg+1)
        for zz in range (len(lst2)):
            if lst2[zz]=='X':
                ans +=(zz+1)
    print(ans)
        


