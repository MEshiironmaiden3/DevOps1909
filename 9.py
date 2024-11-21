

for i in range(1,101):
    if i % 7 == 0 and "7" not in str(i):
        print(i)

names = ["natan", "shay", "ronen", "aaron"]
result = [name.upper() for name in names if "n" in name]
result = [f"hellon: {name}" for name in names if "n" in name]
print(result)
