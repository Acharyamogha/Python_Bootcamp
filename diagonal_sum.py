'''
Print sum of left diagonal and right diagonal of a n x n square matrix
'''

n=int(input("Enter the order of sqaure matrix"))
m=[[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        m[i][j]=int(input(f"Enter the values for {i} {j}"))

lsum,rsum=0,0
for i in range(n):
    for j in range(n):
        # left diagonal elements have equal indices
        if i==j:
            lsum=lsum+m[i][j]
        
        # right diagonal elements have their sum equal to one less than the order of matrix
        if i+j==n-1:
            rsum=rsum+m[i][j]

print("Right diagonal sum: ",rsum)
print("Left diagonal sum: ", lsum)

n=int(input("Enter the order of sqaure matrix"))
m=[[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        m[i][j]=int(input(f"Enter the values for {i} {j}"))
