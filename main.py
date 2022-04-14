from Calculator import Calculator


if __name__ == "__main__":
    calculator = Calculator()
    calc_string = ""
    while calc_string != "Q":
        calc_string = input(
            "Enter numbers to input (Refer to README for format of input): ")
        if(calc_string == "Q"):
            break
        result = calculator.calculate(calc_string)
        print(result)
    print(("Last calculation result: {}\nEnd of program").format(
        calculator.getresult()))
