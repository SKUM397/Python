# swap 2 numbers in place
import mysql.connector

x,y = 10,20
print(x, " ",y)
x,y = y,x
print(x," ",y)

# slice a string

txt = "Hello world"
#slice a string
# start:end:step
print(txt[::2]) 
#use slice to reverse
print(txt[::-1])
