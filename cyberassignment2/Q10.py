num = int(input("Enter the number:"))

def fact(n):
    prod = 1
    for i in range(1,n+1):
        prod *= i

    return prod

for i in range(num):
    for k in range(num-i):
        print(end=" ")

    for j in range(i+1):
        result = fact(i)/(fact(j)*fact(i-j))
        print(int(result), end=" ")
    print("\n")