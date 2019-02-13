# ex39: Dictionaries, Oh Lovely Dictionaries 字典啊可爱的字典
things = ['a','b','c','d']
print(things[1])
things[1] = 'z'
print(things[1])
print(things)

stuff = {'name':'Zed','age': 36, 'height': 6*12+2}
print(stuff['name'])
print(stuff['age'])
print(stuff['height'])

stuff['city'] = "San Francisco"
print(stuff['city'])

stuff[1] = "Wow"
stuff[2] = "Neato"
print(stuff[1])
print(stuff[2])
print(stuff)

del stuff["city"]
del stuff[1]
del stuff[2]
print(stuff)

print("________exercise39____________\n\n\n")
# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan':'MI'
}

#create a basic set of states and some cities in them
cities = {
    'CA' : 'San Francisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-'*10)
print('NY State has:',cities['NY'])
print('OR State has:',cities['OR'])

# print some states
print('-'*10)
print("Michigan's abbreviation is: ",states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('-'*10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ",cities[states['Florida']])

# print every state abbreviation
print('-'*10)
for state, abbrev in states.items():
    #print("{} is abbreviated {}",format(state,abbrev))
    print("%s is abbreviated %s" %(state, abbrev))

# print every city in state
print('-'*10)
for abbrev, city in cities.items():
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-'*10)
for state, abbrev in states.items():
    #  dict.items( ): list of dict's (key,value) pairs, as 2-tuples / 返回一个包含字典中（键，值）对元组的列表
    #print("{} state is abbreviated {} and has city {}".format(state,abbrev,cities[abbrev]))
    print("%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev]))

print('-'*10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas',None)

if not state:
    print("Sorry, no Texas")

# get a city with a default value
city = cities.get('TX','Does Not Exist')
# Python 字典(Dictionary) get() 函数返回指定键的值，如果值不在字典中返回默认值。
# get()方法语法：dict.get(key, default=None)
print(f"The city for the state 'TX' is : {city}")



