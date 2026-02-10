#E Sushanth
#1RUA25BCA0030
# Factorial without recursion

num = int(input("Enter a number: "))

fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial =", fact)
