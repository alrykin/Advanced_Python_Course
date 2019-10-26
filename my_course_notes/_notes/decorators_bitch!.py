
# пример простого декоратора
def deco(func):
    def wrap(*args):
        print("start wrapping")
        func(*args)
        print("stop wrapping")
    return wrap

@deco
def some(var):
    print(f"Hello {var}")

some("mama")


# пример  декоратора двойной глубины
def supr_deco(deco_var):
    print(deco_var)
    def deco(func):
        def wrap(*args):
            print("start wrapping")
            func(*args)
            print("stop wrapping")
        return wrap
    return deco

@supr_deco(100)
def some(var):
    print(f"Hello {var}")


some("mama")


# def access_deco(func):
#     def wrap(*args):
#         print("~"*20)
#         print(*args)
#         print("~"*20)
#         func(*args)
#         print("stop wrapping")
#     return wrap
#
# @access_deco
# def some(var):
#     print(f"Hello {var}")
#
# some("mama")
