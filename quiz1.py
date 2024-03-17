# User input
r = input('Please input a Richter scale value : ')
r = float(r)

# Calculate
e = 10**((1.5*r)+4.8) #J
t = e/(4.184*(10**9))
nl = e/2930200

#print
print('Richter scale value :', r)
print('Equivalence in Joules :', e)
print('Equivalence in tons of TNT :', t)
print('Equivalence in the number of nutritious lunches :', nl)
