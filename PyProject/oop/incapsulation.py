class Person:
    def __init__(self, name):
        self.__name = name      # устанавливаем имя just like private modifier
        self.__age = 0          # устанавливаем возраст
 
    def set_age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
       
            print("Недопустимый возраст")
    
    def get_age(self):
    	print(self.__age)

# print(p1.__age) does not work, the program is unable to see .__age outside the class(only if it calls by class method)


		#------------------------------------------------ ANNOTATIONS ------------------------------------------------#


class Sasuke():
    def __init__(self,name, age):
    	self.__name = name
    	self.__age = age

    @property
    def name(self):
    	return self.__name

    @name.setter
    def name(self, name):
    	self.name = __name

ninja = Sasuke("saske", 10)
print(ninja.name)
print(Sasuke.age)    
    	