print("Enter a string")
x = input()
x = x.replace(" ","")
y=[i for i in x]
out = {}

for i in y:
    if i in out:
        out[i] = out[i] + 1
    else:
        out[i] = 1



print(out)