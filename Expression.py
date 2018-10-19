import re

regexOperators = r'[-+*^/]'


class Expression:
    text = None
    operators = None
    operands = None
    variables = None

    def __init__(self, text):
        self.text = text
        self.operators = re.findall(regexOperators, self.text)
        self.operands = re.split(regexOperators, self.text)
        self.variables = [x for x in self.operands if x.isalpha()]

    def __str__(self):
        string = "\tInput: " + self.text + '\n'
        string += "\tOperators: " + str(self.operators) + '\n'
        string += "\tOperands: " + str(self.operands) + '\n'
        string += "\tVariables: " + str(self.variables) + '\n'
        return string
