# Write code below 💖
  
# This is the title 
print("==================")
print("📐 Area Calculator 📐")
print("==================")

# This is the menu for shape
print("1. Square")
print("2. Rectangle")
print("3. Triangle")
print("4. Circle")
print("5. Quit")

import math

shape = 0

while shape != 5:
 shape = int(input("Wich shape : "))
 if shape == 1:
    side = int(input("Side : "))
    area = side * side
    print(f"The area is {area}")
 elif shape == 2:
    length = int(input("Length : "))
    width = int(input("Width : "))
    area = length * width
    print(f"The area is {area}")
 elif shape == 3:
    height = int(input("Height : "))
    base = int(input("Base : "))
    area = height * base / 2
    print(f"The area is {area}")
 elif shape == 4:
   radius = int(input("Radius : "))
   area = math.pi * radius * radius
   print(f"The area is {area}") 
 elif shape > 5:
  print("Error")
else:
  print("Quit")

