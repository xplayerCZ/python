from random import randint


class Equation:
    def __init__(self, equation):
        self.body = equation
        self.result = eval(equation)
        self.userInput = None


def get_operand(index):
    if index == 0:
        return "+"
    if index == 1:
        return "-"
    if index == 2:
        return "*"
    return " "


def generate_equations(count, difficulty_level):
    equations = []
    for i in range(0, count):
        equations.append(generate_equation(difficulty_level))
    return equations


def generate_equation(difficulty_level):
    if difficulty_level == 1 or difficulty_level == 2:
        operand = randint(0, 1)
        if difficulty_level == 1:
            first_number = randint(0, 9)
            second_number = randint(0, 9)
        else:
            first_number = randint(0, 99)
            second_number = randint(0, 99)

    if difficulty_level == 3 or difficulty_level == 4:
        operand = randint(0, 2)
        if difficulty_level == 3:
            if operand > 1:
                first_number = randint(0, 9)
                second_number = randint(0, 9)
            else:
                first_number = randint(9, 99)
                second_number = randint(9, 99)
        else:
            if operand > 1:
                first_number = randint(9, 49)
                second_number = randint(9, 49)
            else:
                first_number = randint(9, 99)
                second_number = randint(9, 99)

    return Equation(f"{first_number} {get_operand(operand)} {second_number}")


def show_equations(equations):
    for equation in equations:
        equation.userInput = input(f"{equation.body} = ")


def show_results(equations):
    print("Tvoje výsledky:")
    for equation in equations:
        result = "Správně!" if int(
            equation.userInput) == equation.result else f"Špatně. Správný výsledek je {equation.result}"
        print(f"{equation.body} = {equation.userInput} {result}")


print(
    """ 
    Berte prosím v potaz, že zatím nefunguje kontrola vstupů. Proto zadávejte číselné hodnoty a hodnoty ve správných intervalech.
    Program rovněž není nejlépe vyladěný ani nejlépe napsaný. Děkuji za přečtení této zprávy!
    """
)
print("Vítejte v generátoru příkladů!")
numberOfEquations = int(input("Zvolte prosím počet zadání. "))
difficulty = int(input("Zvolte obtížnost 1 až 4. Obtížnost 1 a 2 obsahují pouze + a -. Obtížnosti 3 a 4 obsahují také *. "))

calculableEquations = generate_equations(numberOfEquations, difficulty)
show_equations(calculableEquations)
show_results(calculableEquations)
