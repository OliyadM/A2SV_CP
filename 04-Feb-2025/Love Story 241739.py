# Problem: Love Story - https://codeforces.com/contest/1829/problem/A

t=int(input())
for _ in range(t):
    string = input()
    n=len(string)
    k=0
    for i in range(len(string)):
        if string[i]!='codeforces'[i]:
            k+=1
    print(k)