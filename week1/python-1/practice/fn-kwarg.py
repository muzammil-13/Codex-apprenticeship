# print("Hello World", end="\t")
# print("Next Line Output")

# def fun(a=0, b=3):
#     print(f'{a=} {b=}')

# fun(b=1,a=2)

def kwarg_fun(**_dict):
    print(type(_dict))
    print(_dict.get("passport", "No Specified Key"))

kwarg_fun(name="Arun", age=30, ph=5555)

    