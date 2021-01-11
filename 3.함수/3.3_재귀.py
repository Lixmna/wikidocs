def sumOfDigits(number) :
    if number < 10 :
        return number
    return sumOfDigits(int(number/10)) + number%10

digit = int(input())
answer = sumOfDigits(digit)
print(answer)