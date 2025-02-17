
grade = int(input("Введите вашу оценку за тест (0-100): "))


if grade < 0 or grade > 100:
    print("Оценка должна быть в диапазоне от 0 до 100!")
else:
    
    if grade >= 90:
      
        homework_done = input("Вы сдали все домашние задания? (да/нет): ").lower()
        if homework_done == "да":
            print("Отлично! Оценка: A+")
        else:
            print("Хорошая работа, но сдайте все задания! Оценка: A")
    
    elif 80 <= grade < 90:
        
        attendance = input("Вы посещали более 75% занятий? (да/нет): ").lower()
        if attendance == "да":
            print("Хорошо! Оценка: B")
        else:
            print("Нужно посещать занятия! Оценка: C")
    
    else:
        print("Старайтесь лучше!")
