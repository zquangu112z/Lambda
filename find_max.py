arr = [0, 1, 2, 13, 44, 25, 6, 7, 3, 9]
print("Max = %d" % reduce(lambda x, y: x if x > y else y, arr))
