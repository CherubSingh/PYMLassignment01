def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

num = int(input("Enter a number: "))
print("The sum of the digits of the number is:", sum_of_digits(num))