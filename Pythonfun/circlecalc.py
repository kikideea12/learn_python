
x = "Do you want to find the area(1), diameter(2), or circumference(3) of a circle: "
y = "What is the radius of your circle: "

nr = input(x)

if nr == "1" or "2" or "3":
    nr2 = (input(y))

z = pow(float(nr2), 2)

if nr == "1":
    print("The area of your circle is: ")
    print(3.14 * float(z))

if nr == "2":
    print("The diameter of your circle is: ")
    print(float(nr2) * 2)

if nr == "3":
    print("The circumference of your circle is: ")
    print(round((float(nr2) * 2) * 3.14))





