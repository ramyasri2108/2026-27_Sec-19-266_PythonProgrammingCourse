#1. using for loop
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    if i == 5:
        break
    print(i)

#2. using while loop
i = 1
while i <= n:
    if i == 5:
        break
    print(i)
    i += 1
