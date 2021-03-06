# coding=utf-8
from Expression import *
import re

################# Regex elements #################
decomposedNumber = r'\([0-9]+(\^\([0-9]+(\*[0-9]+)*\))?(\*[0-9]+(\^\([0-9]+(\*[0-9]+)*\))?)*\)'
##################################################
regexFiles = [
    ('quadrado-da-soma.txt', 'QS'),
    ('quadrado-da-diferenca.txt', 'QD'),
    ('produto-da-soma-pela-diferenca.txt', 'PSD'),
    ('equacao-do-segundo-grau', 'ESG')
]

rules = []

for f in regexFiles:
    ff = open("regex/" + f[0], "r")
    rules.append((ff.readline(), f[1]))

print("- Rules:")
for rule in rules:
    print(rule)

print("\n- Expressions:")
while True:
    text = str(input())
    if text.upper() == 'END': break

    expression = None
    try:
        expression = Expression(text)
        print(expression)
    except Exception:
        print("\t- Unbalanced parentheses!!!")
        continue

    while True:
        b, e = next_parentheses(expression.elements)
        if b != -1:
            print("\t- Next Parentheses: ({0}, {1})".format(b, e))
            expression.elements.pop(e)
            expression.elements.pop(b)
        else:
            break

    for rule in rules:
        if re.match(rule[0], expression.text):
            print(expression.text + ' -> ' + rule[1])
            a = float(expression.operands[0])
            b = float(expression.operands[3]) if (len(expression.operands) > 4) else 0
            c = float(expression.operands[5]) if (len(expression.operands) > 5) else float(expression.operands[3]) if (len(expression.operands) == 4) else 0
            print("a = %.3g, b = %.3g, c = %.3g" % (a, b, c))
            x1, x2 = solve2degree(a, b, c)
            if x1 is None: print("Can't be factored")
            else: print(expression.text + " = a*(x - x1)*(x - x2) = %.3g*(x - %.3g)*(x - %.3g)" % (a, x1, x2))
            print()
