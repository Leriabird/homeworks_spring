lst = [cls.__name__ for cls in [A, B, C] if issubclass(D, cls)]
print(' '.join(lst))