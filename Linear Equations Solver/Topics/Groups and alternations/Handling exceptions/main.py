import re

# put your regex in the variable template
template = "(Value|Name|Type)Error"
string = input()
match = re.match(template, string)
print(match.group(1) if match is not None else None)
