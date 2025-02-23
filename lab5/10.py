import re

camel_str = "theCamelStringForExercise10"

# Convert camel case to snake case
snake_str = re.sub(r'([a-z])([A-Z])', r'\1_\2', camel_str).lower()

print(snake_str)
