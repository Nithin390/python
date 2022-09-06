def addition_two_numbers(num1, num2):
    return num1 + num2
def subtraction_two_numbers(num1, num2):
    return num1 - num2
def multiplication_two_numbers(num1, num2):
    return num1*num2
def division_two_numbers(num1, num2):
    return float(num1)/float(num2)
print("Enter the Two Numbers:")
num1 = int(input())
num2 = int(input())
add = addition_two_numbers(num1, num2)
sub = subtraction_two_numbers(num1, num2)
multi = multiplication_two_numbers(num1, num2)
division = division_two_numbers(num1, num2)
print("Addition of two Numbers is: ", add)
print("Subtraction of two Numbers is: ", sub)
print("Multiplication of two Numbers is: ", multi)
print("Division of two Numbers is: ", division)
