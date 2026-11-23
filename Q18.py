# Q18. Calculate the volume of a cube and a cuboid
side = float(input("Enter side of cube: "))
cube_volume = side ** 3

length = float(input("Enter cuboid length: "))
breadth = float(input("Enter cuboid breadth: "))
height = float(input("Enter cuboid height: "))
cuboid_volume = length * breadth * height

print("Volume of cube =", cube_volume)
print("Volume of cuboid =", cuboid_volume)
