
numbers = [22, 45, 67, 12, 89, 34, 55, 90, 10]

max_number = numbers[0]
min_number = numbers[0]


for number in numbers:
    if number > max_number:
        max_number = number
    if number < min_number:
        min_number = number


print("Максимальное число:", max_number)
print("Минимальное число:", min_number)

