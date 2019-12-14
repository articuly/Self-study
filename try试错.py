try:
    print(10 / 5)
    print(10 + "O")
except ArithmeticError as e:
    print(e)
except TypeError as e:
    print(e)
# except:
#     print("you can not do it")
