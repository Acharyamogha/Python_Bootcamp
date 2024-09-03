'''
You are given a string. 
If the string has some “#”, in it you have to move all the hashes to the front of the string and return the whole string back
'''

str=input()

c=0
for i in range(len(str)):
    if str[i] == '#':
        c=c+1
        str2=str.replace('#', '')

str1='#'*c
str=str1+str2
print(str)
