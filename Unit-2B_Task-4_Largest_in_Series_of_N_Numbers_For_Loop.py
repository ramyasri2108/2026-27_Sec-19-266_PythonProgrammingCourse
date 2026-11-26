total_input_numbers = int(input("Enter how many numbers: "))

largest = float(input("Enter a number: "))

for count in range(total_input_numbers - 1):
    num = float(input("Enter a number: "))
    if num > largest:
        largest = num

print(f"Largest among {total_input_numbers} numbers is {largest}")
