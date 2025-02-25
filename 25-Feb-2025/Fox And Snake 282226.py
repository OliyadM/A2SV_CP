# Problem: Fox And Snake - https://codeforces.com/problemset/problem/510/A

m,n = map(int,input().split())
for i in range(1,m+1):
    if i%2:
        print('#'*n)
    elif not i%2 and i%4:
        print(('.'*(n-1))+'#')
    else:
        print('#'+('.'*(n-1)))