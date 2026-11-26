n = int(input("Enter a 3-digit number: "))
original_number = n
sum_of_cubes = 0
while n > 0:
    digit = n % 10
    sum_of_cubes += digit ** 3
    n //= 10
if sum_of_cubes == original_number:
    print(f"{original_number} is an Armstrong number.")
else:
    print(f"{original_number} is not an Armstrong number.")
