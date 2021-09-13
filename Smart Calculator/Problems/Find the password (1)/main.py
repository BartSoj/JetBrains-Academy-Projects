from lxml import etree


def find_password(xml_string):
    root = etree.fromstring(xml_string)
    for item in root.iter():
        if "password" in item.keys():
            return item.get("password")
    return None
