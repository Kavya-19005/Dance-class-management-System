from tkinter import *
from tkinter import ttk
import mysql.connector as mysql
import tkinter.messagebox as MessageBox
from PIL import ImageTk, Image
#===========================


#=======Base==============
def display():
    root_1=Tk()
    root_1.title("Dance Class Management System")
    root_1.geometry("500x1080+0+0")
    root_1.config(bg="#F8F1E9")

    #=======Heading==========
    hdng=Label(root_1,text="Admission",bg="#AA6F73",font=("Times New Roman",16,"bold"),bd=7,relief="ridge")
    hdng.place(x=0,y=0,width=500,height=70)

    #=========Entry Labels===============

    #=======Admission_no=======
    adm_no_lbl=Label(root_1,text="Admission \n No :",bg="#F8F1E9",font=("Times New Roman",16,"bold"))
    adm_no_lbl.place(x=80,y=100)

    adm_no=Entry(root_1,bd=5)
    adm_no.place(x=180,y=110)

    #==name===
    name_lbl=Label(root_1,text="Name :",bg="#F8F1E9",font=("Times New Roman",16,"bold"))
    name_lbl.place(x=100,y=150)

    name=Entry(root_1,bd=5)
    name.place(x=180,y=150)

    #==DOB===
    DOB_lbl=Label(root_1,text="DOB :",bg="#F8F1E9",font=("Times New Roman",16,"bold"))
    DOB_lbl.place(x=100,y=200)


    DOB_y=Entry(root_1,bd=5)
    DOB_y.place(x=180,y=200)


    #==Gender==
    gender_lbl=Label(root_1,text="Gender :",bg="#F8F1E9",font=("Times New Roman",16,"bold"))
    gender_lbl.place(x=100,y=255)

    gender_entry=ttk.Combobox(root_1,font=("Arial",12,"bold"))
    gender_entry['values']=("Female","Male","Neither")
    gender_entry.place(x=180,y=255)



    #==Father name===
    f_name_lbl=Label(root_1,text="Father's \n Name :",bg="#F8F1E9",font=("Times New Roman",16,"bold"))
    f_name_lbl.place(x=100,y=305)

    f_name=Entry(root_1,bd=5)
    f_name.place(x=185,y=315)

    #==Mother name===
    m_name_lbl=Label(root_1,text="Mother's \n Name :",bg="#F8F1E9",font=("Times New Roman",16,"bold"))
    m_name_lbl.place(x=100,y=375)

    m_name=Entry(root_1,bd=5)
    m_name.place(x=185,y=380)
    
    continue_b=Button(root_1,text="Add",font=("Times New Roman",16,"bold"),bg="#BF656F",fg="white",command=add)
    continue_b.place(x=200,y=520)





    root_1.mainloop()


    #=============================

def add():
    con=mysql.connect(host="localhost",user="root",password="kavikavya123",database="dncedb")
    cursor=con.cursor()
    cursor.execute(f"insert into admission values('{adm_no.get()}','{name.get()}','{DOB_y.get()}',\
                   '{gender_entry.get()}','{f_name.get()}','{m_name.get()}')")
    cursor.execute("commit")
    con.close()


#display()

