import re

regexOperators = r'[-+*^/]'


class Expression:
    text = None
    operators = None
    operands = None
    variables = None

    def __init__(self, text):
        text = text.replace(" ", "")
        self.text = text
        self.operators = re.findall(regexOperators, self.text)
        self.operands = re.split(regexOperators, self.text)
        self.variables = [x for x in self.operands if x.isalpha()]

    def __str__(self):
        string = "\tInput: " + self.text + '\n'
        string += "\tOperators: " + str(self.operators) + '\n'
        string += "\tOperands: " + str(self.operands) + '\n'
        string += "\tVariables: " + str(self.variables)
        return string

    def solve2degree(a, b, c):
        delta = b**2 - 4 * a * c
        if (delta < 0): return(None, None)
        x1 = (-b + delta**(1/2)) / (2 * a)
        x2 = (-b - delta**(1/2)) / (2 * a)
        return(x1, x2)
