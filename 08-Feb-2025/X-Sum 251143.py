# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

def diagonal_sum(arr, i, j):
    m = len(arr)  
    n = len(arr[0])  
    s = arr[i][j]  

    
    x, y = i - 1, j - 1
    while x >= 0 and y >= 0:
        s += arr[x][y]
        x -= 1
        y -= 1

    
    x, y = i - 1, j + 1
    while x >= 0 and y < n:
        s += arr[x][y]
        x -= 1
        y += 1

    
    x, y = i + 1, j - 1
    while x < m and y >= 0:
        s += arr[x][y]
        x += 1
        y -= 1

    
    x, y = i + 1, j + 1
    while x < m and y < n:
        s += arr[x][y]
        x += 1
        y += 1

    return s



def max_sum(arr):
    m=len(arr)
    n=len(arr[0])
    temp_sum=0
    for i in range(m):
        for j in range(n):
            temp_sum=max(temp_sum,diagonal_sum(arr,i,j))
    return temp_sum


t = int(input())  
for _ in range(t):  
    m, n = map(int, input().split())  
    arr = []   
    for _ in range(m):  
        row = list(map(int, input().split()))
        arr.append(row)

    print(max_sum(arr))