#####################  decoraters tasks  #####################


# 1) Create a decarator to perform division if it is divided by 0 return cannot perform division

print(" 1) Create a decarator to perform division if it is divided by 0 return cannot perform division ")


def create_dec(f):
    def inner(a, b):
        if b != 0:
            return f(a, b)
        else:
            return "cannot perform division"
    return inner


@create_dec
def divide(a, b):
    return a / b


print(divide(10, 3))
print(divide(10, 5))
print(divide(10, 0))
