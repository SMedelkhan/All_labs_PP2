import re

txt = "AhweAIJEfioSjoSii"

subbing = re.sub(r'(?<!^)([A-Z])', r' \1', txt)

print(subbing)
