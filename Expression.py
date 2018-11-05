import re

regexOperators = r'[-+*^/]'
regexElements = r'[+\-*()]|[A-Za-z]|[0-9]+'


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

    def solve2degree(self, a, b, c):
        delta = b**2 - 4 * a * c
        if (delta < 0): return(None, None)
        x1 = (-b + delta**(1/2)) / (2 * a)
        x2 = (-b - delta**(1/2)) / (2 * a)
        return(x1, x2)

def formTree(expr):
    elements = re.findall(regexElements, expr)
    # print(elements)

def is_balanced(expr):
    stack = []
    elements = re.findall(r'[()]', expr)
    print(elements)

    for el in elements:
        print('>>>>' + str(el == '('))
        if el == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                return False
            stack.pop()

    return len(stack) == 0
