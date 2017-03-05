## Question from last week I could not fully  explain

### Rigo: Why does False == 0 evaluate as true? They are different data types? What are you cazy python?
### Python: No, that is a genius design choice by me. The reason True and False are equal
### to 1 and 0 respectively is because bool type is implemented as a subclass of int type.


x = True
### Using Method Resolution Order built in method(new to python 3)
### we can get a list of types the class is derived from

mro_of_x = type(x).mro()

print("Here are the classes that a Bool Type is derived from:{}".format(mro_of_x))

### HERE IS A GETTO EXAMPLE OF THIS
class nepsInt(object):
    def __init__(self):
        self.zero = 0
        self.one = 1
        self.two = 2
        self.three = 3
        self.four = 4

class nepsBool(nepsInt):
    def __init__(self):
        super(nepsBool, self).__init__()
        self.FALSE = self.zero
        self.TRUE = self.one



customInt = nepsInt()
customBool = nepsBool()

if customInt.zero == customBool.FALSE:
    print("YES ITS TRUE")

#######################################

# This means that because a bool is an int, it can also index, like 0 and 1
mylist = ["apple","pie"]
print(mylist[False])
print(mylist[True])

## From stackoverflow by Olivier Verdier
## Boolean values behave like the values 0 and 1, respectively, in almost all contexts,
## the exception being that when converted to a string, the strings "False" or "True" are returned, respectively


### FROM PYTHON DOCS:
#the following values are considered false:
#None
#False
#zero of any numeric type, for example, 0, 0.0, 0j.
#any empty sequence, for example, '', (), [].
#any empty mapping, for example, {}.
#instances of user-defined classes, if the class defines a __bool__() or __len__() method,
# when that method returns the integer zero or bool value False. [1]

#All other values are considered true — so objects of many types are always true.

def checkTruthy(v):
    if v:
        print("{} evaluates as True".format(v))
    else:
        print("{} evaluates to False".format(v))



### Lets make some custom classes to see how __bool__ works... we will come back more indepth to see how
### are made in a week or two
class alwaysFalseClass(object):
    def __init__(self,name):
        self.attr = name
    def __bool__(self):
        return False
    def __str__(self):
        return str(self.attr)

class alwaysTrueClass(object):
    def __init__(self,name):
        self.attr = name
    def __bool__(self):
        return True
    def __str__(self):
        return str(self.attr)

class customCheckLengthClass(object):
    def __init__(self,name):
        self.attr = name
    def __bool__(self):
        if len(self.attr) > 0:
            return True
        else:
            return False

    def __str__(self):
        return str(self.attr)

classInstance = alwaysFalseClass("Rigo")
classInstance2 = alwaysTrueClass("Lily")
classInstance3 = customCheckLengthClass("Amo")
classInstance4 = customCheckLengthClass("")

checkTruthy(classInstance)
checkTruthy(classInstance2)
checkTruthy(classInstance3)
checkTruthy(classInstance4)









