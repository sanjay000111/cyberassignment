def almost_there(num):
    if (num>=90 and num<=110) or (num>=190 and num<=210):
        return True
    else:
        return False

print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))