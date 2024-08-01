#Input
X1 = float(input("enter x1 coordinates: "))
Y1 = float(input("enter Y1 coordinates: "))
X2 = float(input("enter X2 coordinates: "))
Y2 = float(input("enter Y2 coordinates: "))

Distance = ((X2 - X1)**2 + (Y2 - Y1) **2)**0.5

print("The distance between the two pointes is: ", Distance)
