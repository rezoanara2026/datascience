marks = [88, 74, 93, -5, 61, 47, 105, 82, 59]

valid_marks = []
grade = {"A": 0, "B": 0, "C": 0, "F": 0}

for i in marks:
    if 0 <= i <= 100:
        valid_marks.append(i)

        if i >= 80:
            grade["A"] += 1
        elif i >= 70:
            grade["B"] += 1
        elif i >= 60:
            grade["C"] += 1
        else:
            grade["F"] += 1

average = sum(valid_marks) / len(valid_marks)

print("Valid marks:", valid_marks)
print("Grade counts:", grade)
print("Average:", average)