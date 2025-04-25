#Creating a dictionary to store information about students in a class.
students= {
    "Alice": {"grade": 95, "age": 16},
    "Bob": {"grade": 89, "age": 18 }
}
#Adding a new student to the dictionary
students["Ron"] = {"grade": 100, "age": 17}

#Updating the grade of an existing student
students["Bob"]["grade"] = 98

#Removing a student from the dictionary
del students["Bob"]

#Calculating the average grade of all students in the dictionary.
total_grades = sum(student["grade"] for student in students.values())
average_grade = total_grades / len(students)
print(f"Average grade: {average_grade:.2f}")

#Finding the name of the student with the highest grade
def get_grade(item):
    return item[1]["grade"]

top_student = sorted(students.items(), key=get_grade, reverse=True)[0]
print(f"{top_student[0]} has the highest grade of: {top_student[1]['grade']}")

