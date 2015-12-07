# 4_encapsulation

from Person import*
from Programmer import*
from House import*

person = Person("John", 23)
sub_person = Programmer("Mike", 34)

person._test_protected_method()
person._Person__test_private_method()

sub_person._test_protected_method()
sub_person._Person__test_private_method()

person.test_public_method()



