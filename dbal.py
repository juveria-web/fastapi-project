import pyodbc as p
from model import student
def Getconnection():
    conn = p.connect(r'Driver=SQL Server;Server=DESKTOP-6HB7143\SQLEXPRESS01;Database=studentData')
    return conn
def Getstudent():
    conn = Getconnection()
    cursor = conn.cursor()
    cursor.execute('select * from studentData')
    rows = cursor.fetchall()
    return rows
##    for row in rows:
##         
##        print(row)


def Addstudent(objData):
    conn = Getconnection()
    cursor = conn.cursor()
    cursor.execute(f"insert into studentData values ({objData.Rollno},'{objData.fname}','{objData.lname}','{objData.subject}',{objData.marks},'{objData.city}','{objData.address}',{objData.zipcode})")
                   
    conn.commit()
    print("new studentData added successfully")    
    Getstudent()

def Delete(RollnoToDelete):
    conn = Getconnection()
    cursor = conn.cursor()
    cursor.execute(f"Delete from studentData where Rollno = {RollnoToDelete}")
    conn.commit()

def GetstudentByRollno(studentRollno):
    conn = Getconnection()
    cursor = conn.cursor()
    cursor.execute(f'select* from studentData where Rollno = {studentRollno}')
    row = cursor.fetchone()
    objData = student(Rollno=row[0],fname=row[1],lname=row[2],subject=row[3],marks=row[4],city=row[5],address=row[6],zipcode=row[7])
    
    print(objData.__dict__)
    
    return objData


def Updatestudent(objData):
    conn = Getconnection()
    cursor = conn.cursor()
    cursor.execute(f"Update studentData set fname = '{objData.fname}',lname= '{objData.lname}',subject= '{objData.subject}',marks= {objData.marks},city='{objData.city}',address='{objData.address}',zipcode ={objData.zipcode} where Rollno = {objData.Rollno}")
    cursor.commit()
    print(" student Updated Succesfully")
    Getstudent()


  



                   
                   

        
