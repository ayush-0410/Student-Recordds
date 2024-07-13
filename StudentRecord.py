# Records for students
record1 = ['stdid', 'stdname', 'standard', 'age', 'Hindi', 'English', 'Maths', 'Science', 'Computer', 'Total']
record2 = ['stdid101', 'Ashish Kumar', '10th', 15, 67, 89, 87, 89, 90, 422]
record3 = ['stdid102', 'Abhishek Kumar', '10th', 14, 85, 45, 48, 90, 45, 313]
record4 = ['stdid103', 'Aman', '10th', 15, 23, 56, 78, 78, 67, 302]
record5 = ['stdid104', 'Rahul', '10th', 14, 45, 67, 45, 45, 56, 258]
record6 = ['stdid105', 'Ruby', '10th', 13, 89, 67, 89, 93, 65, 403]
record7 = ['stdid106', 'Sumam', '10th', 13, 90, 46, 67, 67, 67, 337]
record8 = ['stdid107', 'Saurabh', '10th', 15, 45, 23, 34, 45, 34, 181]
record9 = ['stdid108', 'Sumit', '10th', 14, 23, 45, 67, 78, 90, 303]
record10 = ['stdid109', 'Kamlesh', '10th', 15, 45, 56, 78, 99, 67, 303]
record11 = ['stdid110', 'Rohan', '10th', 15, 34, 12, 24, 45, 56, 171]

# List of all student records
student_record = [record1, record2, record3, record4, record5, record6, record7, record8, record9, record10, record11]

# Print all student records
for row in student_record:
    print(row)

print("---------------------------")
print("Name of students whose marks are more than 50 in English:")

# Check for students with English marks greater than 50
for rowindex in range(1, len(student_record)):
    if student_record[rowindex][5] > 50:  # Accessing English marks
        print(student_record[rowindex][1])  # Printing student name

for row in student_record:
    print(row)

print("---------------------------")
print("Name of students whose marks are more than 50 in Maths:")
for rowindex in range(1, len(student_record)):
    if student_record[rowindex][6] > 50:  # Accessing Maths marks
        print(student_record[rowindex][1])  