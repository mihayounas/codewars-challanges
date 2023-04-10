import re

def break_camel_case(s):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', s)


# transform - to camel case 

def to_camel_case(text):
    return re.sub('[-_](.)', lambda x: x.group(1).upper(), text)

# other solution

# def to_camel_case(text):
    # removed = text.replace('-', ' ').replace('_', ' ').split()
    # if len(removed) == 0:
     #   return ''
   # return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])
