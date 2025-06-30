# Write a calculator CLI tool
def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

def main():
    while True:
        print("CLI Calculator")
        print("Select Operation")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        choice=input("Enter a choice (1-5)")

        if choice=="5":
            print("Existing Calculator")
            break

        if choice not in ('1','2','3','4'):
            print("Invalid Choice. Try again")
            continue

        try:
            x=float(input("Enter the first number:"))
            y=float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers")
            continue

        if choice=='1':
            print("Result: ",add(x,y))
        elif choice=='2':
            print("Result: ",subtract(x,y))
        elif choice=='3':
            print("Result: ",multiply(x,y))
        elif choice=='4':
            print("Result: ",divide(x,y))

if __name__=="__main__":
    main()