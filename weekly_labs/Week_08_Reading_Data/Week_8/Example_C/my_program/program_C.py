import csv 

with open('../my_data/student_marks.csv') as f:
    f = csv.reader(f)
    f = list(f)
    print(f)
    values = []
    for item in f:
        values.append(int(item[1]))
    values = [int(item[1]) for item in f]
    print(values)

    print(sum(values)/len(values))

    grades = []

    for m in values:
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

# grades = [[g]for g in grades]

new_file_contents = []

# for line, grade in zip(f, grades):
#     line.append(grade)
#     new_file_contents.append(line)

new_file_contents = [line + [grade] for line, grade in zip(f, grades)]

print(new_file_contents)
    

with open('student_grades.csv', 'w') as f:
    f = csv.writer(f)
    f.writerows(new_file_contents)




