from __future__ import print_function

def square_sum(n):
    sm = 0
#    numbers = [1,2,3,4,5]
    for i in range (1, n+1):
        sm = sm + (i*i)
#        print("sm = ")
#        print(sm)
    return sm

n=5
print(square_sum(n))
