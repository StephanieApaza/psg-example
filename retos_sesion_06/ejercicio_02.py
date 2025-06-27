# Construyendo el operador XNOR

print("Operador XNOR")

print("   A    |    B   |  A XNOR B")
print("-----------------------------")
a = True
b = True
c = (a and b) or (not a and not b)
print(" ",a," | ",b," | ",c)

a = True
b = False
c = (a and b) or (not a and not b)
print(" ",a," | ",b,"| ",c)

a = False
b = True
c = (a and b) or (not a and not b)
print(" ",a,"|",b,"  | ",c)

a = False
b = False
c = (a and b) or (not a and not b)
print(" ",a,"| ",b,"| ",c)