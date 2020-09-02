def prime_count(num):
    count = 0
    for i in range(2, num+1):
        fact = 0
        for j in range(2,i):
            if i%j == 0:
                fact = 1
                break
        if fact == 0:
            count += 1
    return count

num = int(input("Enter the number: "))

print(f"There are {prime_count(num)} Prime numbers between 2-{num}.")