# Name: Leomhel P. Anthwal
# Section: IV-BSIT-C
# Activity: P2 - Custom Module Main Program
# Date: 2026-11-17
# Reference: Developed with ChatGPT assistance; review and explain before submitting.

import student_utils  # Import the module and access functions through its name.
from student_utils import determine_status  # Import one function directly.
from datetime import datetime
from math import isfinite


def read_grades():
    while True:
        raw = input("Enter grades separated by spaces: ")
        try:
            grades = [float(value) for value in raw.split()]
            if not grades or any(not isfinite(g) or not 0 <= g <= 100 for g in grades):
                raise ValueError
            return grades
        except ValueError:
            print("Enter at least one numeric grade; each must be from 0 to 100.")


def main():
    print("Leomhel P. Anthwal | IV-BSIT-C | P2 Student Report")
    grades = read_grades()
    print(f"Report generated: {datetime.now():%Y-%m-%d %H:%M:%S}")
    print(f"Average: {student_utils.calculate_average(grades):.2f}")
    print(f"Highest: {student_utils.get_highest(grades):.2f}")
    print(f"Lowest: {student_utils.get_lowest(grades):.2f}")
    print(f"Status: {determine_status(grades)}")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nProgram closed.")



#  C:\Anthwal ELEC4-Python\set2\p5\students.txt