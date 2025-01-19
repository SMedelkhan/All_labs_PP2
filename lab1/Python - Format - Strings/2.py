#Placeholders and Modifiers

price = 59
txt = f"The price is {price} dollars"
print(txt)


#adding a colon : followed by a legal formatting type
#like .2f which means fixed point number with 2 decimals
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)


# Perform a math operation in the placeholder,
# and return the result
txt = f"The price is {20 * 59} dollars"
print(txt)