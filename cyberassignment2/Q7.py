num = int(input("Enter the number:"))

my_list = []

for i in range(2,num+1):
    fact = 1
    for j in range(2,i):
        if i%j==0:
            fact = 0
            break
    if fact == 0:
        my_list.append((i,"Not-Prime"))
    else:
        my_list.append((i,"Prime"))

print(my_list)