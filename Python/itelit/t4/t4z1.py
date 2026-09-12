rik=1991
input_rik=int(input("В якому році проголошений Акт незалежності України? "))
if input_rik!=rik:
    try:
        input_rik
    except ValueError:
        print("Треба вказати рік")
    else:
        print("Ви відповіли не вірно!")
elif input_rik==rik:
    print("Ви відповіли вірно!")

