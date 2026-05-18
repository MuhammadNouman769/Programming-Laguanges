def student(name , age, city):
    print(f' {name} is {age} years old and lives in {city}')
# positional arguments
student('Shanzy', 20, 'Karachi')
# keyword arguments
student(city='Karachi', name='Shanzy', age=20, )
print('--- Mixed Arguments ---')
student('Shanzy', age=20, city='Karachi')
