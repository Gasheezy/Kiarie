def multiply_2_pure (numbers):
    new_numbers = []
    for n in numbers:
        new_numbers.append (n*2)
    return new_numbers

original_numbers = [11, 20, 43, 14, 35]
changed_numbers = multiply_2_pure (original_numbers)

print (original_numbers)
print (changed_numbers)