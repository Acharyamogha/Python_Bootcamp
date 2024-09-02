'''
Given an array of integers and an integer sum as inputs, find a pair of numbers (a, b) in the array where a + b = sum.
'''

n=int(input("Enter array size"))
a=[0 for _ in range(n)]
for i in range(n):
    a[i]=int(input())
    
sum=int(input("enter the sum"))

for i in range(n):
    for j in range(i,n):
        if a[i]+a[j]==sum:
            print(str(a[i])+","+str(a[j]))
