print("Welcome to the velocity calculator! Please provide the following:\n")
mass = float(input("Mass in Kilograms: "))
gravity = float(input("Gravity in m/s^2, Earth 9.8, Jupiter 24: "))
time = float(input("Time in Seconds: "))
fluid_density = float(input("Density of fluid in kg/m^3, Air 1.3, Water 1000: "))
cross_section = float(input("Cross section area in m^2: "))
drag = float(input("Drag constant, Sphere 0.5, Person feet-first 0.7, Person horizontal 1, Cylinder 1.1: "))

#Calculating 1/2 density * cross section * drag
c = 0.5 * fluid_density * cross_section * drag
print(f"\nThe inner value of C is {c:.3f}")

#Calculating velocity
import math
velocity = (math.sqrt(mass * gravity / c)) * (1 - (math.exp(((-math.sqrt(mass * gravity * c)) / mass) * time)))
print(f"The velocity after {time:.2f} seconds is {velocity:,.3f} m/s^2, or {(velocity * 2.23693629):,.3f} MPH ")