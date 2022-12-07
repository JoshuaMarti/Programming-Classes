def compute_area_rectangle(width, height):
    area = width * height
    return area
def compute_area_square(side):
    area = compute_area_rectangle(side, side)
    return area
def compute_area_circle(radius):
    area = radius * radius * 3.14159
    return area
def compute_area(shape, value, value2 = 1):
    if shape == "circle":
        area = compute_area_circle(value)
    if shape == "square":
        area = compute_area_square(value)
    if shape == "rectangle":
        area = compute_area_rectangle(value, value2)
    return area
shape = ""
while shape != "quit":
    value = 0
    value2 = 0
    shape = ""
    while shape != "circle" and shape != "square" and shape != "rectangle" and shape != "quit":
        shape = input("What shape would you like to calculate the area of? Circle, Square, or Rectangle?\n-->:").lower()
    if shape == "circle":
        value = float(input("Enter the Radius: "))
    elif shape == "square":
        value = float(input("Enter the Side Length: "))
    elif shape == "rectangle":
        value = float(input("Enter the Sirst Side Length: "))
        value2 = float(input("Enter the Second Side Length: "))
    if shape != "quit":
        area = compute_area(shape, value, value2)
        print(f"The area is: {area}")