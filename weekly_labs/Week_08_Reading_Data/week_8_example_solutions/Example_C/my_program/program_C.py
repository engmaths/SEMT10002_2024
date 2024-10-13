import csv

with open('../my_data/student_marks.csv') as f:
    
    f = csv.reader(f)

    f = list(f)
    print(f)

# marks = [int(line[1]) for line in f]

marks = []
for line in f:
    marks.append(int(line[1]))

print(marks)

mean = sum(marks)/len(marks)
print(mean)

grades = []

for m in marks:
    if m >= 70:
        grades.append('A')
    elif m >= 60:
        grades.append('B')
    elif m >= 50:
        grades.append('C')
    elif m >= 40:
        grades.append('D')
    else:
        grades.append('E')

print(grades)

# grades = [[g] for g in grades]

# new_data = [line + [g] for line,g in zip(f, grades)]

new_data = []

for line, g in zip(f, grades):
    line.append(g)
    new_data.append(line)

with open('../my_data/student_grades.csv', 'w') as file:
    
    file = csv.writer(file)

    # file.writerows(grades)
    file.writerows(new_data)









