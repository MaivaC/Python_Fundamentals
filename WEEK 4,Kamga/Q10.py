

person = {'name': 'Jane', 'city': 'New York'}
salary=person.get('salary', 'NAN')

print(person.get('city'))

'''If the key doesn't exist it returns none or a specified default value.
For example'''

print(person.get('Salary')) #using the default valaue
print(salary) #using a specified value