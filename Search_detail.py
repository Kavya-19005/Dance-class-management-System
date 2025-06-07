from tkinter import *
import mysql.connector as mysql
import tkinter.messagebox as MessageBox
from tkinter import ttk

#=========Base=================
def display():
    base_1=Tk()
    base_1.title("Dance Class Management System")
    base_1.geometry("930x1060+0+0")
    base_1.config(bg="#F8F1E9")

    #=======Heading==========
    def view():
        con=mysql.connect(host="localhost",user="root",password="kavikavya123",database="dncedb")
        cursor=con.cursor()
        cursor.execute(f"select * from admission")
        result_set=cursor.fetchall()
        if len(result_set)!=0:
            data_table.delete(*data_table.get_children())
            for row in result_set:
                data_table.insert('',END,values=row)
         
        else:
            MessageBox.showinfo("Status","No record Found")

        cursor.execute("commit")
        con.close()

    def search_tbl():
        con=mysql.connect(host="localhost",user="root",password="kavikavya123",database="dncedb")
        cursor=con.cursor()
        cursor.execute(f"select * from admission where {search_by.get()}='{val1.get()}' ")
        result_set=cursor.fetchall()
        if len(result_set)!=0:
            data_table.delete(*data_table.get_children())
            for row in result_set:
                data_table.insert('',END,values=row)
         
        else:
            MessageBox.showinfo("Status","No record Found")

        if search_by.get() and val1.get() == '':
            MessageBox.showinfo("Status","Please select!")

        cursor.execute("commit")
        con.close()
    

    

    data_frame=Frame(base_1,relief="groove",bg="#F8F1E9",bd=5)
    data_frame.place(x=35,y=80,width=850,height=550)

    search_frame=Frame(data_frame,relief="groove",bg="#AA6F73",bd=5)
    search_frame.pack(side="top",fill="x")
        
    search_by=ttk.Combobox(search_frame,font=("Arial",12,"bold"))
    search_by['values']=("Admission_id","name","DOB","Gender","Father_name","Mother_name")
    val1=Entry(search_frame)
   
    val1.grid(row=0,column=1,padx=2,pady=2)
    
    search_by.grid(row=0,column=0,padx=2,pady=2)


    #-------------------------------add scroll bar--------------------------------------------------------------

    y_scroll=ttk.Scrollbar(data_frame,orient=VERTICAL)
    x_scroll=ttk.Scrollbar(data_frame,orient=HORIZONTAL)
    data_table=ttk.Treeview(data_frame,columns=("Admission_id","name","DOB","Gender","Father_name","Mother_name"),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)
    y_scroll.config(command=data_table.yview)
    x_scroll.config(command=data_table.xview)
    y_scroll.pack(side=RIGHT,fill="y")
    x_scroll.pack(side=BOTTOM,fill="x")

        
    data_table.heading("Admission_id",text="Admission_id")
    data_table.heading("name",text="name")
    data_table.heading("DOB",text="DOB")
    data_table.heading("Gender",text="Gender")
    data_table.heading("Father_name",text="Father_name")
    data_table.heading("Mother_name",text="Mother_name")

    data_table.pack(fill="both",expand=True)
    data_table["show"]='headings'

        
    data_table.column("Admission_id",width=100)
    data_table.column("name",width=100)
    data_table.column("DOB",width=100)
    data_table.column("Gender",width=100)
    data_table.column("Father_name",width=100)
    data_table.column("Mother_name",width=100)

    data_table.pack(fill="both",expand=True)
    data_table["show"]='headings'

    view_b=Button(search_frame,text="View All",font=("Times New Roman",15,"bold"),command=view,bg="#BF656F",fg="white",padx=50,pady=50,relief="ridge")
    view_b.place(x=410,y=0,height=29,width=80)


    hdng=Label(base_1,text="Search Student Details",fg="white",bg="#AA6F73",font=("Times New Roman",16,"bold"),bd=4,relief="ridge")
    hdng.place(x=0,y=0,width=930,height=70)

    search_b=Button(search_frame,text="Search",font=("Times New Roman",15,"bold"),command=search_tbl,bg="#BF656F",fg="white",padx=50,pady=50,relief="ridge")
    search_b.place(x=610,y=0,height=29,width=75)



    

    mainloop()



