'''
Every decimal number can be changed into its binary form. Suppose your computer has it’s own Corona Virus, 
that eats binary digits from the right side of a number. 
Suppose a virus has 6 spikes, it will eat up 6 binary digits in your numbers. 
You will have a bunch of numbers, and your machine will have a virus with n spikes, 
you have to calculate what will be the final situation of the final numbers. 
First input, a single Integer N Second input space separated integers of the bunch of values Third input a single integer n, 
the number of spikes in Corona for Computer

'''

# take user input
n=int(input())
b=[0 for _ in range(n)]

ip=input()
spikes=int(input())

# convert string to integer values
a=list(map(int, ip.split()))

# convert decimal to binary string
for i in range(0,n):
    b[i]=bin(a[i])[2:]

# remove the characters from right depending on spikes value
for i in range(len(b)):
    if len(b[i])<=spikes:
        b[i]="0"
    else:
        b[i]=b[i][:-spikes]
        
# convert string back to integer
dec=[int(i) for i in b]
print(dec)
