# 4_encapsulation

class Person:
    
    __address = "n/a"
    __name = "n/a"
    __age = 0
     
    def __init__(self, n, a):
        self.__name = n
        self.__age = a
    
    def set_name(self, n):
        self.__name = n
        
    def get_name(self):
        return self.__name
    
    def set_age(self, a):
        self.__age = a
        
    def get_age(self):
        return self.__age
    
    def set_address(self, a):
        self.__address = a
    
    def get_address(self):
        return self.__address

    def description_of_person(self):
        print("---------------------")
        print("| My name is ", self.__name)
        print("| I'm ", self.__age ,"years old.")
        print("| My address is ",self.__address)
        
    def _test_protected_method(self):
        print("I'm protected method")
       
    def __test_private_method(self):
        print("I'm private method")
        
    def test_public_method(self):
        print("I'm public method")
        self.__test_private_method()