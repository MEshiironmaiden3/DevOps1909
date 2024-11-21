import datetime
from mydep import test as mydep_test
from my_other_dep import test as my_other_dep
mydep_test()
my_other_dep

def wait_for_print():
    from time import sleep
    sleep(3)
    print("Hello World")


print(datetime.datetime.now())



