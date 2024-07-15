a = 20
b =  40
if a > b :
    print(a -b)
    print("yes a a is bigger than b")
elif a == b:
    print(a + b)
    print("a is equal to b")
else:
    print("a is not bigger or equal to b")

#iterations
i = 1
while i < 6:
    i +=1
    if i == 3:
        continue
    print(i)
    print("i am running a while loop")

i = 1
while i < 6:
    i +=1
    if i == 3:
        break
    print(i)
    print("i am running a while loop")

mgNum = int(input("Guess The Magic Number"))

while mgNum !=5:
    print("wrong Try again")
    mgNum = int(input("Enter a Number: "))

else:
    print("You're a Genius, That's the Magic Number")

# num = int(input("Enter a Number"))

# while num !=3:
#     print("wrong Number please try again")
#     num = int(input("Enter a Number: "))
# else:
#     print("Yes you are right")