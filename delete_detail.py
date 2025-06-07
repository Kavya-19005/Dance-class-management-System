from tkinter import *
import mysql.connector as mysql
import tkinter.messagebox as MessageBox
from tkinter import ttk

#==================================


#=========Base=================
def display():
    base_4=Tk()
    base_4.title("Dance Class Management System")
    base_4.geometry("500x500+0+0")
    base_4.config(bg="#F8F1E9")

    hdng=Label(base_4,text="Delete Student Details",fg="white",bg="#AA6F73",font=("Times New Roman",16,"bold"),bd=4,relief="ridge")
    hdng.place(x=0,y=0,width=500,height=70)

    stud_id_lbl=Label(base_4,text="Student ID",bg="#F8F1E9",font=("Times New Roman",16,"bold"))
    stud_id_lbl.place(x=100,y=150)

    stud_id=Entry(base_4,bd=5)
    stud_id.place(x=210,y=150)


    def delete():
        con=mysql.connect(host="localhost",user="root",password="kavikavya123",database="dncedb")
        cursor=con.cursor()
        cursor.execute(f"delete from admission where admission_id=('{stud_id.get()}')")
        cursor.execute("commit")
        con.close()

        

    delete_b=Button(base_4,text="Delete",font=("Times New Roman",15,"bold"),command=delete,bg="#BF656F",fg="white",padx=50,pady=50,relief="ridge")
    delete_b.place(x=25,y=250,height=50,width=200)

    cancel_b=Button(base_4,text="Cancel",command=base_4.destroy,font=("Times New Roman",15,"bold"),bg="#BF656F",fg="white",padx=50,pady=50,relief="ridge")
    cancel_b.place(x=275,y=250,height=50,width=200)

    mainloop()


