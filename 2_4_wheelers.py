'''Determine how many two wheelers and four wheelers can be manufactured given the total number of vehicles and total wheels as input. '''

tv=int(input("Enter total vehicles: "))
tw=int(input("Enter total wheels: "))

y=(tw-2*tv)//2
x=tv-y

if x<0 or y<0:
    print("Cannot find solution")

else:
    print("Number of 2 wheelers: ",x)
    print("Number of 4 wheelers: ",y)
