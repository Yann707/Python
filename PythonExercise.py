#Exercise1
'''print("Hello, Wu Zongyan!")

#Exercise2
#1
name = input("Enter your name here: ")

print(f"Hello, {name}!")

#2

import math

radius = float(input("Enter the radius of the circle: "))

area = math.pi * (radius ** 2)

print(f"The area of the circle is: {area:}")

#3

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

perimeter = (length + width) * 2

area = length * width

print(f"The perimeter of the rectangle is: {perimeter:}")
print(f"The area of the rectangle is: {area:}")

#4

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

sum= num1 + num2 + num3
product = num1 * num2 * num3
average = sum / 3

print(f"Sum: {sum}")
print(f"Product: {product}")
print(f"Average: {average}")

#5

def convert(talents, pounds, lots):
    talent = 20
    pound = 32
    lot = 13.3

    grams = (talents * talent * pound * lot + pounds * pound * lot + lots * lot)

    kilograms = grams // 1000
    grams = grams % 1000

    return kilograms, grams

talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

kilograms, grams = convert(talents, pounds, lots)
print(f"The weight in modern units is: {kilograms:.0f} kilograms and {grams:.2f} grams.")

#6

import random

code1 = [random.randint(0, 9),
         random.randint(0, 9),
         random.randint(0, 9)]
code2 = [random.randint(0, 9),
         random.randint(0, 9),
         random.randint(0, 9)]
code3 = [random.randint(1, 6),
         random.randint(1, 6),
         random.randint(1, 6),
         random.randint(1, 6)]
code4 = [random.randint(1, 6),
         random.randint(1, 6),
         random.randint(1, 6),
         random.randint(1, 6)]
print("3-digit code:", code1)
print("3-digit code:", code2)
print("4-digit code:", code3)
print("4-digit code:", code4)'''

#Exercise2
#1
size = 42
length = float(input("Enter the length of the zander in centimeters: "))

if length >= size:
    print("No problem!")
else:
    centimeters = size - length
    print(f"The zander is {centimeters:.2f} centimeters below the size limit.")
    print("Please release the fish back into the lake.")

#2
cabin_class = input("Enter the cabin class (LUX, A, B, or C): ")

if cabin_class == "LUX":
    print("You have selected a LUX cabin: upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("You have selected a cabin in class A: above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("You have selected a cabin in class B: windowless cabin above the car deck.")
elif cabin_class == "C":
    print("You have selected a cabin in class C: windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")

#3
gender = input("Enter biological gender (male or female): ")

if gender == "female":
   hemoglobin_value=float(input("Enter hemoglobin value(g/l): "))
   min = 117
   max = 155

elif gender == "male":
   hemoglobin_value=float(input("Enter hemoglobin value(g/l): "))
   min = 134
   max = 167

if hemoglobin_value >= min and hemoglobin_value <= max:
    print("Please stay in good health! Your hemoglobin level is normal.")
elif hemoglobin_value > max :
    print("Please pay attention to your health! Your Hemoglobin level is high.")
elif hemoglobin_value < min :
    print ("Please pay attention to your health! Your Hemoglobin level is low.")

#4
year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")






