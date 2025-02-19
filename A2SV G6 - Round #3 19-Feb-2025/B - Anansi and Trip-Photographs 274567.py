# Problem: B - Anansi and Trip-Photographs - https://codeforces.com/gym/588468/problem/B

def photo(arr,n,x):
    arr.sort()
    row_1=arr[:n]
    row_2=arr[n:]
    for i in range(n):
        if row_2[i] - row_1[i] <x:
            return False
    return True

t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    arr=list(map(int,input().split()))
    if photo(arr,n,x):
        print("YES")
    else:
        print("NO")