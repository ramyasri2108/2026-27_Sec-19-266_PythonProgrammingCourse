n = int(input("Enter a number: "))
reversed_number = 0
while n > 0:
    digit = n % 10
    reversed_number = reversed_number * 10 + digit
    n //= 10
print(f"The reversed number is {reversed_number}")
