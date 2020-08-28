def letter_count(string):
    count_upper = 0
    count_lower = 0
    for i in range(len(string)):
        if string[i].isalpha():
            if string[i].isupper():
                count_upper += 1
            elif string[i].islower():
                count_lower += 1

    print(f"The total number of upper case letters in string {string} is {count_upper}.")
    print(f"The total number of lower case letters in string {string} is {count_lower}.")

letter_count("Hello My name is Varnsh Karnwal.")