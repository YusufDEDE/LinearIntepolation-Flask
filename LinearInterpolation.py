def start(y0, x, x0, x1, y1):
    print("y0", y0,"x", x, "x0", x0, "x1", x1, "y1",y1)
    y = (x - x0) * (y1-y0) / (x1-x0)
    return y0 + y


print(start(1355, 6, 4, 7, 1680))