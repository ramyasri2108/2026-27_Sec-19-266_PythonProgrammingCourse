list_data = [5,4,3,3,2,1,5,4,2,1,7]
unique = []

for item in list_data:
    if item not in unique:
        unique.append(item)

print("Original:", list_data)
print("Without duplicates:", unique)
