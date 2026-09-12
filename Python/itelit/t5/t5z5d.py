print("КАЛЬКУЛЯТОР")
a=int(input("Введіть перше число: "))
b=int(input("Введіть друге число: "))
dia=input("Напиши дію над цими числами (+, -, *, /), q вийти: ")

if dia == "q":
    print("Програму завершено")
    
elif dia == "-":
    print("Відповідь:",a-b)
elif dia== "+":
    print("Відповідь:",a+b)
elif dia== "/":
    print("Відповідь:",a/b)
elif dia== "*":
    print("Відповідь:",a*b)
