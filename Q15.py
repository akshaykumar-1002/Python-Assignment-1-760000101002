# Q15. Calculate total and average of five subject marks
marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

total = sum(marks)
average = total / 5

print("Total marks =", total)
print("Average marks =", average)
