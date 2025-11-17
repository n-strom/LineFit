def linear (m, x, b):
    return m * x + b

def slope_units (x_units, y_units):
    x_units = x_units.rstrip("s")
    y_units = y_units.rstrip("s")
    return y_units + "/" + x_units

def print_equation (m, b, y_units, x_units):
    return print("The equation of the line is: y = ", str(m), slope_units(x_units, y_units),"x + ", str(b), x_units)
