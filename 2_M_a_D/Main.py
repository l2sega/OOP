# 2_D_a_M

from Person import* 
from House import*

person1 = Person("John", 23)
person2 = Person("Mike", 34)

house1 = House("1street")

house1.settle_person(person1)
house1.settle_person(person2)

person1.description_of_person() 
person2.description_of_person()

house1.description_of_house()

#house1.evict_person(person1)
#house1.evict_person(person2)

person1.testClassMethod()
person1.testStaticMethod()

Person.testClassMethod()
Person.testStaticMethod()

