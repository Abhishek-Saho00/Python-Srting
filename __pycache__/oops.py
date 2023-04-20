class DemoClass:
	# define function and variable inside a class
	a = 10
	def sumvalue(self):
		print(10+21)


men = DemoClass()
men1 = DemoClass()
print(men1.a)
print(men.a)

men.sumvalue()
#  Class and Obect 
class MyClass:
 	x = 11

value = MyClass()
print(value.x)


class Person:
	def __init__(self,name,age,adress):
		self.name = name
		self.age = age
		self.adress = adress

info = Person("Abhishek sah", 23, "ktm, nepal")

print(info.name)
print(info.age)
print(info.adress)



