lower_val = int(input("Enter the lower limit of the range:"))

upper_val = int(input("Enter the upper limit of the range:"))

num = int(input("Enter the number:"))

def check_the_num(lower_val, upper_val, num):
    if num>=lower_val and num<=upper_val:
        print(f"The number {num} is in the range {lower_val}-{upper_val}.")

    else:
        print(f"The number is not in range {lower_val}-{upper_val}.")


check_the_num(lower_val, upper_val, num)