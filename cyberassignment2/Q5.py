def result_multiply(lst):
    result = 1
    for item in lst:
        result *= item
    return result

print(result_multiply([1,2,3,4,5]))