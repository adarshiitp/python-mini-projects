while True:


    try:
        num1 = int(input("Enter Your number 1 = "))
        num2 = int(input("Enter Your number 2 = "))
    except ValueError:
        print("❌ Invalid input! Please enter only numbers.")
        continue

    print(f"Please Enter Which Calculaion you perform \nFor Addition Enter '+'\nFor Subtraction Enter '-'\nFor Multiplication Enter '*'\nFor Division Enter '/'\nFor Exponent Enter '**'\nFor Remainder Enter '%'")
    a = input("Enter 👉 ")

    match a:
        case "+":
            print(f"The Sum of {num1} and {num2} is = {num1+num2}")
        case "-":
            print(f"The Subtraction of {num1} and {num2} is = {num1-num2}")
        case "*":
            print(f"The Multiplication of {num1} and {num2} is = {num1*num2}")
        case "/":
            if num2 == 0:
                print("❌ Division by zero is not allowed.")
            else:
                print(f"The Division is = {num1 / num2:.2f}")
        case "**":
            print(f"The Exponent   is = {num1**num2}")
        case "%":
            print(f"The Remainder of {num1} and {num2} division is = {num1%num2}")
        case _:
            print("❌ Invalid operation. Please enter a valid symbol.")

    choice = input("Do you want to calculate again? (yes/no): ").lower()
    if choice != "yes":
        print("Thanks for using this Calculator. Goodbye! 👋")
        break