import csv
def create():
    with open("student.csv","w") as obj:
        fobj=csv.writer(obj)
        fobj.writerow(['student ID','NAME','Class',' Roll Number','Batch ID'])
        while True:
            studentID=input("student id")
            Name=input("Name")
            Class=input("class")
            RollNumber=input("Roll Number")
            BatchID=input("Batch ID")
            i=[studentID,Name,Class,RollNumber,BatchID]
            fobj.writerow(i)
            j=int(input("1=Enter for update\n2=enter for exit"))
            if j==2:
                break;
def display():
    with open("student.csv","r")as obj:
        fobj=csv.reader(obj)
        for k in fobj:
            print(k)
create()
display()
def create():
    with open("course.csv","w")as m:
        fm=csv.writer(m)
        fm.writerow(['Course ID','Corse Nmae','Marks obtained'])

        while True:
            CourseID=input("enter course ID")
            CorseName=input("enter course name")
            Marksobtained=input("marks as studentID:Marks-studentID:Marks")
            p=[ CourseID,CorseName,Marksobtained]
            fm.writerow(p)
            j = int(input("1=Enter for update\n2=enter for exit"))
            if j == 2:
                break;

def display():
    with open("course.csv","r")as m:
        fm=csv.reader(m)
        for l in fm:
            print(l)
create()
display()
def create():
    with open("Batch.csv","w")as m:
        fm=csv.writer(m)
        fm.writerow(['Batch ID','Batch Name','Department Name','List of Course','List of student'])
        while True:
            BatchID=input("Batch ID")
            BatchName=input("Batch Name")
            DepartmentName=input("Department Name")
            ListofCourse=input("List of Course")
            Listofstudent=input("List of student")
            t=[BatchID,BatchName,DepartmentName,ListofCourse,Listofstudent]
            fm.writerow(t)
            j = int(input("1=Enter for update\n2=enter for exit"))
            if j == 2:
                break;
def display():
    with open("Batch.csv", "r") as m:
        fm = csv.reader(m)
        for l in fm:
         print(l)
create()
display()
def create():
    with open("Department.csv","w") as obj:
        fobj=csv.writer(obj)
        fobj.writerow(['DepartmentId','DepartmentName','List of Batches'])
        while True:
            DepartmentId=input("DepartmentId")

            DepartmentName=input("DepartmentName")

            ListofBatches=input("List of Batches")
            p=[ DepartmentId,DepartmentName,ListofBatches]
            fobj.writerow(p)
            j = int(input("1=Enter for update\n2=enter for exit"))
            if j == 2:
                break;


def display():
        with open("Department.csv", "r") as obj:
            fobj = csv.reader(obj)
            for l in fobj:
             print(l)
create()
display()
import csv
with open("Reportcard.csv","w")as m:
    fm=csv.writer(m)
    fm.writerow(['Subject','Marks','Grade'])
    Grade=None
    while True:
            Subject=input("Subject")

            Marks=int(input("Marks"))
            Grade=input("Grade")



            fm.writerow([Subject,Marks,Grade])
            j = int(input("1=Enter for update\n2=enter for exit"))
            if j == 2:
                     break


def display():
    with open("Reportcard.csv", "r") as m:
        fm = csv.reader(m)
        for l in fm:
            print(l)

display()
