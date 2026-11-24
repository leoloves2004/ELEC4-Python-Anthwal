# Name: Leomhel P. Anthwal
# Section: IV-BSIT-C
# Activity: P1 - Student Grade Calculator
# Date: 2026-11-17
# Reference: Developed with ChatGPT assistance; review and explain before submitting.

"""Calculate a student's grade report using user-defined functions."""

from math import isfinite

PASSING_AVERAGE = 75


def accept_grades():
    """Read one or more grades, retrying invalid entries."""
    while True:
        try:
            count = int(input("How many grades? "))
            if count < 1:
                raise ValueError
            break
        except ValueError:
            print("Enter a positive whole number.")

    grades = []
    while len(grades) < count:
        try:
            grade = float(input(f"Grade {len(grades) + 1}: "))
            if not isfinite(grade) or not 0 <= grade <= 100:
                raise ValueError
        except ValueError:
            print("Enter a number from 0 to 100.")
        else:
            grades.append(grade)
    return grades


def compute_average(grades):
    return sum(grades) / len(grades)


def get_highest(grades):
    return max(grades)


def get_lowest(grades):
    return min(grades)


def determine_status(grades):
    return "PASS" if compute_average(grades) >= PASSING_AVERAGE else "FAIL"


def display_results(grades):
    if not grades:
        print("Enter grades first.")
        return
    print(f"Average: {compute_average(grades):.2f}")
    print(f"Highest: {get_highest(grades):.2f}")
    print(f"Lowest: {get_lowest(grades):.2f}")
    print(f"Status: {determine_status(grades)}")


def main():
    print("Leomhel P. Anthwal | IV-BSIT-C | P1 Grade Calculator")
    grades = []
    while True:
        print("\n1. Enter grades\n2. View results\n3. Exit")
        choice = input("Choice: ").strip()
        if choice == "1":
            grades = accept_grades()
        elif choice == "2":
            display_results(grades)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Select 1, 2, or 3.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nProgram closed.")

# A local variable exists inside the function where it is created.
# For example, grades in accept_grades() holds the input for that function.
# PASSING_AVERAGE is a global constant defined outside all functions.
# determine_status() reads that constant, while each function's parameters are local.
