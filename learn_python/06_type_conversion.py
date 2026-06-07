''' ============= Type conversion ================ '''

# python may do tarha hai type conversion hota hai implicit or explicit

# implicit program k hisab se data ki type ko auto convert kr deta hai 

a = 10
b = 2.3
c = a + b
print(type(c))

# explicit may manualy data type ko apne hisab se convert krte hain
print(4 + int('4'))
d = 3
b = 4.4
print(d + int(b))

s = 3j
u = 3
print(str(s) + str(u))
# print(float(s) + float(u))