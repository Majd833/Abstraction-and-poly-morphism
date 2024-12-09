from abc import ABC,abstractmethod
class meth:
    def print(self,x):
        x=print("the value of x is:",x)
    @abstractmethod
    def task(self):
        print("this function is set to private")
class chld(meth):
    def task(self):
        print("We are in the test function")
class_obj=chld()
class_obj.task
class_obj.print(100)