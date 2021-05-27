try:
    my_dict = dict(i= i*i for i in range(int(input())))
    for x, y in my_dict.items():
        print(x, y)
except:
    raise SyntaxError


