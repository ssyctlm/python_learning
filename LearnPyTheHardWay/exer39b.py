# ************ LPTHW edition4.0 exercise.40

cities = {
    'CA' : 'San Francisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville'
}

cities['NY'] = 'New Yourk'
cities['OR'] = 'Portland'

def find_city(themap,key):
    if key in themap:
        return themap[key]
    else:
        return "Not found"

#ok pay attention
cities['_find'] = find_city

while True:
    print("State? (Enter to quit) ",end='')
    state = input(">").upper()
    if not state:# if 这种 判断 True False 的，相当于加上了 bool，只要有值，而且值不是 0 就是 True
        # 例如： a= '' 或者 0 , if a :(返回False）, a=' ' 或者 a = 1 , a= '1' , if a:（返回都是True)
        break

    # this line is the most important ever! study!
    city_found = cities['_find'](cities,state)
    print( city_found )

for i,v in cities.items():
    print(i,v,end='/')

print(cities['_find'](cities,'CA'))



