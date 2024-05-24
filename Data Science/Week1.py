# Create lower triangular, upper triangular and pyramid containing the "*" character.


# lower triangular

n = int(input("Enter the numbers of rows in lower triangular: "))
for i in range(n):
    for j in range(i+1):
        print("*",end="  ")
    print()

# upper triangular
n = int(input("Enter numbers of rows in upper trainagle: "))
for i in range(n):
    for j in range(n):
        if i<=j :
            print("*  ", end="")
        else:
            print("   ", end='')
    print()

# pyramid
n = int(input("Enter number of rows in pyramid: "))
for i in range(n):
    for j in range(n - i - 1):
        print("   ", end="")
    for k in range(2 * i + 1):
        print("*  ", end="")
    print()