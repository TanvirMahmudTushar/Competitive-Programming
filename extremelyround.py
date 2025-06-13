for i in range(int(input())):
    n = int(input())
    eq = int('1'+'0'*(len(str(n))-1))
    if n<=10:
        print(n)
    elif n<= 100:
        print(9+n//10)
    elif n<= 1000:
        print(19+(n//100)-1)
    elif n<=10000:
        print(28+(n//1000)-1)
    elif n<=100000:
        print(37+((n//10000)-1))
    elif n<=1000000:
        print(46+((n//100000)-1))
    

