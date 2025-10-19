PI=3.14
def calculate_area(shape,*dimensions):
    if shape=="rectangle":
        area=dimensions[0]*dimensions[1]
        return area
    if shape=="circle":
        radius=dimensions[0]
        area=PI*radius*radius
        return area
    return None
def calculate_perimeter(shape,*dimensions):
    if shape=="rectangle":
        perimeter=2*(dimensions[0]*dimensions[1])
        return perimeter
    elif shape=="circle":
        perimeter=2*PI*dimensions[0]
        return perimeter
    return None

    