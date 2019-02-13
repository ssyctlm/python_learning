#ex44:Inheritance vs Composition
# -*- coding:utf-8 -*-

## Implicit Inheritance
class Parent (object):
	
	def implicit(self):
		print('PARENT implicit()')
		
class Child (Parent):
	pass
	
dad = Parent()
son = Child()

dad.implicit()
son.implicit()

## Override Explicitly
class Child2(Parent):
	def implicit(self):
		print("I overrided this Method(function)")

son2 =Child2()

dad.implicit()
son2.implicit()

## Alter Before Or After (在之前或者之后更改）
print("\n")

class Baba:
	def altered(self):
		print(" BABA altered()")

class Erzi(Baba):
	def altered(self):
		print("ERZI, b4 BABA altered()")
		super(Erzi, self).altered( ) # 带着erzi , self 去爹爹那里继承 altered（）方法
		# The explaination in the tuition :You should be able to read this as "call
		# super with arguments Child and self, then call the function altered on whatever it returns"
		print("ERZI, after BABA altered()")

baba = Baba()
erzi = Erzi()

baba.altered()
erzi.altered()

## All athree Combine
class Parent (object):
	
	def override(self):
		print("PARENT override()")
		
	def implicit(self):
		print("PARENT implicit()")
		
	def altered(self):
		print("PARENT altered()")
		
class Child (Parent):
	
	def override(self):
		print("CHILD override()")
		
	def altered(self):
		print("CHILD, BEFORE PARENT altered()")
		super(Child,self).altered()
		print("CHILD, AFTER PARENT altered()")

print(' ')		
dad = Parent()
son = Child()
print(' ')		
dad.implicit()
son.implicit()
print(' ')		
dad.override()
son.override()
print(' ')		
dad.altered()
son.altered()

## The reason for super()
class Child(Parent):
	
	def __init__(self,stuff):
		self.stuff = stuff
		super(Child,self).__init__()
		
		
## Composition
class Other (object):
	
	def override(self):
		print('OTHER override()')
		
	def implicit(self):
		print('OTHER implicit()')
	
	def altered(self):
		print('OTHER altered()')
		
class Child(object):
	
	def __init__(self):
		self.other = Other()
		
	def implicit(self):
		self.other.implicit()
		
	def override(self):
		print('CHILD override')
		
	def altered(self):
		print('CHILD, BEFORE altered()')
		self.other.altered()
		print('CHILD, AFTER altered()')
		
son = Child()

son.implicit()
son.override()
son.altered()
		
		
