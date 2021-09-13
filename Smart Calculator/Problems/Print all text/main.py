from lxml import etree

root = etree.fromstring(input())
for e in root:
    print(e.text)
