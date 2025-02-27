# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

def median(arr):
    arr.sort()
    n = len(arr)
    if  n%2 !=0:
        return arr[n//2]
    else:
        
        return arr[(n//2)-1]

t=int(input())
arr=list(map(int,input().split()))
print(median(arr))
