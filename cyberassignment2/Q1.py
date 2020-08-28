radius = int(input("Enter the radius of sphere:"))
pi = 3.14


def volume_calculator(radius):
    vol_of_sphere = (4*pi*(radius**3))/3
    return vol_of_sphere

print(f"The volume of the sphere of radius {radius} is {volume_calculator(radius):.4} cubic units.")