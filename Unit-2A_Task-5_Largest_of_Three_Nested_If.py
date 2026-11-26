First_num=float(input("Enter the First number: "))
Second_num=float(input("Enter the Second number: "))
Third_num=float(input("Enter the Third number: "))

if First_num >= Second_num:
    if First_num >= Third_num:
        largest = First_num
    else:
        largest = Third_num
else:
    if Second_num >= Third_num:
        largest = Second_num
    else:
        largest = Third_num

print(f"The largest number is:{largest}")
