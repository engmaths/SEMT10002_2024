import csv

# Open the file
with open('../my_data/student_marks.csv') as f:
    
    f = csv.reader(f)

    # Display the contents 
    f = list(f)
    print(f)

# Get student marks as numerical values 
marks = []
for line in f:
    marks.append(int(line[1]))

# Another way to get student marks as numerical values
# marks = [int(line[1]) for line in f]

print(marks)

# Find the average of the student marks 
mean = sum(marks)/len(marks)
print(mean)

# Compute the grade associated with each mark
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


# Save grades to new file
with open('../my_data/student_grades.csv', 'w') as file:
    
    file = csv.writer(file)
    file.writerow(grades)


# Add grades as new column to original data
new_data = []
for line, g in zip(f, grades):
    line.append(g)
    new_data.append(line)


# Another way to add grades as new column to original data
# new_data = [line + [g] for line,g in zip(f, grades)]


with open('../my_data/student_marks_updated.csv', 'w') as file:
    
    file = csv.writer(file)

    # file.writerows(grades)
    file.writerows(new_data)









