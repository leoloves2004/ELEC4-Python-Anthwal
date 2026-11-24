# Name: Leomhel P. Anthwal
# Section: IV-BSIT-C
# Activity: P2 - Custom Module
# Date: 2026-11-17
# Reference: Developed with ChatGPT assistance; review and explain before submitting.

"""Reusable calculations for nonempty collections of valid student grades."""


def calculate_average(grades):
    if not grades:
        raise ValueError("At least one grade is required.")
    return sum(grades) / len(grades)


def determine_status(grades):
    return "PASS" if calculate_average(grades) >= 75 else "FAIL"


def get_highest(grades):
    if not grades:
        raise ValueError("At least one grade is required.")
    return max(grades)


def get_lowest(grades):
    if not grades:
        raise ValueError("At least one grade is required.")
    return min(grades)
