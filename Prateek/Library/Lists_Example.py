
dogs = ['Roger','Syd','tommy']

print('Roger' in dogs)
# cats = []
print(dogs[1])
print(dogs.index('Syd'))

print(dogs.index('Syd'))

print(dogs[-1])
print(dogs[0:2])
print(dogs[2:])

dogs.append('cutie')
# dogs.extend('yum')
dogs.insert(1,'doggy')
print(dogs)


extend_list = []

extend_list.extend([1,2])
print(extend_list)

extend_list.extend((10,11))
print(extend_list)

# extend_list.extend("ABC")
# print(extend_list)
dogs.sort()
print(dogs)

cats = ('meow','waffle')
print(cats.index('meow'))

newcats = cats + ('tree','opo')
print(newcats)

dog = {'name':'tommy', 'age':5}

print(dog['name'])
print(dog['age'])

dog['name'] = 'Roger'
print(dog)

print(dog.get('name'))

# dog.pop('name')
# print(dog)

# dog.popitem()
# print(dog)

print(list(dog.keys()))
print(list(dog.values()))


# dog1 = {}

dog1 = dog.copy()
print(dog1)

del dog1['name']
print(dog1)