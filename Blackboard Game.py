
for i in range(int(input())):
    n = int(input())
    cnt = [0] * 4
    for i in range(n):
        cnt[i % 4] += 1
    print("Bob" if cnt[0] == cnt[3] and cnt[1] == cnt[2] else "Alice")
