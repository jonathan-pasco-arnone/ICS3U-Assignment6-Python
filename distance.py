#!/usr/bin/env python3

# Created by: Jonathan Pasco-Arnone
# Created on: January 2021
# This program calculates the distance of 2 points on a plane

import math


def calculator(x1, y1, x2, y2):
    # This function calculates the distance of 2 points on a plane

    distance = math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))

    return distance


def main():
    # This function gathers inputs and places them into the
    # designated functions

    print("The formula for distance is d=√((x_2-x_1)²+(y_2-y_1)²)."
          " With the x_1 and y_1 being coordinate 1. And the x_2 and y_2"
          " being coordinate 2. Please enter the coordinates in cm.")
    print("")

    while(1):
        try:
            x_1 = int(input("x_1: "))
            y_1 = int(input("y_1: "))
            x_2 = int(input("x_2: "))
            y_2 = int(input("y_1: "))
        except Exception:
            print("")
            print("Please enter valid integers")
            print("")
        else:
            break
    final_distance = calculator(x_1, y_1, x_2, y_2)
    print("")
    print("The distance between ({0},{1}) and ({2},{3}) is"
          " {4}cm.".format(x_1, y_1, x_2, y_2, final_distance))


if __name__ == "__main__":
    main()
