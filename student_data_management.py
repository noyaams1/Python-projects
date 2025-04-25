students= {
    "Alice": {"age": 16, "subjects": ["Math","Geography","History"],"grades": {75,80,95}},
    "Bob":  {"age": 18, "subjects": ["Math","Chemistry","Physics"], "grades": {100,60,85}}
}
#Adding a new student to the dictionary
students["Diana"] = {"age": 17, "subjects": ["Math", "English", "literature"], "grades": {55,90,95}}
print(students)
#Updating the grades of an existing student by adding new grades to their set of grades
students["Alice"]["grades"].update([60, 100])
print(students["Alice"]["grades"])
#Removing a subject from a student's list of subjects.
students["Bob"]["subjects"].remove("Math")
print(students["Bob"]["subjects"])
#Finding the average grade of a specific student by converting their grades set to a list
Diana_grades= list(students["Diana"]["grades"])
Diana_avg= sum(Diana_grades)//len(Diana_grades)
print(Diana_avg)
#Finding the student with the highest average grade and printing their name, age, and subjects
def get_avg(student):
    return sum(student[1]["grades"]) / len(student[1]["grades"])
top_student = max(students.items(), key=get_avg)
name = top_student[0]
info = top_student[1]
average = sum(info["grades"]) / len(info["grades"])
print(f"Average grade: {average:.2f}")
print(f"Top student: {name}")
print(f"Age: {info['age']}")
print(f"Subjects: {', '.join(info['subjects'])}")
#Creating a tuple for each student (name, age, number of subjects)
def get_num_subjects(student_tuple):
    return student_tuple[2]
student_tuples = [
    (name, info["age"], len(info["subjects"]))
    for name, info in students.items()
]
sorted_students = sorted(student_tuples, key=get_num_subjects)
for student in sorted_students:
    print(student)
