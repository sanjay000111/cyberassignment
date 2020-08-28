num = int(input("Enter the limit:"))

my_dict = {}

for i in range(2,num+1):
    fact = 1
    for j in range(2,i):
        if i%j==0:
            fact = 0
            break

    if fact == 0:
        my_dict[i] = "Not-Prime"
    else:
        my_dict[i] = "Prime"

print(my_dict)

my_dict_copy = my_dict.copy()

for item in my_dict_copy:
    if my_dict_copy[item] == 'Not-Prime':
        my_dict.pop(item)

print(my_dict)
