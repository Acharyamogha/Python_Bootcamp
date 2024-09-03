'''
You’re given a string where multiple characters are repeated consecutively. You’re supposed to reduce the size of this string using mathematical logic given as in the example below :

Input =    abbbccddddde
Output = ab3c2d5e
'''

s=input()

for i in s:
        c=s.count(i)
        #if count is greater than 1, replace all the occurrences with number of occurrences of that char
        if c>1:
            s=s.replace(i*c,i+str(c))
print(s)
