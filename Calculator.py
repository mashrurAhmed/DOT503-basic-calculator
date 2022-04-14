

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num1, num2):
        self.result = num1 + num2
        return self.result

    def substract(self, num1, num2):
        self.result = num1 - num2
        return self.result

    def multiply(self, num1, num2):
        self.result = num1 * num2
        return self.result

    def divide(self, num1, num2):
        self.result = num1 / num2
        return self.result

    def calculate(self, input_list):

        num1 = float(input_list[0])
        num2 = float(input_list[2])
        if(input_list[1]) == '+':
            self.result = self.add(num1, num2)
        elif(input_list[1]) == '-':
            self.result = self.substract(num1, num2)
        elif(input_list[1]) == '*':
            self.result = self.multiply(num1, num2)
        elif(input_list[1]) == '/':
            self.result = self.divide(num1, num2)
        else:
            print("Invalid operator")
        return self.result

    def getresult(self):
        return self.result
