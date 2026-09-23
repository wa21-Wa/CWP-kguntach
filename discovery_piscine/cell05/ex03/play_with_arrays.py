array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = []

for num in array:
    if num > 5:
        result = num + 2
        if result not in new_array:
            new_array.append(result)

print(f"Original array: {array}")
print(f"New array: {new_array}")