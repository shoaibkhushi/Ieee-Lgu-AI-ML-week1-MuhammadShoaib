name = input("Enter Student Name: ")
roll_no = input("Enter Student Roll_No: ")

#subject
Subject ={}
Subject_Number = int(input("How Much you Want Subject Enter Min(Subject 3):"))
for i in range(Subject_Number):
    subject_name = input(f"Enter Subject {i+1} Name: ")
    marks = int(input(f"Enter {subject_name} Marks : "))
    Subject[subject_name]= marks
Student = {
    "Name":name,
    "Roll_No":roll_no,
    "Subjects":Subject
}    
total_marks = sum(Subject.values())
total_subject = len(Subject)
avg_marks= total_marks/total_subject

#Calculate Grade
if avg_marks >= 80:
    Action = "A"
elif avg_marks >= 70:
    Action = "B"
elif avg_marks >= 60:
    Action = "C"
elif avg_marks >= 50:
    Action = "D"
else:
    Action = "Fail"

#Attendence Checker
total_class = int(input("Enter Total Class: "))
attend_class = int(input("Enter Total Attend Class: "))

Attendence_Rate = (attend_class/total_class)*100
#Check Attendence Eligibilty
if Attendence_Rate >= 75:
    Action2 = f"You Are Eligible For Exam Your Attendence {Attendence_Rate:.2f}%"
else:
    Action2 = f"You are not Eligible For Exam Your Attendence {Attendence_Rate:.2f}%"

#Student Dashbord
print("="*50)
print("                 STUDENT DASHBOARD           ")
print("="*50)
print("-"*50)
print(f"Student_Name:  {name}")
print(f"Roll_No   :{roll_no}")
print("-"*50)
print(f"{'Subject':<20} {'Marks':>10}")
print("-"*50)
for subject_name, marks in Subject.items():
    print(f"{subject_name: <20} {marks :>10}")
print("-"*50)
print(f"{'Total Marks': <20} {total_marks:>10}")
print(f"{'Average Marks':<20} {avg_marks :>10.2f}")
print("-"*50)
print(f"Grade        :{Action}")
print(f"Exam Status  :{Action2}")
print("="*50)