import re

def break_camel_case(s):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', s)
