import mysql.connector
from tkinter import messagebox
#B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R

def Save_Data_MySql(B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R):
    try:
        mydb=mysql.connector.connect(host='localhost',user='root',password='root')
        mycursor=mydb.cursor()
        print("Connection Established!")
        
    except:
        messagebox.showerror("Connection","Database connection not established!")
        
    try:
        command="create database Heart_Data"
        mycursor.execute(command)
        
        command="use Heart_Data"
        mycursor.execute(command)
        
        command="create table data(user int auto_increment key not null, Name varchar(50), Date varchar(100), DOB varchar(100),age varchar(100),sex varchar(100),cp varchar(100),trestbps varchar(100),chol varchar(100),fbs varchar(100),restecg varchar(100),thalach varchar(100),exang varchar(100),oldpeak varchar(100),slope varchar(100),ca varchar(100),thal varchar(100),result varchar(100),)"
        mycursor.execute(command)
        
        command="insert into data(Name,Date,DOB,Age,Sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,result)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(command,(B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R))
        mydb.commit()
        mydb.close()
        messagebox.showinfo("Resgister","New user added successfully..")
        
    
    except:
        mycursor.execute("use Heart_Data")
        mydb=mysql.connector.connect(host='localhost',user='root',password='root',database="Heart_Data")
        mycursor=mydb.cursor()
        
        command="insert into data(Name,Date,DOB,Age,Sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,result)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(command,(B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R))
        mydb.commit()
        mydb.close()
        messagebox.showinfo("Resgister","New user added successfully..")
        
#Save_Date_MySql('abc','08/08/1990','1990','44','1','1','233','233','1','1','233','1','233','0','2','1','0')