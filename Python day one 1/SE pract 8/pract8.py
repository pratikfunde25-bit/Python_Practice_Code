# # ---------- CLASS FOR STUDENT DETAILS ----------
# class Student:
#     def __init__(self):
#         self.first_name = ""
#         self.middle_name = ""
#         self.last_name = ""
#         self.class_name = ""
#         self.academic_year = ""
#         self.ucid = ""
#         self.department = ""

#     # Method to accept student details
#     def accept_details(self):
#         print("----- Enter Student Details -----")
#         self.first_name = input("Enter First Name: ")
#         self.middle_name = input("Enter Middle Name: ")
#         self.last_name = input("Enter Last Name: ")
#         self.class_name = input("Enter Class: ")
#         self.academic_year = input("Enter Academic Year: ")
#         self.ucid = input("Enter UCID: ")
#         self.department = input("Enter Department: ")

#     # Method to display student details
#     def display_details(self):
#         print("\n----- STUDENT INFORMATION -----")
#         print("First Name:", self.first_name)
#         print("Middle Name:", self.middle_name)
#         print("Last Name:", self.last_name)
#         print("Class:", self.class_name)
#         print("Academic Year:", self.academic_year)
#         print("UCID:", self.ucid)
#         print("Department:", self.department)


# # ---------- CLASS FOR MARKS & RESULT ----------
# class Result:
#     def __init__(self):
#         self.se = 0
#         self.dbms = 0
#         self.ds = 0
#         self.total = 0
#         self.percentage = 0.0

#     # Method to accept marks
#     def accept_marks(self):
#         print("\n----- Enter Marks (out of 100) -----")
#         self.se = int(input("Enter SE Marks: "))
#         self.dbms = int(input("Enter DBMS Marks: "))
#         self.ds = int(input("Enter DS Marks: "))

#     # Method to calculate total and percentage
#     def calculate_result(self):
#         self.total = self.se + self.dbms + self.ds
#         self.percentage = self.total / 3

#     # Method to display marksheet
#     def display_result(self):
#         print("\n----- STUDENT MARKS -----")
#         print("SE:", self.se)
#         print("DBMS:", self.dbms)
#         print("DS:", self.ds)
#         print("Total Marks:", self.total)
#         print("Percentage:", self.percentage)


# # ---------- MAIN PROGRAM ----------
# student = Student()
# result = Result()

# student.accept_details()
# result.accept_marks()

# result.calculate_result()

# print("\n========== FINAL STUDENT RESULT ==========")
# student.display_details()
# result.display_result()
# print("==========================================")



class Student:
    def __init__(self):
        self.data = {}     # dictionary to store all details

    def accept_details(self):
        print("----- Enter Student Details -----")
        self.data["First Name"] = input("Enter First Name: ")
        self.data["Middle Name"] = input("Enter Middle Name: ")
        self.data["Last Name"] = input("Enter Last Name: ")
        self.data["Class"] = input("Enter Class: ")
        self.data["Academic Year"] = input("Enter Academic Year: ")
        self.data["UCID"] = input("Enter UCID: ")
        self.data["Department"] = input("Enter Department: ")

    def display_details(self):
        print("\n----- STUDENT INFORMATION -----")
        for key, value in self.data.items():
            print(f"{key}: {value}")


class Result:
    def __init__(self):
        self.marks = {}     # dictionary for marks & result

    def accept_marks(self):
        print("\n----- Enter Marks (out of 100) -----")
        self.marks["SE"] = int(input("Enter SE Marks: "))
        self.marks["DBMS"] = int(input("Enter DBMS Marks: "))
        self.marks["DS"] = int(input("Enter DS Marks: "))

    def calculate(self):
        total = self.marks["SE"] + self.marks["DBMS"] + self.marks["DS"]
        percentage = total / 3
        self.marks["Total"] = total
        self.marks["Percentage"] = percentage

    def display(self):
        print("\n----- MARKS & RESULT -----")
        for key, value in self.marks.items():
            print(f"{key}: {value}")


# -------- MAIN PROGRAM --------
s = Student()
r = Result()

s.accept_details()
r.accept_marks()
r.calculate()

print("\n========== FINAL STUDENT RESULT ==========")
s.display_details()
r.display()
print("==========================================")
