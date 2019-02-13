p = (4,5)
print('p = (4,5)')
x,y = p
print('x,y = p')
print('x :',x)
print('y :',y)
print('-'*10)

data = ['ACME',50,90.1,(2012,12,21)]
print("data = ['ACME',50,90.1,(2012,12,21)]")
name,shares,price,date = data
print("name,shares,price,date = data")
print('name :',name)
print('date :',date)
name,shares,price,(year,mon,day) = data
print("name,shares,price,(year,mon,day) = data")
print('name :',name)
print('year :',year)
print('mon :',mon)
print('day :',day)

print('-'*10)
s = 'Hello'
print('s = \'Hello\'')
a,b,c,d,e = s
print("a,b,c,d,e = s")
print('a :',a)
print('e :',e)
