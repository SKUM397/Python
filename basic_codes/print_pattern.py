#WAP to print this pattern
#1           i is top to bottom, starts from 0 to user input number
#1 2         j is left to right, starts from 0 to i+1 so it runs from 0 to i
#1 2 3       sep="" is seperation command
#1 2 3 4     end="" is what to use to end the line
#1 2 3 4 5   Also modified code to print every digit twice

def pattern_1(n):
    num = 1
    for i in range (0,n):
#        print("i = " , i)
        num = 1
        for j in range (0,i+1):
#            print("j= ",j, "num = ", num)
            print(str(num) ,str(num), sep = "", end=" ")
#            print(end=" ")
            num = num + 1
        print("\r")


n= 10
print(pattern_1(n))