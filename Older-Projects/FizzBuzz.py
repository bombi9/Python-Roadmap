numero = int(input("Enter a number you fizzy buzz: "))

def FizzBuzz(number):
    lolac = number % 3
    bobac = number % 5
    if lolac == bobac:
        return "FizzBuzz"
    elif lolac == 0:
        return "Fizz"
    elif bobac == 0:
        return "Buzz"
    else:
        return number

print("The Ultimate FizzBuzz() challenger iiiis: ")
print(FizzBuzz(numero))