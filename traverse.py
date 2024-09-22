"""
Traverse a matrix clockwise.  Ask user to enter number of rows and number of columns in a 2 dimension matrix.  
Using these numbers, ask user to enter the matrix elements.  
Once the matrix elements are entered, program needs to start from the top left corner of the matrix and 
traverse the matrix in clockwise spiral and print all values in a single line
    
"""
m,n=3,3

a=[[1,2,3],
[5,6,7],
[9,10,11]]

i=0
x=m//2
y=n//2
while m>x and n>y:
    for j in range(i,n):
        print(a[i][j], end=' ')
    
    for i in range(i+1, m):
        print(a[i][j], end=' ')
    
    for j in range(n-2,-1,-1):
        print(a[i][j], end=' ')
    
    for i in range(m-2,0,-1):
        print(a[i][j], end=' ')
    m=m-1
    n=n-1

