def summer_69(lst):
    sum = 0

    if 6 in lst:
        start_pos = lst.index(6)
        last_pos = lst.index(9)
    else:
        start_pos = -1
        last_pos = -1
        
    for i in range(len(lst)):
        if i>=start_pos and i<=last_pos:
            pass
        else:
            sum += lst[i]

    return sum

print(summer_69([1,3,5]))
print(summer_69([4,5,6,7,8,9]))
print(summer_69([2,1,6,9,11]))