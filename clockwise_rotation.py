'''
Given a square matrix, turn it by 90 degrees in an clockwise direction
'''

m=int(input("Enter the number of rows"))
n=int(input("Enter the number of columns"))

a=[[0 for _ in range(n)] for _ in range(m)]

print("Enter the matrix elements")
for i in range(m):
    for j in range(n):
        a[i][j]=int(input())
    
for i in range(m):
    for j in range(n):
        print(a[i][j], end=" ")
    print()

print("\nMatrix after rotation")

for i in range(m):
    j=n-1
    for j in range(n-1,-1,-1):
        print(a[j][i], end=" ")
    print()
