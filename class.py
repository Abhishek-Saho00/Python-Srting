# class Person:
# 	def __init__(self, name, adress):
# 		self.name = name
# 		self.adress = adress
# 		print("HI i am a programmer")

# 	def info(self):

# 		print("i am a Studnets" + self.adress + self.name)



# a = Person("abhishek", "  and i am currently live in koteshwor ")
# a.name= " Abhishek sah"
# a.adress = " koteshwor"
# a.info()

class default:
	name = "Abhishek sah"
	age = 23

	def __init__(self):
		adress = "ktm 446000"

		print("Hi i am Abhishek sah from NEpal", adress , self.name, self.age)

o = default()
# Encapsulation..

class display:
	__a = 10
	# private 
	_b = 20
	# protected
	def Value(self):

		print("a is ", self.__a, self._b)

obj = display()
obj.Value()

