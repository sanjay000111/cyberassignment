def spy_game(lst):
    result = False
    for i in range(len(lst)):
        if lst[i] == 0:
            for j in range(i+1,len(lst)):
                if lst[j] == 0:
                    for k in range(j+1, len(lst)):
                        if lst[k] == 7:
                            result = True
    return result

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))