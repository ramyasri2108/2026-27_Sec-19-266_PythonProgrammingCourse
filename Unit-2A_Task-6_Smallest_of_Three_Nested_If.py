First_num=float(input("Enter the First Number: "))
Second_num=float(input("Enter the Second Number: "))
Third_num=float(input("Enter the Third Number: "))

if First_num <= Second_num:
    if First_num <= Third_num:
        smallest=First_num
    else:
        smallest=Third_num
else:
    if Second_num <= Third_num:
        smallest=Second_num
    else:
        smallest=Third_num

print(f"The smallest number is:{smallest}")
