# 3_Inheritance

from Person import*

class House:
    def __init__(self, a):
        self.__address = a
        
    __address = "n/a"
    __list_of_residents = ["n/a"]
    
    def set_address(self, a):
        self.__address = a
        
    def get_address(self):
        return self.__address
    
    def settle_person(self, person):
            if isinstance(person,Person):
                self.__list_of_residents.append(person)
                person.set_address(self.__address)
            else:
                print("settle_person's argument is't Person")

    def evict_person(self, person):
        self.__list_of_residents.remove(person)
        person.set_address("n/a")
        
        if len(self.__list_of_residents) == 0:
            self.__list_of_residents= ["n/a"]
    
    def description_of_house(self):
        print("--------------------")
        print("# Address of this house is ", self.__address)
        print("# In the house live:")
        
        for p in self.__list_of_residents:
            if isinstance(p,Person):
                print("# -",p.get_name())