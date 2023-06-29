#Excercise 21
#how many cans need of wall for paint

import math

def paint_calculation(height,width,cover):
    area=height*width
    no_of_cans=math.ceil(area/cover)
    print(f"You will need {no_of_cans} cans of paints.")


h=int(input("Enter the height of wall in meters:\n"))
w=int(input("Enter the width of wall in meters:\n"))

coverage=7

paint_calculation(width=w,height=h,cover=coverage)