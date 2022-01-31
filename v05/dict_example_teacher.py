
linus = {}
linus['name'] = 'Linus'
linus['age'] = 40
linus['has_children'] = True

rafael = {}
rafael['name'] = 'Rafael'
rafael['age'] = 24
rafael['has_children'] = False

victor = {}
victor['name'] = 'Victor'
victor['age'] = 23
victor['has_children'] = False

teachers = []
teachers.append(linus)
teachers.append(rafael)
teachers.append(victor)

total_age = 0 
for teacher in teachers:
    total_age += teacher['age']

print (f'Jösses {total_age} år!!!')
print ('Jösses',total_age,'år!!!')
