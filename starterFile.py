#Your code goes here. 

import math

def safe_divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Cannot divide by zero"


def process_list(input_list):
    total=0
    for element in input_list:
        try:
            number = int(element)
            total += number**2
        except(ValueError, TypeError):
            continue
    return total


def nested_operations(a, b):
    try:
        num1=int(a)
        num2=int(b)

        try:
            divisionresult=num1/num2
            result=math.sqrt(divisionresult)
            return result
        except ZeroDivisionError:
            return "Cannot divide by zero"
    except ValueError:
        return "Invalid input:non-numeric value provided"



def process_input():
    try:
        userinput=input("Please enter a number:")
        number=float(userinput)

        result = number **2
    except ValueError:
        print("Invalid input: Please enter a valid number.")
        return None
    else:
        print(f"The result of the number is:{result}")
        return result
    finally:
        print("Processing complete!")
    

def main():
    print(safe_divide(5, 7))
    print(process_list([3, 5, 8, 10]))
    print(nested_operations(3, 6))
    (process_input())

main()

