class MyClass:
    __privatevar=27
    def __privMeth(self):
        print("I am a private function")
    def hello(self):
        print("Private variable is",self.__privatevar)
obj=MyClass()
obj.hello()
obj.__privatevar=10
obj.hello()
obj.__privMeth()