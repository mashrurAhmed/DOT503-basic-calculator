from Calculator import Calculator


def check_operation_list(calc_list):
    if(len(calc_list) != 3):
        return False
    if(calc_list[1] != '+' and calc_list[1] != '-' and calc_list[1] != '*' and calc_list[1] != '/'):
        return False
    return True

if __name__ == "__main__":
    calculator = Calculator()
    calc_string = ""
    while calc_string != "N":
        calc_string = input("Enter numbers to input: ")
        if(calc_string == "N"):
            break
        calc_list = calc_string.split(' ')
        if (check_operation_list(calc_list) == False):
            print("Invalid input given.")
            continue
        result = calculator.calculate(calc_list)
        print(result)
