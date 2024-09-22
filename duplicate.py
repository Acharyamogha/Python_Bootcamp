"""
Duplicate Number problem.  Given an array of n+1 integers where each integer is between 1 and n (inclusive), 
there is exactly one duplicate number. Find the duplicate number using only one for loop.

"""
arr=input()

arr=list(map(int, arr.split()))

arr_sum=sum(arr)
n=len(arr)-1
act_sum=n*(n+1)//2

print(f"The repeated number is: {arr_sum-act_sum}")

