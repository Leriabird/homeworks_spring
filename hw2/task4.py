exclass_n = int(input())
temp_inheritance_lst = [input().split() for i in range(exclass_n)]
inheritance_dict = {elt[0]: elt[2:len(elt)] for elt in temp_inheritance_lst}
exceptions_n = int(input())
exception_order_dict = {input(): i for i in range(exceptions_n)}
print(exception_order_dict)

for elt in exception_order_lst:

# 4
# ArithmeticError
# ZeroDivisionError : ArithmeticError
# OSError
# FileNotFoundError : OSError
# 4
# ZeroDivisionError
# OSError
# ArithmeticError
# FileNotFoundError