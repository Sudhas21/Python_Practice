1.

n = int(input("Enter a number: "))

d = {}
for i in range(1, n + 1):
    d[i] = i * i

print(d)


2.

n = int(input("Enter a number: "))

fact = 1
for i in range(1, n + 1):
    fact *= i

print(fact)


3.

values = input("Enter comma-separated numbers: ")

list_values = values.split(",")
tuple_values = tuple(list_values)

print(list_values)
print(tuple_values)

