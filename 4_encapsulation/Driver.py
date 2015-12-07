# 4_encapsulation

from Person import *

class Driver(Person):
        
    __exp_of_dr = 0
    
    def get_experience_of_driving(self):
        return self.__experionce_of_driving
    
    def set_experience_of_driving(self, ex_pr):
        self.__exp_of_dr = ex_pr

    def description_of_person(self):
        super().description_of_person()
        print("I'm driver and my experiance is ",self.__exp_of_dr, " years")