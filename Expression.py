import re

regexOperators = r"[-+*^/]"
regexElements = r"[+\-*()]|[A-Za-z]|[0-9]+"


class Expression:
    text = None
    elements = None
    operators = None
    operands = None
    variables = None

    def __init__(self, text):
        text = text.replace(" ", "")

        if not is_balanced(text):
            raise Exception("Unbalanced parentheses")

        self.text = text
        self.elements = re.findall(regexElements, text)
        self.operators = re.findall(regexOperators, self.text)
        self.operands = re.split(regexOperators, self.text)
        self.variables = [x for x in self.operands if x.isalpha()]

    def __str__(self):
        string = "\tInput: " + self.text + '\n'
        string += "\tOperators: " + str(self.operators) + '\n'
        string += "\tOperands: " + str(self.operands) + '\n'
        string += "\tVariables: " + str(self.variables)
        return string

def is_balanced(expr):
    stack = []
    elements = re.findall(r"[()]", expr)

    for el in elements:
        if el == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                return False
            stack.pop()

    return len(stack) == 0

def solve2degree(a, b, c):
    delta = b**2 - 4 * a * c
    if delta < 0: return None, None
    x1 = (-b + delta**(1/2)) / (2 * a)
    x2 = (-b - delta**(1/2)) / (2 * a)
    return x1, x2

def next_parentheses(elements):
    begin = end = -1
    stack = []

    for i in range(len(elements)):
        if elements[i] == '(':
            begin = i
            stack.append('(')
        elif elements[i] == ')':
            stack.pop()
            if len(stack) == 0:
                end = i
                break

    return begin, end
