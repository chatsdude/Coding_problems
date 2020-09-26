
s='111111'
r = s.split("0")
print(r)
x = [len(xi) for xi in r]
print(x)
x = [xi for xi in x if xi > 0]
print(x)
if len(x) > 0:
    print(sum((n*(n+1))//2 for n in x) % 1000000007)