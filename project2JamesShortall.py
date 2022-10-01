my_file = open("Project2.txt", 'r')
names = []
all_lines = my_file.readlines()
for line in all_lines:
    upper_case_line = line.upper()
    #  upper_case_line = upper_case_line.strip()
    studentid_and_gpa = upper_case_line.split(' : ')
    print(studentid_and_gpa[0])
print("Names are not shown to comply with FERPPA guidelines")