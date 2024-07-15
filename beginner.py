# def joshua():
#     print("step one")
#     print("step two")
# print("step three")
# print("standalone print")
# joshua("")

# num = 5
# num2 = 4.0
# isStudent=True
# print(num + num)

# print(7 + num)
# name= "henry"

# print(name)
# print("welcome " + name)

# first_class = "Welcome to Python Class June"
# print(first_class)

# num = 9 #int
# price=20.00 # float
# is_student=False #boolean
# gender="male" #string
# numbers=[30, 12, 1, 18] #list
# grades =("A", "B", "C", "D") #tuple
# scores = {"a":20, "b":12} #dict
# age_set = {20, 19, 18} #set



# print(type(price))
# print(type("this"))
# first_name=input("enter your Name: ")
# second_name=input("enter your name mf: ")
# info=" Hope you Know MF Means MotherFvcker😂"
# print(first_name + second_name + info )
# MF="Therefore that Makes you a Big a$$ Motherfvcker "
# take_note="this is just a Coding Drill So Don't take whatever that's displayed here to heart"
# print( MF + take_note )

# int()
# str()
# float()
# bool()
# list()

# print(int('10'))
# t_numbers=tuple(numbers)
# print(t_numbers)

#simple basic calculator
# first_number=int(input('enter the first number: '))
# first_number=input('enter the first number: ')
# second_number=input('enter the second number: ')
# second_number=int(input('enter the second number: '))
# print(int(first_number) + int(second_number))
# print(first_number + second_number)
# print( first_number // second_number)
# print( first_number + second_number)
# print( first_number - second_number)
# print( first_number % second_number) 

# true or false Print
print(2**3) 
print(5 == 5) #true
print(5 == 7)#false
print(6 > 2)#true
print(4 < 1)#false
print(2 > 4 and 5 == 5)
print(4 > 2 or 4 == 6)
print(not 6 == 5 or 2 < 6)

x=5
y=7
print(x is not y)
print(y - x)

# Indexof Print
# a="Welcome to Class"

# print(a[2])
# print(a[0])
# print(a[0:5]) #slicing a string
# print(a[0:7:2]) #slicing a string with a step
# print(a[0:]) #slicing a string from the start to the end
# print(a[:7]) #slicing a string from the start to the 7th index
# print(a[7:]) #slicing a string from the 7th index to the end
# print(a[:]) #slicing a string from the start to the end
# sch="welcome to backend with django class"
# print(sch[24: ])
# print(sch[-12:])
# print("frontend" in sch )
# print(sch[24:36])

age=17
name="Joshua"
course="Backend"
lang="python"
sch="%s is %d years old and he is studying %s with %s"%(name, age, course, lang)
print(sch)
sch2="{} is {} years old and he is studying {} with {}".format(name , age, course, lang)
print(sch2)
sch3=f"{name} is {age} year old and she is studying {course} with {lang}"
print(sch3.lower()) 
print(sch3.upper()) 
print(sch3.endswith("python")) 
print(sch3.capitalize()) 
print(sch3.title()) 