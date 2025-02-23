import re

snake_str = "The_snake_code_style_for_exersize_7"
def replace_underscore(match):
    return match.group(1).upper()

camel_str = re.sub(r'_(.)', replace_underscore, snake_str)
print(camel_str) 