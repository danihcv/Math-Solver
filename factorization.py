from Expression import Expression

# a^2-b^2
# rule1 = ['a','^','2','-','b','^','2']
# rule2 = ['a','^','2','-','a','b','^','2']
rules = []
while (True):
    rule = input()
    if (rule == "END"): break
    rules += [list(rule)]
for rule in rules:
    print(rule)

text = input()
expression = Expression(text)
print(expression)