def pallindrome(string):
    size = len(string) - 1
    i = 0
    fact = 1
    while i<=len(string)//2:
        if string[i] != string[size]:
            fact = 0
            break
        i += 1
        size -= 1

    if fact == 1:
        print("The entered string is pallindrome.")
    elif fact == 0:
        print("The entered string is not pallindrome.")

pallindrome("02022020")