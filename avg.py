
grades = [85, 90, 78, 92, 88, 76, 95, 89, 84]

average_grade = sum(grades) / len(grades)


with open("average_grade.txt", "w") as file:
    file.write(f"The average grade of the students is: {average_grade:.2f}")

print("Average grade calculated and saved to 'average_grade.txt'")
