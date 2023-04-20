# def name():
# 	print("My name is Abhishek sah")


# name()

# # Function is a block of code which only runs when its called
# # you can pass data , know as parameter , into a function
# # function can return data as a result:
# def myFunction():
# 	print("Hello from a  function")


# myFunction()

# def myName(name):
# 	print(name + " sah")


# myName("Abhishek")
# myName("avinash")
# myName("arvind")


# def children(*kids):
# 	print("The youngest child is " + kids[2])


# children("Ashish", "Abhishek", "Anish")


# def member(child1, child2, child3):
	# print("The youngest child is " + child2)


# member(child1= "Abhishek", child2="Anish", child3="avinash")
# # Return
# # Recursion
# def countryName(country  = "Norway"):
# 	 print("I am from " + country)


# countryName("Sweden")
# countryName("india")
# countryName()
# countryName("Brazil")

# def myFunction(x):
# 	return 5 * x


# print(myFunction(8))
# print(myFunction(5))
# print(myFunction(10))

   

# def myName():
# 	pass

# def countdown(n):
# 	print(n)
# 	if n == 0:
# 		return
# 	else:
# 		countdown(n-1)

def tri_recursion(k):
	if(k > 0):
		result = k+tri_recursion(k-1)
		print(result)
	else:
		result = 0
	return result    

print("\n\nRecursion Example results")
tri_recursion(6)



def factorial(x):

    if x== 1:

	    return 1
    else:
        return(x * factorial(x-1))


num = 10
print("The factorial of" ,num, "is", factorial(num))

#  Re- do 
def 
