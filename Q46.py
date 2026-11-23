# Q46. Accept five subject marks from the user and display their total
marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

print("Total marks =", sum(marks))
