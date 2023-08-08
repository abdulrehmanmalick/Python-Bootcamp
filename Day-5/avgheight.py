# Calculate Average Student Height
student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)


total_height = 0

for height in student_heights:
    total_height += height

totalStudents = 0
for student in student_heights:
    totalStudents += 1

average_height = round(total_height / totalStudents)
print(average_height) 


# Without For loop:

HeightTotal = sum(student_heights)
totStudents = len(student_heights)
avgH = round(HeightTotal/totStudents)
print(avgH)