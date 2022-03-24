##Calculate SI for given data and tell total amount returned

def SI(p,r,t):
    I = (p*r*t)/100
    print("P = ",p," R = ",r," T = ",t)
    print("Simple interest = ",I)
    print("Total amt = ",I+p)

SI(1000,4,6)