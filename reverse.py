'''
What logic will you use to reverse an integer without using any string functions?

'''

n=int(input())
rev=0
while n>0:
    rem=n%10
    rev=rev*10 + rem
    n=n//10
    
print(rev)
