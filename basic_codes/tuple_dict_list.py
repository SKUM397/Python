#WAP to unpack a tuple in several variables
import string
from re import M
from tokenize import maybe


myTuple = (1,2,3,4,5)

print(myTuple)
n1,n2,n3,n4,n5 = myTuple

print(n1+n2+n3)

myTuple = myTuple + (6,)
print(myTuple)

myTuple = myTuple + (7,8,9) + myTuple
print(myTuple)

#get 4th from first and last of a tuple
myTupleStr = ('s','u','d','h','a','n','s','h','u','k','u','m','a','r')
print(myTupleStr[3] + "  " + myTupleStr[-4])

#print how many time some character is repeated
str = string.ascii_lowercase
print (str)
print ("length of Tuple = ", len(myTupleStr))

count = 0
leng = 0
tupLen = len(myTupleStr)
for x in str:
    for i in range(tupLen):
        if x == myTupleStr[i]:
            count+=1
            leng+=1
    #print ("i=", i)
    #print ("x=", x)
    if count >0:
        print ("count for " ,x,"= " , count)
    count = 0
print("len = ", leng)

#convert tuple to dict
t = ((1,'a'),(2,'b'),(3,'c'))
print(dict((y,x) for x,y in t))

#unzip a list of tuples to individual lists
myList = list(zip(*t))
print(myList)

#WAP to join 2 tuples together using zip method
#lists are t and myList
x = zip(t,myList)
print("zipped tuple is : ", tuple(x))
print(type(x))