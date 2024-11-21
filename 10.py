# age = int(input("Enter your age: "))
# if 31 < age < 41:
#     print("You are ok")
#
# years_of_experience = int(input("Enter your years of experience: "))
# if 2 < years_of_experience < 10:
#     print("You have experience")

def check_in_interval(what_to_ask, min_value, max_value):
    current_value = int(input(what_to_ask))
    if min_value < current_value < max_value:
        return True
    return False

# def square(n):
#     print(n*n)

# square(5)
result = check_in_interval("Enter your age: ", 0, 20)
if result:
    print("your name has been entered")
# check_in_interval( "enter years of experience:",2,10)