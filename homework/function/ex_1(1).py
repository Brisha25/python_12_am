#Write a function get_simple_interest(principal, rate, time) 
#to calculate and return simple interest based on given principal, rate and time.
def get_simple_interest(p,r,t):
    simple_interest = p*r*t/100
    return simple_interest

si = get_simple_interest(10000,2,10)
print(si)