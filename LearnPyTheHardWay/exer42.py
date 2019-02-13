# ex42: Is-A , Has -A , Objects and Classes

## Animal is-a object (yes, sort of confusing) look at the extra credit.
class Animal(object):
    pass

## ?? Dog is-a Animal
class Dog(Animal):
    def __init__(self, name):
        ## Dog has a name
        self.name = name

## Cat is-a Animal
class Cat(Animal):
    def __init__(self,name):
        ## Cat has a name
        self.name = name

## Person is-a object
class Person(object):
    def __init__(self,name):
        ## Person has-a name
        self.name = name

        ## Pet has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):
    def __init__(self, name, salary):
        ##  super() 函数是用于调用父类(超类)的一个方法。super 是用来解决多重继承问题的，
        # 直接用类名调用父类方法在使用单继承的时候没问题，但是如果使用多继承，会涉及到查找顺序（MRO）、
        # 重复调用（钻石继承）等种种问题。
        # class FooChild(FooParent):
        #     def __init__(self):
        #         #**super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类B的对象 FooChild 转换为类 FooParent 的对象**
        #         super(FooChild, self).__init__()
        #         print('Child')
        super(Employee,self).__init__(name)
        #That's how you can run the __init__ method of a parent class reliably. Go search for "python super" and read the
        # various advice on it being evil and good for you.

        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass

## Rover is-a Dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## mary has-a pet is-a satan
mary.pet = satan

## fank is-a employee,has-a name "Frank" and has-a salary 120000
frank = Employee("Frank",120000)

## frank has-a pet is-a rover
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a salmon
crouse =  Salmon()

## harry is-a halibut
harry = Halibut()

