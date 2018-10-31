from Expression import Expression
import re

# a^2-b^2
# rule1 = ['a','^','2','-','b','^','2']
# rule2 = ['a','^','2','-','a','b','^','2']
rules = [
    # ('\(([0-9]*(\*[0-9]+)*(\*[A-Za-z])?|[A-Za-z])\+([0-9]*(\*[0-9]+)*(\*[A-Za-z])?|[A-Za-z])\)\^(2|\(2(\*[0-9]+)*\))',
    #  'quadrado da soma'),     ERRADO: (a + b)^2
    ('([0-9]+|[A-Za-z]|\(([0-9]+\*)*([0-9]+|[A-Za-z])\))\^(2|\(2(\*[0-9]+)\))([+-].+)*-([0-9]+|[A-Za-z]|\((['
     '0-9]+\*)*([0-9]+|[A-Za-z])\))\^(2|\(2(\*[0-9]+)\))', 'produto da soma pela diferença'),
    (r'(\+?\-?[0-9]+\*x\^2)(\+?\-?[0-9]+\*x)?(\+?\-?[0-9]+)?', 'equação do segundo grau')
]
print("- Rules:")
for rule in rules:
    print(rule)

print("\n- Expressions:")
while True:
    text = input()
    if text.upper() == 'END': break
    expression = Expression(text)
    print(expression)

    for rule in rules:
        if re.match(rule[0], expression.text):
            print(expression.text + ' -> ' + rule[1])
            a = float(expression.operands[0])
            b = float(expression.operands[3]) if (len(expression.operands) > 4) else 0
            c = float(expression.operands[5]) if (len(expression.operands) > 5) else float(expression.operands[3]) if (len(expression.operands) == 4) else 0
            print("a = %.3g, b = %.3g, c = %.3g" % (a, b, c))
            x1, x2 = Expression.solve2degree(a, b, c)
            if (x1 is None): print("Can't be factored")
            else: print(expression.text + " = a*(x - x1)*(x - x2) = %.3g*(x - %.3g)*(x - %.3g)" % (a, x1, x2))
            print()
