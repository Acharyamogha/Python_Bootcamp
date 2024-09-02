'''
Given an array of integers, write a function that returns true if there is a 
Pythagorean triplet (a, b, c) that satisfies a2 + b2 = c2.
'''

n=int(input("Enter array size"))
a=[0 for _ in range(n)]
for i in range(n):
    a[i]=int(input())

triplets=set()
for i in range(n):
    for j in range(n):
        for k in range(n):
            if a[i]**2==(a[j]**2 + a[k]**2):
                triplet=tuple(sorted((a[i],a[j],a[k])))
                triplets.add(triplet)
                
if triplets:
    for triplet in triplets:
        print("Pythagorean triplet is: ", triplet)
else:
    print("No pythagorean triplet")
