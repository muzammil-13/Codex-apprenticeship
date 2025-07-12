# print("Hello World", end="\t")
# print("Next Line Output")

# def fun(a=0, b=3):
#     print(f'{a=} {b=}')

# fun(b=1,a=2)

# def kwarg_fun(**_dict):
#     print(type(_dict))
#     print(_dict.get("passport", "No Specified Key"))

# kwarg_fun(name="Arun", age=30, ph=5555)

def demo_args_kwargs(*args, **kwargs):
    print("Positional arguments (*args):")
    for i, arg in enumerate(args):
        print(f"  args[{i}] = {arg}")
    
    print("\nKeyword arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"  {key} = {value}")

    # Example: sum all numeric args and kwargs
    total = sum(arg for arg in args if isinstance(arg, (int, float)))
    total += sum(value for value in kwargs.values() if isinstance(value, (int, float)))
    print(f"\nSum of all numeric values: {total}")

# Example usage:
demo_args_kwargs(1, 2, "hello", 4.5, name="Arun", age=30, ph=5555, city="Delhi")