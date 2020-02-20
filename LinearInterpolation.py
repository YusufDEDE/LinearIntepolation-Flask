def start(y0, x, x0, x1, y1):
    try:
        return y0 + (x - x0) * (y1-y0) / (x1-x0)
    except ZeroDivisionError:
        return 'division by zero!!!'    
