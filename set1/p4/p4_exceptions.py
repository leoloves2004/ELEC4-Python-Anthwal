# Name: Leomhel P. Anthwal
# Section: IV-BSIT-C
# Activity: P4 - Safe Menu Program
# Date: 2026-11-17
# Reference: Developed with ChatGPT assistance; review and explain before submitting.

from math import isfinite


def divide_numbers():
    try:
        numerator = float(input("Numerator: "))
        denominator = float(input("Denominator: "))
        if not isfinite(numerator) or not isfinite(denominator):
            raise ValueError("Numbers must be finite.")
        result = numerator / denominator
        if not isfinite(result):
            raise OverflowError("The result is too large.")
    except ValueError:
        print("Invalid number. Enter finite numeric values.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except OverflowError:
        print("The result is too large to represent.")
    else:
        print(f"Result: {result:g}")
    finally:
        print("Division attempt finished.")


def display_file():
    try:
        filename = input("File name or path: ").strip()
        with open(filename, "r", encoding="utf-8") as file:
            contents = file.read()
    except FileNotFoundError:
        print("File not found. Check the file name or path.")
    except PermissionError:
        print("You do not have permission to read that file.")
    except UnicodeError:
        print("The file is not readable UTF-8 text.")
    except (OSError, ValueError):
        print("Cannot open that path as a text file.")
    else:
        print(contents if contents else "The file is empty.")
    finally:
        print("File operation finished.")


def main():
    print("Leomhel P. Anthwal | IV-BSIT-C | P4 Safe Menu")
    while True:
        print("\n1. Divide\n2. Open file\n3. Exit")
        choice = input("Choice: ").strip()
        if choice == "1":
            divide_numbers()
        elif choice == "2":
            display_file()
        elif choice == "3":
            break
        else:
            print("Invalid menu selection. Select 1, 2, or 3.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nProgram closed.")
