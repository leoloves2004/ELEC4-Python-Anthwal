# Name: Leomhel P. Anthwal
# Section: IV-BSIT-C
# Activity: P3 - Student Record Manager
# Date: 2026-11-17
# Reference: Developed with ChatGPT assistance; review and explain before submitting.


def clean_name(name):
    return " ".join(name.split())


def add_student(students, name_keys, name):
    name = clean_name(name)
    if not name:
        return "Name cannot be blank."
    if name.casefold() in name_keys:
        return "Student already exists."
    students.append(name)
    name_keys.add(name.casefold())
    return f"Added: {name}"


def remove_student(students, name_keys, name):
    key = clean_name(name).casefold()
    for student in students:
        if student.casefold() == key:
            students.remove(student)
            name_keys.remove(key)
            return f"Removed: {student}"
    return "Student not found."


def search_students(students, query):
    query = clean_name(query).casefold()
    if not query:
        return []
    return sorted((s for s in students if query in s.casefold()), key=str.casefold)


def display_students(students):
    for number, student in enumerate(sorted(students, key=str.casefold), start=1):
        print(f"{number}. {student}")
    print(f"Total students: {len(students)}")


def main():
    print("Leomhel P. Anthwal | IV-BSIT-C | P3 Record Manager")
    students = []
    name_keys = set()
    while True:
        print("\n1. Add\n2. Remove\n3. Search\n4. Display all\n5. Exit")
        choice = input("Choice: ").strip()
        if choice == "1":
            print(add_student(students, name_keys, input("Full name: ")))
        elif choice == "2":
            print(remove_student(students, name_keys, input("Full name to remove: ")))
        elif choice == "3":
            matches = search_students(students, input("Partial name: "))
            if matches:
                display_students(matches)
            else:
                print("No matching students.")
        elif choice == "4":
            display_students(students)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Select 1 to 5.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nProgram closed.")

# A list preserves order and can contain duplicate values.
# A set contains unique values and does not provide a display order.
# students is a list that preserves each student's original capitalization.
# name_keys is a set of normalized names that prevents case-insensitive duplicates.
