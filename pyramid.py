'''
Ask user for a positive integer N as input and then construct the pyramid using the sample given below and output should contain N lines.

Suppose N = 7, output should be 
               1
              232
             34543
            4567654
           567898765
          67890109876
         7890123210987
'''

n=int(input())

for i in range(1,n+1):
    # print the starting spaces
    for j in range(1, n+1-i):
        print(" ", end="")
    # print the increasing number
    for h in range(i, 2*i):
        # if the number is greater than 9 take its remainder w.r.t 10
        if h>=10:
            h=h%10
        print(h, end="")
    # print the decreasing number
    for k in range(2*i-2, i-1, -1):
        # if the number is greater than 9 take its remainder w.r.t 10
        if k>=10:
            k=k%10
        print(k, end="")
    # print the ending spaces
    for l in range(1, n+1-i):
        print(" ", end="")
    # go to next line
    print()
