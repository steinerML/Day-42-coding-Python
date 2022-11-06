def calculate (**kwargs):
    T = kwargs['bedrag']
    i = kwargs['interest']
    n = kwargs['term']
    
    J = (i/(1-(1+i)**(-n)))*T
    
    return J

a = calculate(bedrag=100000, interest=0.4074/100, term =360)
print(round(a,2))