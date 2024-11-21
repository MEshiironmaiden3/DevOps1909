# before
#my__file = open('input.txt', 'r')
#names = my_file.read().splitlines()
#for name in names:
#    print(name)
#my_file.close()

#import requests
# after
with open("names.txt", "r") as my_file:
    names = my_file.read().splitlines()
    for name in names:
        print(name)

with requests.get("https://digital.isracard.co.il/") as response:
    response.raise_for_status()

