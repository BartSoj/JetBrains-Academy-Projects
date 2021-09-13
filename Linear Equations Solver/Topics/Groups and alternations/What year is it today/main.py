import re

# put your regex in the variable template
template = r"(\d{1,2}/\d{1,2}/|\d{1,2}\.\d{1,2}\.)(\d{4})"
string = input()
match = re.match(template, string)
print(match.group(2) if match else None)
