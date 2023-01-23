add = []

for i in range(5):
    while True:
        print("Enter int #", i+1)
        x = input()
        try:
            if x.isdigit():
                add.append(int(x))
                break
        except:
            pass
        print('\nIncorrect input, try again')

total = 0
for i in add:
    total += i

print("Your sum is ", total)