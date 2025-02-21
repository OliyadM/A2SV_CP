# Problem: B - Special Matrix Quest - https://codeforces.com/gym/586960/problem/B

n = int(input().strip())
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))
 
m = n // 2
total = 0
 
for i in range(n):
    total += mat[i][i]  
    total += mat[i][n - 1 - i]  
    total += mat[m][i]  
    total += mat[i][m]  
 
total -= 3 * mat[m][m]
 
print(total)