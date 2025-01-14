def sum_values(a, *args):
    total = 0 + a
    # print(args)
    # print(type(args))
    # for num in args:
    #     total += num
    return total

print(sum_values(1, 2, 3, "teststring"))  # Output: 6


def print_details(x, **kwargs):
    print('x')
    print(x)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(x="a", name="John", age=30, city="New York")