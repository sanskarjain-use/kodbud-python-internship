"""Task 5: Password Strength Checker (uses re)"""
import re

MIN_LENGTH = 8


def check_password(pw):
    problems = []
    if len(pw) < MIN_LENGTH:
        problems.append(f"at least {MIN_LENGTH} characters")
    if not re.search(r"\d", pw):
        problems.append("a number")
    if not re.search(r"[A-Z]", pw):
        problems.append("an uppercase letter")
    if not re.search(r"[^A-Za-z0-9]", pw):
        problems.append("a special character")
    return problems


def main():
    pw = input("Enter a password to check: ")
    problems = check_password(pw)
    if problems:
        print("Weak. Missing: " + ", ".join(problems))
    else:
        print("Strong")


if __name__ == "__main__":
    main()
