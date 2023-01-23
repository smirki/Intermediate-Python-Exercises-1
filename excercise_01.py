def get_unique_list(li):
    res = []
    for i in li:
        temp = i
        counter = 0
        for j in li:
            if j == i:
                counter += 1
        for k in res:
                if i == k:
                    counter = 10
        if counter <= 2:
            res.append(temp)
    return res

my_list = [1, 2, 3, 2, 1, 4]
unique_list = get_unique_list(my_list)
print(unique_list)