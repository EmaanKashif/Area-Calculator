def calculate_area():
    while True:
        shape = input("Enter the shape(rectangle,circle,triangle,square): ").strip().lower()
         
        if shape == "exit":
         print("Exiting the program")
         break

        if shape == "rectangle":
           width = float(input("Enter the width: "))
           height = float(input("Enter the height: "))
           print(f"The area of the rectangle is {width*height:.2f}")

        elif shape == "circle":
            radius = float(input("Enter the radius: "))
            print(f"The area of the circle is {3.14*radius**2:.2f}")

        elif shape == "triangle":
            base = float(input("Enter the base: "))
            height = float(input("Enter the height: "))
            print(f"The area of the triangle is {1/2*base*height:.2f}")
        
        elif shape == "square":
            side = float(input("Enter the side lenght: "))
            print(f"The area of the square is {side **2:.2f}")

        else:
           print("Enter a valid shape")
calculate_area()
