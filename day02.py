# function , loop , if else and elif
def sayHello():
    print("Hello Mayur Adlak")
# sayHello()

def printName(name):
    #parameterized function
    print(f"Hello {name}")
# printName("Mayur Adlak")

def addNumbers(a, b):
    return int(a) + int(b)

# result = addNumbers("13", "5")
# print("Sum of numbers ", result)

def para(self,**kwargs):
    for key, value in kwargs.items():
        print(f"key : {key} , value : {value}")


def ArgEx(self,**args):
    print("Args  : ",args)
# para(self=1,a=2,b=3)

# ArgEx(self=1,a=2,b=3)
'''
start: SupportsIndex,
    stop: SupportsIndex,
    step: SupportsIndex = 
'''
# for i in range(11):
#     print("Value : ",i)
    
# Nested Loop

# for i in range(11):
#     for j in range(11):
#         print("Value : ",i,j)

# n = 0
# print("While Loop Here ")
# while n<=10:
#     print("Value : ",n)
#     n+=1

status=False

if status:
    print("Status is True")
else:
    print("Status is False")
