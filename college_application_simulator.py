subjects = []
grades = []
total_units = []

while sum(total_units) < 20:
    subject = input("Enter your subject: ")
    subjects.append(subject)

    while True:
        grade = int(input("Enter your grade in the subject (0-100): "))
        if 0 <= grade <= 100:
            break
        print("Grade must be between 0 and 100.")

    while True:
        units = int(input("Enter the number of units (3-5): "))
        if units in [3, 4, 5]:
            break
        print("Units must be 3, 4, or 5.")

    if units == 4:
        grade += 20
    elif units == 5:
        grade += 25

    grades.append(grade)
    total_units.append(units)

    print(f"Added subject: {subject} | Adjusted grade: {grade} | Units: {units}")
    print("Current total units:", sum(total_units))
    print()

# calculating average
avg_grades = sum(grades) / len(grades)
print("\nYour average grade is:", round(avg_grades, 2))

Haifa_uni = 85
TLV_uni = 90
Ben_Gurion_uni = 80

if avg_grades >= TLV_uni:
    print("You are accepted to TLV University")
if avg_grades >= Haifa_uni:
    print("You are accepted to Haifa University")
if avg_grades >= Ben_Gurion_uni:
    print("You are accepted to Ben-Gurion University")
if avg_grades < Ben_Gurion_uni:
    print("Sorry, you are not accepted to any university.")
