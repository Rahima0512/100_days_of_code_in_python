#Calculator
#ADD
def add(n1,n2):
    return n1+n2
#SUBTRACT
def sub(n1,n2):
    return n1-n2
#MULTIPLY
def mul(n1,n2):
    return n1*n2
#DIVIDE
def div(n1,n2):
    return n1/n2

Operations={'+':add,'-':sub,'*':mul,'/':div}
continue1='y'
def calculator_func():
    num1 = float(input("Enter the first number\t"))
    num2 = float(input("Enter the second number\t"))

    for key in Operations:
        print(key)
    symbol = input("Enter the operation to be performed:\t")

    func_perform = Operations[symbol]
    answer = func_perform(num1, num2)
    print(f"\t {num1} {symbol} {num2}\t=\t {answer}")
while(continue1=='y'):
    calculator_func()
    continue1=input("Do you wanna continue? y/n\t")

