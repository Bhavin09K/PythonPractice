# Calculator using if condition and function

def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def divide(x,y):
    return x/y
def multiply(x,y):
    return x*y

print("Select Operation: ")
print("1.Add")
print("2.Subtarct")
print("3.Divide")
print("4.Multiply")

condition = True

while (condition):
    choice = input("Enter Choice 1/2/3/4 : ")
    if choice in ('1','2','3','4'):
        a = float(input("Enter first number: "))
        b = float(input("Enter Secont number: "))

        if choice == '1':
            print("a","+","b :" ,add(a,b))
        elif choice == '2':
            print("a","-","b :" ,subtract(a,b))   
        elif choice == '3':
            print("a","/","b :" ,divide(a,b))
        elif choice =='4':
            print("a","*","b :" ,multiply(a,b))

        condition_check = input("Do you want to continue: (yes/no) : ")  
        if condition_check == "yes":
            condition == True
        elif condition_check =="no":
            condition == False
            break
    else:
        print("Invalid Input")                   





