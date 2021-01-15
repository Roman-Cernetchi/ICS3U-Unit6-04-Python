#!/usr/bin/env python3

# Created by: Roman Cernetchi
# Created on: January 2021
# This program prints a 2D array and finds the average of all the numbers

import random


def average_2D(list_2D):
    # This function finds the average

    total = 0
    rows = len(list_2D)
    columns = len(list_2D[0])

    for row_value in list_2D:
        for value in row_value:
            total += value

    average = total / (rows*columns)

    return average


def main():
    # This function handles input and prints a 2D array

    list_2D = []

    # input
    while True:
        try:
            rows_input = input("Enter the number of rows you want: ")
            rows = int(rows_input)
            columns_input = input("Enter the number of columns you want: ")
            columns = int(columns_input)
            print("")

            # check for negative numbers
            if rows > 0 and columns > 0:

                for loop_counter_rows in range(0, rows):
                    temp_column = []
                    for loop_counter_columns in range(0, columns):
                        random_num = random.randint(0, 50)
                        temp_column.append(random_num)
                        print("{0} ".format(random_num), end="")
                    list_2D.append(temp_column)
                    print("")

            average_of_array = average_2D(list_2D)
            average_rounded = '{0:.5g}'.format(average_of_array)

            print("")
            print("The average of all the numbers is: {0}"
                  .format(average_rounded))
            break

        except Exception:
            # output
            print("Invalid input, try again.")


if __name__ == "__main__":
    main()
