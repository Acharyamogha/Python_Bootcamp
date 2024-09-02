'''
Write an algorithm to determine if the spelling of a number is in the ascending order as per the English alphabet
'''

num=input("Enter the number in words: ")
x=True
for i in range(len(num)):
    if i==len(num)-1:
        break
    elif ord(num[i])>ord(num[i+1]):
        x=False
        print("not in ascending order")
        break

if x:
    print("Number is in ascending order")
