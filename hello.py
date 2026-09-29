
# Student Grade System
# File name: grade_system.py

try:
    # Get the student's mark
    mark = float(input("Enter your mark (0-100): "))

    # Check whether the mark is within the valid range
    if mark < 0 or mark > 100:
        print("Invalid mark! Please enter a mark between 0 and 100.")

    else:
        # Calculate the grade
        if mark >= 90:
            grade = "A"
        elif mark >= 80:
            grade = "B"
        elif mark >= 70:
            grade = "C"
        elif mark >= 60:
            grade = "D"
        else:
            grade = "E"

        # Display the result
        if mark.is_integer():
            mark = int(mark)

        print(f"Mark: {mark} -> Grade: {grade}")

except ValueError:
    print("Invalid input! Please enter a numeric mark.")