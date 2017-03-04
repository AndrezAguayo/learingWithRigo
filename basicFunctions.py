## how to make a funciton in pyton

# first write def key word to "define" a function
# then type the name of the function, can not start with numbers no spaces and what not
# then use () - more on this next
# then to finish intlizing the function end with a :

def spacer(n=""):
    print("\n___________{}_____________\n".format(n))

def myfirstFunction():
    print("this is my first funcition")

spacer("Testing my First Function")
myfirstFunction()

def takeInArguments(a,b,c):
    print(a)
    print(b)
    print(c)

spacer("Testing takeInArguments")
takeInArguments("HelloFirst","HelloSecond","HelloThird")

spacer("Testing takeInArguments rearanged arguments")
takeInArguments(c="HelloFirst",b="HelloSecond",a="HelloThird")




def namedArguments(a="a",b="b",c="c"):
    print(a)
    print(b)
    print(c)


spacer("Testing namedArguments with no arguments")
namedArguments()
spacer("Testing namedArguments with overridden argument")
namedArguments(a="Raspberry")
spacer("Testing namedArguments with overridden arguments")
namedArguments(a="Raspberry",b="Raspberry",c="Raspberry")





def variableLengthArgument(*args):
    for arg in args:
        print("Argument: {0}".format(arg))

def variableLengthKeywordArgument(**kwargs):
    for key in kwargs:
        print("Key word: {0}, Argument: {1}".format(key, kwargs[key]))

def variableLengtBothTypeArgument(*args, **kwargs):
    for arg in args:
        print("Argument: {0}".format(arg))
    for key in kwargs:
        print("Key word: {0}, Argument: {1}".format(key, kwargs[key]))


spacer("Testing variableLengthArgument with random arguments")
variableLengthArgument("dog",1,2323, True, 43.44, 99,False, "A lot of words")


spacer("Testing variableLengthKeywordArgument with random named arguments")
variableLengthKeywordArgument(rigo="nfdafj", sisMich="FDFD", lily="happy", amo="Fadf")


spacer("Testing variableLengthKeywordArgument with named and not named")
variableLengtBothTypeArgument("dog",1,2323, True,rigo="nfdafj", sisMich="FDFD", lily="happy", amo="Fadf")

### must be non named first then keyword args
#Uncomment below to see Error witll not evaluate
#variableLengtBothTypeArgument(rigo="nfdafj", sisMich="FDFD", lily="happy", amo="Fadf","dog",1,2323, True,)
