a,b=5,10
print("original a = ",a)
print("original b=",b)
print("\n")
#Using a Temporary Variable
print("Using a Temporary Variable")
a,b = 5,10

temp = a
a = b
b = temp

print("a =", a, "b =", b)

# Using Arithmetic: Addition & Subtraction
print("Using Arithmetic: Addition & Subtraction")
a,b = 5,10

a = a + b
b = a - b
a = a - b

print("a =", a, "b =", b)

#Using Multiplication & Division
print("Using Multiplication & Division")
a,b = 5,10

a = a * b
b = a / b
a = a / b

print("a =", int(a), "b =", int(b))

