# # Collects value of x and y from the user
# x = float(input("Enter first number "))
# y = float(input("Enter second number "))

# # Round funtion rounds the float to the nearest 2 decimal places then stores it into the variable Z then prints the result.
# z = round(x+y , 2)
# print (z)

# Collects value of x and y from the user
x = float(input("Enter first number "))
y = float(input("Enter second number "))

# Here we use the round function inside an F-string for the same rounding above but the syntax is different cos we use ':.(n)f'
b = (f"{x+y:.2f}")
print (b)