
students = [
    {"name": "Alice", "grades": [80, 90, 85]},
    {"name": "Bob", "grades": [33, 40, 50]},
    {"name": "Charlie", "grades": [95, 100, 97]}
]

# Handling potential errors.
for student in students:
    if student["grades"] == []:
        print(f"The student {student["name"]} doesnt have any grades available")
        exit()
def calculate_average(grades):
    return sum(grades) / len(grades)
average_grades = list(map(lambda student: (student["name"], calculate_average(student["grades"])), students))
print("\nAverage grades for each student:")
for name, avg_grade in average_grades:
    print(f"Average grade of {name}: {avg_grade:.2f}")

print("\nStudents who passed:")
average_grade=50
passing_students= list(filter(lambda students: calculate_average(students["grades"]) >= 50, students))
for student in passing_students:
    average_grade= calculate_average(student["grades"])
    print(f"{student['name']}: {average_grade:.2f}")

print("\nStudents sorted by average grade (descending):")
sorted_students = sorted(students, key=lambda student: calculate_average(student["grades"]), reverse=True)
for student in sorted_students:
    average_grade = calculate_average(student["grades"])
    print(f"{student['name']}: {average_grade:.2f}")

updated_students_grades = []
print("\nIncreasing each student's grade by 5 points: ")
for student in students:
    updated_grades = list(map(lambda grade: min(grade + 5, 100), student["grades"]))
    updated_students_grades.append({"name": student["name"], "grades": updated_grades})
for student in updated_students_grades:
    print(f"{student['name']} updated grades: {student['grades']}")

print("\n~~~~~~ Summary Report ~~~~~~")
highest_grade = max(average_grades, key=lambda x: x[1])[1]
top_student = list(filter(lambda x: x[1] == highest_grade, average_grades))
print(f"Highest average grade in the class: {highest_grade:.2f}")
print("Student(s) with the highest grade:")
for name, avg in top_student:
    print(f"{name}: {avg:.2f}")

