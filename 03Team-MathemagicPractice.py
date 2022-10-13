#What is the length of a side of the square?
#The area is:
#Length of Rectangle?
#Width?
#Area of rectangle is:
#Radius of Circle?
#Area is:

'''square1=float(input("What is the length of a side of the square? "))
print(f"The area is: {square1**2}")
rect1=float(input("What is the length of the rectangle?"))
rect2=float(input("What is the width of the rectangle? "))
print(f"The area of the rectangle is {rect1*rect2}")'''

radius=float(input("What is the radius of the circle? "))
print("Please wait, calculating Pi")
import datetime
ms1=datetime.datetime.now().second

#Borrowed code for calculating Pi
pi = 3
iterations=100000000
bottom_number = 2
for i in range(iterations):
   if(i%2==0):
       pi += 4/(bottom_number*(bottom_number+1)*(bottom_number+2))
   else:
       pi -= 4/(bottom_number*(bottom_number+1)*(bottom_number+2))
   bottom_number += 25
#   if(i%100==0):
#       print(str(pi))
#End borrowed code for calculating Pi

ms2=datetime.datetime.now().second
print(f"Calculating Pi took approximately {ms2-ms1} seconds.")
print(f"The area of your circle is approximately {pi*radius**2}.")
print(f"An inaccurate calculation would be {3.14*radius**2}")