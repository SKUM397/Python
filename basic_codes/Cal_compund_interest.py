# calculate Compound interest for given data

def CI(principle,rate,time):
#    power = pow(((1+r)/100),t)
#    amt = p * power
    Amount = principle * (pow((1+rate/100),time))
#    Amount = principle * (pow((1 + rate/100),time))
    I = Amount - principle
    print("Comound interest = ", I)

CI(10000,10.25,5)

#check pull

