'''Get an input string S from the user.  If the string consists of ‘*’ and ‘#’, 
program needs to find the minimum number of ‘*’ or ‘#’ to make it a valid string. 
The string is considered valid if the number of ‘*’ and ‘#’ are equal. The ‘*’ and ‘#’ can be at any position in the string. 
Note : The output will be zero, positive or negative integer based on number of ‘*’ and ‘#’ in the input string.'''


str= input()
hc,sc=0,0
for i in str:
    if i=='*':
        sc=sc+1
    elif i=='#':
        hc=hc+1

count=sc-hc
if count==0:
    print("total count is zero. so valid")
else:
    print("total count is not 0, instead ", count)
    print("Not valid")
