'''Auto Fare (There is a fixed minimum charge of Rs. 35 which takes you the first 1.6 km. 
After that every km and part thereof is charged at Rs.10 per km. 
Waiting charges are at Rs 1 per minute and luggage charges are at Rs 5 per 10kg)'''

d=int(input())
w=int(input())
l=int(input())

dist_fare=10
dist_cost,wait_cost,lug_cost=35,0,0
if d>1.6:
    dist_cost=35+(dist_fare*(d-1.6))

if w>0:
    wait_cost=w

n=l/10
lug_cost=n*5

total_cost=dist_cost+wait_cost+lug_cost
print(total_cost)
