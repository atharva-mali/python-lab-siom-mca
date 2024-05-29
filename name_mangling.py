# Name Mangling

class Foo:
    def __init__(self):
        self.__helper()
    def __helper(self):
        print("sneaky")

x=Foo()
x.__Foo__helper()
x.__helper()

