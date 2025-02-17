45
grades = list(map(int, input("Введите список оценок через пробел: ").split()))


even_count = 0
odd_count = 0


def grade_to_letter(grade):
    if grade >= 90:
        return 'A', 'Сдал'
    elif grade >= 80:
        return 'B', 'Сдал'
    elif grade >= 70:
        return 'C', 'Сдал'
    elif grade >= 60:
        return 'D', 'Сдал'
    else:
        return 'F', 'Не сдал'


for grade in grades:
    letter, status = grade_to_letter(grade)
    
  
    if grade % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    print(f"Балл: {grade} -> Оценка: {letter} ({status})")


print(f"\nЧетных оценок: {even_count}")
print(f"Нечетных оценок: {odd_count}")
