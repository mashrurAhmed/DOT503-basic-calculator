from Calculator import Calculator


if __name__ == "__main__":
    calculator = Calculator()
    calc_string = ""
    while calc_string != "N":
        calc_string = input("Enter numbers to input: ")
        if(calc_string == "N"):
            break
        result = calculator.calculate(calc_string)
        print(result)
