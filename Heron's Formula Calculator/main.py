import math 

a = float(input("Side a: "))
b = float(input("Side b: "))
c = float(input("Side c: "))

def heronsFormula(a, b, c):
    s = (a + b + c) / 2
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    return area


answer = heronsFormula(a, b, c)
print("The area of the triangle is:", answer)









