# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C

def splitt(string):
    if not string:
        return 0
    maximum=1
    for i in range(len(string)-1):
        first=string[:i+1]
        last=string[i+1:]
        cur_max=len(set(first))+len(set(last))
        maximum=max(maximum,cur_max)
    return maximum
t=int(input())
for _ in range(t):
    n=int(input())
    string=input()
    print(splitt(string))  