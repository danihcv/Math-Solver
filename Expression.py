import re

class Expression:

    text = None
    operands = None
    variables = None
    numbers = None

    def __init__(self, text):
        self.text = text
        self.operands = re.split(r'-|\+|\*|\^', self.text)
        self.variables = [x for x in self.operands if x.isalpha()]

    def __str__(self):
        string = ""
        string += self.text + '\n'
        string += str(self.operands) + '\n'
        string += str(self.variables) + '\n'
        return string
