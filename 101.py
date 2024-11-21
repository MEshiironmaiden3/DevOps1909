current_name = input('What is your name?')

my_file = open('names.txt', 'a')
my_file.write(current_name + '\n')
my_file.close()

my_file = open("names.txt", 'r')
for name in my_file.readlines():
    if "n" in name:
      print(f"hello {name.strip()}")
my_file.close()