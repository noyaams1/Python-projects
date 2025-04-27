
def rectangle_area(length,width):
    if length < 0 or width < 0:
        return None
    else:
        area = length * width
        return area

print(rectangle_area(2,4))
print(rectangle_area(0,4))
print(rectangle_area(111,4))
print(rectangle_area(1.5,0.5))
print(rectangle_area(-2,-1))
