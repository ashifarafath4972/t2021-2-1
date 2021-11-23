a = float(input("type a : "))
b = float(input("type b : "))
op_type = input("type operation type : ")

class Calculator():
    def operation(self,a,b,op_type):
        if op_type == 'addition':
            print(a+b)
        elif op_type == 'subtraction':
            print(a-b)
        elif op_type == 'multiplication':
            print(a*b)
        elif op_type == 'division':
            print(a/b)
        else:
            print("Please type correct operation")

class_object = Calculator()
class_object.operation(a,b,op_type)