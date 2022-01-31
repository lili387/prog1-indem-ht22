
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

linus['vfu_studens'] = [victor, rafael]

teacher = []
teacher.append(linus)
teacher.append(rafael)
teacher.append(victor)

print(teacher)
