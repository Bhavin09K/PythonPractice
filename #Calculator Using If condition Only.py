#Calculator Using If condition Only

print("1.Add")
print("2.Subtract")

while True:
    choice = input("What You Want To Do (1/2) : ")
    if choice in ('1','2'):
        x = float(input("Enter first number :"))
        y = float(input("Enter second number :"))

        if choice == '1':
            print("Sum = ",x+y)
        elif choice == '2':
            print("Difference = ", x-y)
            next_calculation = input("Another Calculation (yes/No) :")
            if next_calculation == 'No':
                break
    else:
        print("Invalid Input")
