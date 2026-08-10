# Asssignment 2.1 WAP to add 3 no.s and print result
a = 3
b = 4
c = 5
print(a+b+c)

# Assignment 2.2 WAP to concatenate three strings and print result
x =  "Ram"
y = "Varshney"
z = "1024160048"
print(x + " " + y + " " + str(z))

# Assingment 4.1: WAP to print the table of 7, 9
for i in range(1, 11):
    print(7, "x", i, "=", 7*i)

for i in range(1, 11):
    print(9, "x", i, "=", 9*i)

# Assingment 4.2: WAP to print the table of n and n is given by user
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "*", i, "=", n*i)


# Assingment 4.3: WAP to add all the numbers from 1 to n and n is given by user.
n = int(input("Enter a number: "))

total = 0
for i in range(1, n+1):
    total = total + i

print(total)

# Assingment 5.1: WAP to find max amoung three numbers and input from user. [Try max() function]
a = int(input("Enter First No: "))
b = int(input("Enter Second No: "))
c = int(input("Enter Third No: "))

print(max(a, b, c))

# Assingment 5.2: WAP to add all numbers divisible by 7 and 9 from 1 to n and n is given by the user.
n = int(input("Enter a No: "))

total = 0
for i in range(1, n+1):
    if i % 7 == 0 and i % 9 == 0:
        total = total + i

print(total)

# Assingment 5.3: WAP to add all prime numbers from 1 to n and n is given by the user.
n = int(input("Enter a No: "))

total = 0
for i in range(2, n+1):
    f = 0
    for j in range(2, i//2 + 1):
        if i % j == 0:
            f = 1
            break
    if f == 0:
        total = total + i

print(total)

# Assingment 6.1: WAP using function that add all odd numbers from 1 to n, n is given by the user.
def AddOdd(n):
    total = 0
    for i in range(1, n+1):
        if i % 2 != 0:
            total = total + i
    return total

n = int(input("Enter a No: "))
print("AddOdd(", n, ") -> ", AddOdd(n))

# Assingment 6.2: WAP using function that add all prime numbers from 1 to n, n given by the user.

def IsPrime(n):
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return 0
    return 1

def AddPrime(n):
    total = 0
    for i in range(2, n+1):
        if IsPrime(i) == 1:
            total = total + i
    return total

n = int(input("Enter a No: "))
print("AddPrime(", n, ")    -> ", AddPrime(n))