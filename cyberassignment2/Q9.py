import sys

lst = sys.argv

n = int(lst[1])

a = 0
b = 1
i = 0
print(a)
print(b)

while i<n-2:
    c = a + b
    print(c)
    a = b
    b = c
    i += 1
    