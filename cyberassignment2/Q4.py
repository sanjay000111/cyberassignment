def unique(lst):
    new_lst = []
    for item in lst:
        if lst.count(item) == 1:
            new_lst.append(item)

    return new_lst

print(unique([1,1,2,3,4,5,5,6,6]))