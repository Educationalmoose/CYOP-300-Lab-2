"""
Name: Mason Conaway
Class: CYOP 300
Date: 3/10/2026
"""

import random
from datetime import date
import math

def menu():
    """shows a menu to the user with options for which program to run"""
    while True:
        print("******************************************")
        item = input("Please choose an item from the menu below: "
                     "\n\ta.   Generate Secure Password"
                     "\n\tb.   Calculate and Format a Percentage"
                     "\n\tc.   How many days from today until July 4, 2025"
                     "\n\td.   Use the Law of Cosines to calculate the leg of a right triangle"
                     "\n\te.   Calculate the volume of a Right Circular Cylinder"
                     "\n\tf.   Exit Program\n").lower()
        print("******************************************")
        match item:
            case 'a':
                generate_secure_password()
                thank_user()
                return
            case 'b':
                calculate_and_format_percentage()
                thank_user()
                return
            case 'c':
                days_until_july_4_2026()
                thank_user()
                return
            case 'd':
                calculate_leg_of_triangle()
                thank_user()
                return
            case 'e':
                calculate_volume_of_right_circular_cylinder()
                thank_user()
                return
            case 'f':
                thank_user()
                break
            case _:
                print("Invalid item selected.")
                return

def generate_secure_password():
    """generates a secure password for user based on specified criteria"""
    while True: # continuously loops until valid input is detected
        length = input("Please choose a length for the password: ")
        if is_integer(length) and int(length) > 0:
            length = int(length)
            break
        print("ERROR: Please enter a positive integer for the length of the password")

    while True: # continuously loops until valid input is detected
        allow_upper_case = input("Do you want to allow for uppercase letters? (y/n) ")
        if allow_upper_case.lower() == "y":
            allow_upper_case = True
            break
        if allow_upper_case.lower() == "n":
            allow_upper_case = False
            break
        print("ERROR: Please enter either 'y' or 'n' ")

    while True: # continuously loops until valid input is detected
        allow_lower_case = input("Do you want to allow for lowercase letters? (y/n) ")
        if allow_lower_case.lower() == "y":
            allow_lower_case = True
            break
        if allow_lower_case.lower() == "n":
            allow_lower_case = False
            break
        print("ERROR: Please enter either 'y' or 'n'")

    while True: # continuously loops until valid input is detected
        allow_numbers = input("Do you want to allow for numbers? (y/n) ")
        if allow_numbers.lower() == "y":
            allow_numbers = True
            break
        if allow_numbers.lower() == "n":
            allow_numbers = False
            break
        print("ERROR: Please enter either 'y' or 'n'")

    while True: # continuously loops until valid input is detected
        allow_special_characters = input("Do you want to allow for special characters? (y/n) ")
        if allow_special_characters.lower() == "y":
            allow_special_characters = True
            break
        if allow_special_characters.lower() == "n":
            allow_special_characters = False
            break
        print("ERROR: Please enter either 'y' or 'n'")
    possible_characters = []

    if allow_upper_case: # adds all uppercase letters to the pool of chars
        for j in range(65,91):
            # ascii for uppercase letters
            possible_characters.append(chr(j))
    if allow_lower_case: # adds all lowercase letters to the pool of chars
        for j in range(97,122):
            # ascii for lowercase letters
            possible_characters.append(chr(j))
    if allow_numbers: # adds all numbers to the pool of chars
        for j in range(0,10):
            # numbers 0-9
            possible_characters.append(random.randint(0,9))
    if allow_special_characters: # adds all special characters to the pool of chars
        #random character from list
        special_char_list = ['!','?','.','<','>','@','#','$','%','^','&','*','{','}','(',')']
        possible_characters.extend(special_char_list)

    while True:
        # new empty list to contain the password
        password = []

        for _ in range(length): # generates a password with the desired length
            # pull a random character from the set of possible characters
            random_num = random.randint(0,len(possible_characters)-1)
            password.append(str(possible_characters[random_num]))

        print("PASSWORD: " + "".join(password))
        go_again = input("\nWould you like to generate a new password? (y/n) ")
        if go_again.lower() == 'n':
            break
        if go_again.lower() != "y":
            print("ERROR: Please enter either 'y' or 'n'")

def calculate_and_format_percentage():
    """calculates and formats a percentage of desired length to user"""
    while True:
        whole = input("Please choose a number that represents the whole portion: ")
        if is_number(whole):
            whole = float(whole)
            break
        print("ERROR: Please enter a number for the whole portion")

    while True:
        part = input("Please choose a number that represents the part of the whole portion: ")
        if is_number(part):
            part = float(part)
            break
        print("ERROR: Please enter a number for the part of the whole portion")

    while True:
        decimal_places = input("Please enter the number of decimal places: ")
        if is_number(decimal_places):
            decimal_places = int(decimal_places)
            break
        print("ERROR: Please enter an integer for the number of decimal places")
    percentage = part/whole * 100
    print(f"PERCENTAGE: {percentage:.{decimal_places}f}%")

def days_until_july_4_2026():
    """calculates and formats a number of days until July 4, 2026"""
    today = date.today() # gets today's date
    july_4_2025 = date(2026, 7, 4) # sets the date

    print("Days until July 4, 2025: " + str((july_4_2025 - today).days))

def calculate_leg_of_triangle():
    """calculates and formats the length of the leg of a triangle"""
    print("To calculate the length of the leg of any triangle")
    print("we will need two side lengths, and the angle opposite of the")
    print("missing side length.")
    while True: # continuously loops until valid input is detected
        a = input("Leg A: ")
        if is_number(a) and float(a) > 0:
            a = float(a)
            break
        print("ERROR: Please enter a positive number for the leg A")

    while True: # continuously loops until valid input is detected
        b = input("Leg B: ")
        if is_number(b) and float(b) > 0:
            b = float(b)
            break
        print("ERROR: Please enter a positive number for the leg B")

    while True: # continuously loops until valid input is detected
        c_angle = input("Angle opposite of leg C: ")
        if is_number(c_angle):
            if 0 < float(c_angle) < 180:
                c_angle = float(c_angle)
                break
            print("ERROR: Angle must be between 0 and 180 degrees (exclusive)")
        else:
            print("ERROR: Please enter a number for the angle opposite of leg C")

    c_angle_radians = math.radians(c_angle) # converts angle to radians
    c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(c_angle_radians)) # calculates leg c
    print(f"The length of leg C is: {c:.3f}")

def calculate_volume_of_right_circular_cylinder():
    """calculates and formats the volume of a right circular cylinder"""
    while True: # continuously loops until valid input is detected
        radius = input("Please enter the radius: ")
        if is_number(radius) and float(radius) > 0:
            radius = float(radius)
            break
        print("ERROR: Please enter a valid number for the radius of the right circular cylinder")

    while True: # continuously loops until valid input is detected
        height = input("Please enter the height: ")
        if is_number(height) and float(height) > 0:
            height = float(height)
            break
        print("ERROR: Please enter a positive number for the height of the right circular cylinder")

    volume = math.pi * (radius * radius) * height # calculates the volume
    print(f"VOLUME: {volume:.3f}")
def thank_user():
    """thanks the user for participating"""
    print("\n******************************************")
    print("   Thank you for using the application!")
    print("******************************************\n")
    input()

def is_number(s):
    """checks if a string is a number by attempting to convert it to a float"""
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_integer(s):
    """checks if a string is a number by attempting to convert it to an integer"""
    try:
        int(s)
        return True
    except ValueError:
        return False

menu()
