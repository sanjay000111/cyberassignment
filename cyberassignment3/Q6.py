def blackjack(num1,num2,num3):
    sum = num1+ num2+ num3
    if sum<=21:
        return sum
    elif sum>21 and (num1==11 or num2==11 or num3==11):
        sum -= 10
        if sum > 21:
            return "Bust"
        else:
            return sum
    else:
        return "Bust"

print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))