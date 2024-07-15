# numbers=[20, 19, 31, 9, 14]
# print(type(numbers))
# print(numbers[0]) #accessing a value from a list
# print(numbers[1])
# numbers[1]=23 #updating a list value
# print(numbers)

# del numbers[2] #deleting a value from a list

# print(numbers)

# mixed_list=["john", 19, True, 50.00, [20, 49, 92]]
# print(mixed_list)
# print(type(mixed_list))
# print(mixed_list[-1][-2])
# print(len(mixed_list)) #return total numbers in an array
# new_numbers=[8,11,17]
# print(numbers+new_numbers) #concatenate
# print(numbers * 2) #repitation
# print("sam" in mixed_list) #check Number of a List items
# print(mixed_list[:2])
# print(mixed_list[1:]) #slicing a list
# print(len(numbers))
# mixed_list.append("Backend")
# print(mixed_list)
# mixed_list.append(89)
# print(mixed_list)
# print(mixed_list.pop())
# print(mixed_list)
# mixed_list.insert(-1, 42)
# mixed_list.remove(True)
# print(mixed_list)

#tuple Collection
"""
Note: Tuple are like Constant in Javascript They are the Final say of Value Given within the Array
"""

# number_tuple=(20, 12, 90, 81)
# mixed_tuple=("john", 90, 3.10, True, ["a", "b", "c"])
# print(number_tuple[0])
# print(number_tuple[-1])
# print(number_tuple)
# print(len(number_tuple))
# print("john" in mixed_tuple)
# if 6 > 2 : 
#     print("Six is Greater than Two")

# #set collection
# number_set={2, 4, 6, 8, 4, 5, 2, 5}
# number_set2={2, 4, 6, 8}
# print(number_set)
# number_set.add(7)
# print(number_set)
# set2={9,10,8}
# number_set.update(set2)
# print(number_set)
# number_set.remove(4)
# print(number_set)

# students={"john", "mike", "josh"}
# teachers={"henry", "emeka", "miracle"}
# univelcity= students | teachers #union
# num_sets=number_set & number_set2 #intersect
# print(univelcity)
# print(students)
# print(num_sets)

#dictionary collection
students={
    'name': 'mike',
    'age': 19,
    'courses': ['Frontend', 'Backend', 'Fullstack'],
    'address': {
    'street': 'montgomery',
    'lga': 'yaba',
    'state': 'Lagos',
    'postal_code': 102222
    },
    "is_admin": False
}

#accesing value from a dictionary 
print(students['name'])
print(students['courses'][1])
print(students['courses'][-2])
students['is_admin']= True #updating a value
print(students.get('phone'))
students.update({'postal_code': 4444})
# print(students)
students.pop("is_admin")
print(students.keys())
print(students.items())
print(students.values)
# print(students)