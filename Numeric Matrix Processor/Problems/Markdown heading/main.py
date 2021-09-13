def heading(text, heading_level=1):
    if heading_level < 1:
        heading_level = 1
    elif heading_level > 6:
        heading_level = 6
    return "#" * heading_level + " " + text
