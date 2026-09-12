a=int(input("Введіть a: "))
try:
    rez=a*b
except NameError:
    print("NameError: Змінна b не визначена")
else:
    print("Помилок немає!")
finally:
    print("Программа коректно завершила свою роботу")
    
    
