text = "2976fbvbuhdbv47347f378q@#$%^&*()hdff"

digits = ''
alpha = ''
speciel = ''

for i in text:
    if i.isdigit():
        digits = digits+i
    elif i.isalpha():
        alpha = alpha+i
    else:
        speciel = speciel+i    
print(f" Digits - {digits} Alpha - {alpha} speciel {speciel}")