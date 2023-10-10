import random
squers = [0]*51
for i in range(51):
    squers[i]=i**2
print(squers)
print("---------")

cubs=[x**3 for x in range(20,31)]
print(cubs)
print("---------")

def f(x):
    y=3*x-2
    return y
values=[f(x) for x in range(-5,6)]
print(values)
print("---------")

pary = [(x,y) for x in range(10,21) for y in range(5,11)]
print(pary)
print("---------")

# pary2 = [(x,y) for x in range(4,8) for y in ['jablko','gruszka','komputer']]
pary2 = [(random.choice(range(4,8)),random.choice(['jablko','gruszka','komputer'])) for k in range(5)]
print(pary2)
print("---------")
