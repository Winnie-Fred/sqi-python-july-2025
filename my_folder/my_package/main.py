# from module1 import module_1_func as module_one_func
# from module2 import module_2_func as module_two_func


from my_package import module_1_func1

print(module_1_func1())

# print(__name__)


import sys
for p in sys.path:
    print(p)

# pypi

# monty hall python