# 3_Inheritance

from Person import *

class Programmer(Person):
    
    __exp_of_prog = 0
    
    def get_experience_of_programming(self):
        return self.__experience_of_rpogramming
    
    def set_experience_of_programming(self, ex_pr):
        self.__exp_of_prog = ex_pr

    def description_of_person(self):
        super().description_of_person()
        print("I'm programmer and my experiance is ",self.__exp_of_prog, " years")