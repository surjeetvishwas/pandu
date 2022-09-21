print('''
Calculator
''')

num1=eval(input("Enter your Number 1: "))
num2=eval(input("Enter your Number 2: "))
opr=input("Enter your Operation: ")

if opr==('+'):
    print(num1+num2)
elif opr==('-'):
    print(num1-num2)
elif opr==('*'):
    print(num1*num2)
elif opr==('/'):
    print(num1/num2)
else :
    print("invalid Opertion")



