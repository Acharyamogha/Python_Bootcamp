# Change a to b and vice-versa
str=input().lower()
str1=""
for i in str:
    if i=='a':
        str1 = str1 + 'b'
    elif i=='b':
        str1= str1 + 'a'
    else:
        str1= str1 + i

print(str1)
