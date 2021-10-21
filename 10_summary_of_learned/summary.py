numbers = [1, 2, 3, 4, 5, 6, 7]

sum_of_numbers = 0

print("There is N numbers in numbers array: ", len(numbers))

for index in range(0, len(numbers)):
    print(numbers[index] % 2)
    if numbers[index] % 2 == 0:
      sum_of_numbers = sum_of_numbers + numbers[index]
    else:
      pass

print(sum_of_numbers)