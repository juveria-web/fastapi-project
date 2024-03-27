from fastapi import FastAPI, Request
from  model import  student
import dbal
# predefined module contains predefined class to chk whether user given i/p is correct/not
from pydantic import BaseModel
 # This class is defined to check user given input or to perform validation

class studentDataType(BaseModel):
     Rollno : int       
     fname : str
     lname : str
     subject: str
     marks : int
     city : str
     address: str
     zipcode :int
 #app is an object of FastAPI() class to use its method you can give any name
app = FastAPI()

   # creating 1st API to fetch/get all student data

@app.get("/") 

# defining a method that will excute when above endpoint hits
def getstudent():  

   # defining an empty list that will store all student details right now its 
    
    emp = []
  # calling Getstudent() method that is defined in dbal file/module
    
    rows = dbal.Getstudent()
 # using for loop in order to iterate each row of studentdata
    
    for row in rows:
        print(rows) 
    # creating an object 'value' of 'student' class to fectch/get each row of studentdata
        
        value = student(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])

     
        emp.append(value)
         # finally returns the result in json form where "student" is key (an object
    return {"value" : emp}

# creating 2nd API to add/insert new student data/record

@app.post("/add")
# defining a method that will excute when above endpoint hits

def addNewStudent(obj : studentDataType):

   # print("\n\n", obj, "\n\n")
       # creating an object 'objstu' of 'student' class to add/insert new record i
    
    objStu = student(obj.Rollno, obj.fname, obj.lname, obj.subject, obj.marks, obj.city, obj.address,obj.zipcode)

 # calling Addstudent() method that is defined in dbal file/module and passing our above filled object '
    
    dbal.Addstudent(objStu)

    return {"message" : "Successfully added new student."}


## creating 3rd API to delete particular employee record based on empno as it is

@app.delete("/delete")

def deleteStudent(obj: studentDataType):

    # print(obj)studentDataType
    # creating an object 'objstu' of 'student' class and passing values to each of its attribute

    objstu = student(obj.Rollno, obj.fname, obj.lname, obj.subject, obj.marks, obj.city, obj.address, obj.zipcode)

     # calling Deletestudent() method that is defined in dbal file/module and passing our above filled object'objstu' as a parameter that will catched by Updatestudent(objstu) method as an argument


    dbal.Delete(objstu.Rollno)

     # finally returns the result by displaying the success message
    
    return {"message":"Deleted the selected record."}

# creating 4th API to update particular student record based on Rollno as it is a Primary Key
 
@app.put("/update")
# defining a method that will excute when above endpoint hits

def updatestudent(obj : studentDataType):
      
       # creating an object 'objstu' of 'student' class and passing values to each of its attributes

      objStu = student(obj.Rollno, obj.fname, obj.lname, obj.subject, obj.marks, obj.city, obj.address,obj.zipcode)

       # calling Updatestudent() method that is defined in dbal file/module and passing our above filled object
      dbal.Updatestudent(objStu)
      
      return {"message": "Updated the selected record."}


