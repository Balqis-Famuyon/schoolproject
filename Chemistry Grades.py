import csv
fields = ['Student Name', 'Age', 'Sex', 'First C.A', 'Lab test', 'Exam', 'Term score', 'Grade']
Number_of_students = int(input('Number of students:'))
i = 0
students = []
while i < Number_of_students:
    Name = input('Name of student: ')
    Age = int(input('Age: '))
    Sex = input('Sex: ')
    while Sex.upper() != 'M' and Sex.upper() != 'F':
        print('Input "M" for Male and "F" for Female')
        Sex = input('Sex: ')
    First_C_A = int(input('First C A: '))
    Lab_Test = int(input('Lab test: '))
    Exam = int(input('Exam: '))
    term_score = (First_C_A + Lab_Test + Exam) / 3
    Grade = 'F'
    if term_score >= 70:
        Grade = 'A'
    elif term_score >= 60:
        Grade = 'B'
    elif term_score >= 50:
        Grade = 'C'
    elif term_score >= 40:
        Grade = 'D'
    student = [Name, Age, Sex, First_C_A, Lab_Test, Exam, term_score , Grade]
    students.append(student)
    i += 1
with open('students_data.csv', 'w', newline='') as f:
    write = csv.writer(f)
    write.writerow(fields)
    write.writerows(students)
