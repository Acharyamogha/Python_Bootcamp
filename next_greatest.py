'''
Take an array as user input and print the Next Greater Element (NGE) for every element.
If x is the first greater element on the right side of x in the array.
Elements for which no greater element exist, consider the next greater element as -1.
'''

ip=input()
a=list(map(int, ip.split()))
b=[]
c=len(a)
for i in range(c):
    for j in range(i+1, c):
        if a[j]>a[i]:
            b.append(a[j])
            break
b.append(-1)
print(b)
