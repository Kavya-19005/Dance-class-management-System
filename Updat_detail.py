from tkinter import *
from tkinter import ttk
import mysql.connector as mysql
import tkinter.messagebox as MessageBox

#=========Base=================
def display():
    base_3=Tk()
    base_3.title("Dance Class Management System")
    base_3.geometry("800x1060+0+0")
    base_3.config(bg="#F8F1E9")

    #=======Heading==========
    hdng=Label(base_3,text="Update Student Details",fg='white',bg="#AA6F73",font=("Times New Roman",16,"bold"),bd=4,relief="ridge")
    hdng.place(x=0,y=0,width=800,height=70)

    stud_id_lbl=Label(base_3,text="Student ID :",bg="#F8F1E9",font=("Times New Roman",16,"bold"))
    stud_id_lbl.place(x=100,y=150)

    stud_id=Entry(base_3,bd=5)
    stud_id.place(x=210,y=150)


    cat_lbl=Label(base_3,text="Category of Updation :",bg="#F8F1E9",font=("Times New Roman",16,"bold"))
    cat_lbl.place(x=80,y=250)

    cat_entry=ttk.Combobox(base_3,font=("Arial",12,"bold"))
    cat_entry['values']=("admission_id","name","DOB","gender","father_name","mother_name")
    cat_entry.place(x=290,y=260)

    updt_entry=Entry(base_3,bd=5)
    updt_entry.place(x=600,y=260)

    def update():
        con=mysql.connect(host="localhost",user="root",password="kavikavya123",database="dncedb")
        cursor=con.cursor()
        cursor.execute(f"update admission set {cat_entry.get()}=('{updt_entry.get()}') where admission_id=('{stud_id.get()}')")
        cursor.execute("commit")
        con.close()

    updt_b=Button(base_3,text="Update",bg="#AA6F73",fg="white",font=("Times New Roman",16,"bold"),command=update)
    updt_b.place(x=180,y=500)


    base_3.mainloop()


