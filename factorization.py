from Expression import Expression
import re

# a^2-b^2
# rule1 = ['a','^','2','-','b','^','2']
# rule2 = ['a','^','2','-','a','b','^','2']
rules = [
    # ('\(([0-9]*(\*[0-9]+)*(\*[A-Za-z])?|[A-Za-z])\+([0-9]*(\*[0-9]+)*(\*[A-Za-z])?|[A-Za-z])\)\^(2|\(2(\*[0-9]+)*\))',
    #  'quadrado da soma'),     ERRADO: (a + b)^2
    ('([0-9]+|[A-Za-z]|\(([0-9]+\*)*([0-9]+|[A-Za-z])\))\^(2|\(2(\*[0-9]+)\))([+-].+)*-([0-9]+|[A-Za-z]|\((['
     '0-9]+\*)*([0-9]+|[A-Za-z])\))\^(2|\(2(\*[0-9]+)\))', 'produto da soma pela diferença')
]
print("- Rules:")
# while True:
#     rule = input()
#     if rule.upper() == "END":
#         break
#     rules += [list(rule)]
for rule in rules:
    print(rule)

print("\n- Expressions:")
while True:
    text = input()
    if text.upper() == 'END':
        break
    expression = Expression(text)
    print(expression)

for rule in rules:
    if re.match(rule[0], expression.text):
        print(expression.text + ' -> ' + rule[1])
