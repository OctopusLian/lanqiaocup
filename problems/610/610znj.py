import fractions
a = 1/1
s = 0
for i in range(20):
  s = s + a
  a = a/2
print(fractions.Fraction(s))