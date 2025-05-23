# !/usr/bin/env python3
# Created By: Aaron Rivelino
# Date: May 22, 2025
# The program places the numbers into
# a single variable list and prints them to the console
# It will generate 10 random numbers from 1 to a 100
# Then it will display the highest number generated

import random
import constants


# define the function to find the maximum value in the array
def find_max_value(array):
    # Initizilisate max value to zero
    max_value = 0
    # Loop through each index in the array
    for counter in range(len(array)):
        # If the current value is greater than max_value, then update the max_value
        if array[counter] > max_value:
            max_value = array[counter]

    # After checking all the numbers, return the largest one found
    return max_value


# Define the main function
def main():
    # Create an empty list, to store tha random numbers
    array = []

    # Loop to generate MAX_ARRAY_SIZE number of random integers
    for counter in range(constants.MAX_ARRAY_SIZE):
        # Generate a random number between the minimum num and the max num
        num = random.randint(constants.MIN_NUM, constants.MAX_NUM)

        # Add the generated number to the list
        array.append(num)
        # Display the random number generated
        print(f"The random number generated is: {num}")

    # call the function to find the highest value in the array
    hights_value = find_max_value(array)

    # Display the max value found
    print(f"Max value is {hights_value}")


if __name__ == "__main__":
    main()
