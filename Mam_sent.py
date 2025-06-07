from tkinter import *
import mysql.connector as mysql
import tkinter.messagebox as MessageBox

from tkinter import ttk
#--------------------------------------add test-------------------------------------------------
def addtestwindow():
    testname=StringVar()
    def add():
        
        con=mysql.connect(host="localhost",user="root",password="ente01Pwd",database="srms")
        cursor=con.cursor()
        cursor.execute(f"insert into test(test_name) values('{testname_entry.get()}')")
        cursor.execute("commit")
        con.close()
    def delete():
        pass
    def clear():
        pass

    test_win=Toplevel(root)
    test_win.geometry("400x250+200+200")
    test_win.title("Add Test")
    newtest_frame=LabelFrame(test_win,bg="#033054",\
    font=("Arial",15,"bold"),relief="ridge",bd=5)

    newtest_frame.place(x=20,y=20,width=350,height=200)
    testname_lbl=Label(newtest_frame,text="Test Name:",font=("goudy old family",15),bg="#033054",fg="white")
    testname_entry=Entry(newtest_frame,textvariable=testname,font=("goudy old family",12))
    button_frame=Frame(newtest_frame,relief="groove",bd=5,bg="#033054")

    button_frame.place(x=10,y=100,width=300,height=60)
    add_btn=Button(button_frame,text="Add",font=("goudy old family",15),\
    bd=5,fg="#033054",bg="white",width=6,command=add)
    delete_btn=Button(button_frame,text="Delete",font=("goudy old family",15),\
    bd=5,fg="#033054",bg="white",width=6,command=delete)
    clear_btn=Button(button_frame,text="Clear",font=("goudy old family",15),\
    bd=5,fg="#033054",bg="white",width=6,command=clear)
    
    testname_lbl.grid(row=1,column=0,padx=10,pady=10)
    testname_entry.grid(row=1,column=1,padx=10,pady=10)
    add_btn.grid(row=0,column=0,padx=5,pady=5)
    delete_btn.grid(row=0,column=1,padx=5,pady=5)
    clear_btn.grid(row=0,column=2,padx=5,pady=5)
#--------------------------------------------------------------------------------------------------

def addsubjectwindow():
    subname=StringVar()
    
    def add():
        
        con=mysql.connect(host="localhost",user="root",password="ente01Pwd",database="srms")
        cursor=con.cursor()
        cursor.execute(f"insert into subject(subject_name) values('{subname_entry.get()}')")
        cursor.execute("commit")
        con.close()
    def delete():
        pass
    def clear():
        pass

    sub_win=Toplevel(root)
    sub_win.geometry("400x250+200+200")
    sub_win.title("Add Test")
    newsub_frame=LabelFrame(sub_win,bg="#033054",\
    font=("Arial",15,"bold"),relief="ridge",bd=5)

    newsub_frame.place(x=20,y=20,width=350,height=200)
    subname_lbl=Label(newsub_frame,text="Sub Name:",font=("goudy old family",15),bg="#033054",fg="white")
    subname_entry=Entry(newsub_frame,textvariable=subname,font=("goudy old family",12))
    button_frame=Frame(newsub_frame,relief="groove",bd=5,bg="#033054")

    button_frame.place(x=10,y=100,width=300,height=60)
    add_btn=Button(button_frame,text="Add",font=("goudy old family",15),\
    bd=5,fg="#033054",bg="white",width=6,command=add)
    delete_btn=Button(button_frame,text="Delete",font=("goudy old family",15),\
    bd=5,fg="#033054",bg="white",width=6,command=delete)
    clear_btn=Button(button_frame,text="Clear",font=("goudy old family",15),\
    bd=5,fg="#033054",bg="white",width=6,command=clear)
    
    subname_lbl.grid(row=1,column=0,padx=10,pady=10)
    subname_entry.grid(row=1,column=1,padx=10,pady=10)
    add_btn.grid(row=0,column=0,padx=5,pady=5)
    delete_btn.grid(row=0,column=1,padx=5,pady=5)
    clear_btn.grid(row=0,column=2,padx=5,pady=5)
#--------------------------------------------------------------------------------------------------
def addstudentwindow():
    name=StringVar()
    rollno=StringVar()
    clas=StringVar()
    sec=StringVar()
    
    
    def add():
        
        con=mysql.connect(host="localhost",user="root",password="ente01Pwd",database="srms")
        cursor=con.cursor()
        cursor.execute(f"insert into student(rollno,name,class,sec) values('{studroll_entry.get()}','{studname_entry.get()}','{class_entry.get()}','{sec_entry.get()}')")
        cursor.execute("commit")
        con.close()
    def delete():
        pass
    def clear():
        pass

    stud_win=Toplevel(root)
    stud_win.geometry("400x320+200+200")
    stud_win.title("Add Test")
    newstud_frame=LabelFrame(stud_win,bg="#033054",\
    font=("Arial",15,"bold"),relief="ridge",bd=5)

    newstud_frame.place(x=20,y=20,width=350,height=300)
    studname_lbl=Label(newstud_frame,text="Name:",font=("goudy old family",15),bg="#033054",fg="white")
    studname_entry=Entry(newstud_frame,textvariable=name,font=("goudy old family",12))
    studroll_lbl=Label(newstud_frame,text="Roll No:",font=("goudy old family",15),bg="#033054",fg="white")
    studroll_entry=Entry(newstud_frame,textvariable=rollno,font=("goudy old family",12))
    class_lbl=Label(newstud_frame,text="Class:",font=("goudy old family",15),bg="#033054",fg="white")
    class_entry=Entry(newstud_frame,textvariable=clas,font=("goudy old family",12))
    sec_lbl=Label(newstud_frame,text="Section:",font=("goudy old family",15),bg="#033054",fg="white")
    sec_entry=Entry(newstud_frame,textvariable=sec,font=("goudy old family",12))
    button_frame=Frame(newstud_frame,relief="groove",bd=5,bg="#033054")

    button_frame.place(x=10,y=200,width=300,height=60)
    add_btn=Button(button_frame,text="Add",font=("goudy old family",15),\
    bd=5,fg="#033054",bg="white",width=6,command=add)
    delete_btn=Button(button_frame,text="Delete",font=("goudy old family",15),\
    bd=5,fg="#033054",bg="white",width=6,command=delete)
    clear_btn=Button(button_frame,text="Clear",font=("goudy old family",15),\
    bd=5,fg="#033054",bg="white",width=6,command=clear)
    
    studname_lbl.grid(row=0,column=0,padx=10,pady=10)
    studname_entry.grid(row=0,column=1,padx=10,pady=10)
    studroll_lbl.grid(row=1,column=0,padx=10,pady=10)
    studroll_entry.grid(row=1,column=1,padx=10,pady=10)
    class_lbl.grid(row=2,column=0,padx=10,pady=10)
    class_entry.grid(row=2,column=1,padx=10,pady=10)
    sec_lbl.grid(row=3,column=0,padx=10,pady=10)
    sec_entry.grid(row=3,column=1,padx=10,pady=10)
    add_btn.grid(row=0,column=0,padx=5,pady=5)
    delete_btn.grid(row=0,column=1,padx=5,pady=5)
    clear_btn.grid(row=0,column=2,padx=5,pady=5)
#-----------------------Add mark------------------------------------------------------------------
def addmarkwindow():

    
    rollno=StringVar()
    sub=StringVar()
    test=StringVar()
    mark=IntVar()
    
    def add():
        
        con=mysql.connect(host="localhost",user="root",password="ente01Pwd",database="srms")
        cursor=con.cursor()
        m=int(mark_entry.get())
        cursor.execute(f"insert into result(rollno,subject,test,mark) values('{rollno_entry.get()}','{subject_entry.get()}','{test_entry.get()}','{m}')")
        cursor.execute("commit")
        con.close()
    def delete():
        pass
    def clear():
        mark.set(0)
    def populate_combo():
        con=mysql.connect(host="localhost",user="root",password="ente01Pwd",database="srms")
        cursor=con.cursor()
        cursor.execute("select subject_name from subject")
        result_set=cursor.fetchall()
        subject_entry['values']=result_set
        con.commit()
        cursor.execute("select test_name from test")
        result_set=cursor.fetchall()
        test_entry['values']=result_set
        con.commit()
        cursor.execute("select rollno from student")
        result_set=cursor.fetchall()
        rollno_entry['values']=result_set
        con.commit()
        con.close()

    
    mark_win=Toplevel(root)
    mark_win.geometry("400x320+200+200")
    mark_win.title("Add Mark")
    newmark_frame=LabelFrame(mark_win,bg="#033054",\
    font=("Arial",15,"bold"),relief="ridge",bd=5)

    newmark_frame.place(x=20,y=20,width=350,height=300)
    rollno_lbl=Label(newmark_frame,text="RollNo:",font=("goudy old family",15),bg="#033054",fg="white")
    rollno_entry=ttk.Combobox(newmark_frame,textvariable=rollno,font=("goudy old family",12))
    
    subject_lbl=Label(newmark_frame,text="Subject:",font=("goudy old family",15),bg="#033054",fg="white")
    subject_entry=ttk.Combobox(newmark_frame,textvariable=sub,font=("goudy old family",12))
    test_lbl=Label(newmark_frame,text="Test:",font=("goudy old family",15),bg="#033054",fg="white")
    test_entry=ttk.Combobox(newmark_frame,textvariable=test,font=("goudy old family",12))
    mark_lbl=Label(newmark_frame,text="Mark:",font=("goudy old family",15),bg="#033054",fg="white")
    mark_entry=Entry(newmark_frame,textvariable=mark,font=("goudy old family",12))
    
    button_frame=Frame(newmark_frame,relief="groove",bd=5,bg="#033054")

    button_frame.place(x=10,y=200,width=300,height=60)
    add_btn=Button(button_frame,text="Add",font=("goudy old family",15),\
    bd=5,fg="#033054",bg="white",width=6,command=add)
    delete_btn=Button(button_frame,text="Delete",font=("goudy old family",15),\
    bd=5,fg="#033054",bg="white",width=6,command=delete)
    clear_btn=Button(button_frame,text="Clear",font=("goudy old family",15),\
    bd=5,fg="#033054",bg="white",width=6,command=clear)
    
    rollno_lbl.grid(row=0,column=0,padx=10,pady=10)
    rollno_entry.grid(row=0,column=1,padx=10,pady=10)
    subject_lbl.grid(row=1,column=0,padx=10,pady=10)
    subject_entry.grid(row=1,column=1,padx=10,pady=10)
    test_lbl.grid(row=2,column=0,padx=10,pady=10)
    test_entry.grid(row=2,column=1,padx=10,pady=10)
    mark_lbl.grid(row=3,column=0,padx=10,pady=10)
    mark_entry.grid(row=3,column=1,padx=10,pady=10)
    add_btn.grid(row=0,column=0,padx=5,pady=5)
    delete_btn.grid(row=0,column=1,padx=5,pady=5)
    clear_btn.grid(row=0,column=2,padx=5,pady=5)
    populate_combo()
#--------------------------------------------------------------------------------------------------
def show_results():

    def search():
        
        con=mysql.connect(host="localhost",user="root",password="ente01Pwd",database="srms")
        cursor=con.cursor()
        

        cursor.execute(f"select name,class,sec,subject,test,mark from student,result where student.rollno=result.rollno && {search_by.get()}='{val1.get()}' && {searchby.get()}='{val2.get()}' ")
        
        result_set=cursor.fetchall()
        
        
        if len(result_set)!=0:
           mark_table.delete(*mark_table.get_children())
           for row in result_set:
                 mark_table.insert('',END,values=row)
     
        else:
            MessageBox.showinfo("Status","No record Found")
        cursor.execute("commit")
        con.close()
        #searchby_entry.delete(0,END)'''
#-------------------------------------------------------------------------------------------------
    window=Toplevel(root)
    window.geometry("860x560+50+50")
    window.title("Show Resuls")

    data_frame=Frame(window,relief="groove",bg="lightgray",bd=5)
    data_frame.place(x=0,y=0,width=850,height=550)

    search_frame=Frame(data_frame,relief="groove",bd=5)
    search_frame.pack(side="top",fill="x")
    

    search_by=ttk.Combobox(search_frame,font=("Arial",12,"bold"))
    search_by['values']=("name","class","section","Subject","Test")
    val1=Entry(search_frame)
    val2=Entry(search_frame)
    val1.grid(row=0,column=1,padx=2,pady=2)
    val2.grid(row=0,column=3,padx=2,pady=2)
    search_by.grid(row=0,column=0,padx=2,pady=2)
    searchby=ttk.Combobox(search_frame,font=("Arial",12,"bold"))
    searchby['values']=("name","class","section","Subject","Test")
    searchby.grid(row=0,column=2,padx=2,pady=2)
    

    search_btn=Button(search_frame,text="Search",font=("arial",12,"bold"),bd=5,width=12,command=search)
    search_btn.grid(row=0,column=4,padx=10,pady=5)

#-------------------------------add scroll bar--------------------------------------------------------------

    y_scroll=ttk.Scrollbar(data_frame,orient=VERTICAL)
    x_scroll=ttk.Scrollbar(data_frame,orient=HORIZONTAL)
    mark_table=ttk.Treeview(data_frame,columns=("Name","Class","Section","Subject","Test","Mark"),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)
    y_scroll.config(command=mark_table.yview)
    x_scroll.config(command=mark_table.xview)
    y_scroll.pack(side=RIGHT,fill="y")
    x_scroll.pack(side=BOTTOM,fill="x")

    
    mark_table.heading("Name",text="Name")
    mark_table.heading("Class",text="Class")
    mark_table.heading("Section",text="Section")
    mark_table.heading("Subject",text="Subject")
    mark_table.heading("Test",text="Test")
    mark_table.heading("Mark",text="Mark")

    mark_table.pack(fill="both",expand=True)
    mark_table["show"]='headings'

    
    mark_table.column("Name",width=100)
    mark_table.column("Class",width=100)
    mark_table.column("Section",width=100)
    mark_table.column("Subject",width=100)
    mark_table.column("Test",width=100)
    mark_table.column("Mark",width=100)

    mark_table.pack(fill="both",expand=True)
    mark_table["show"]='headings'
    
#--------------------------------------------------------------------------------------------------

root=Tk()
root.title("Student Result Management System")
root.geometry("1350x700+0+0")
title=Label(root,text="Student Management System",font=("goudy old family",20,"bold"),bg="#033054",fg="white")
title.place(x=0,y=0,relwidth=1,height=40)
menu_frame=LabelFrame(root,text="Menu",font=("times new roman",15))
menu_frame.place(x=0,y=50,width=1340,height=80)
add_test=Button(menu_frame,text="Add Test",font=("Goudy old style",15,"bold"),\
                cursor="hand2",bg="#0b5377",fg="white",command=addtestwindow)
add_test.place(x=10,y=5,height=40,width=150)
add_student=Button(menu_frame,text="Add Student",font=("Goudy old style",15,"bold"),\
                   cursor="hand2",bg="#0b5377",fg="white",command=addstudentwindow)
add_student.place(x=170,y=5,height=40,width=150)
add_subject=Button(menu_frame,text="Add Subject",font=("Goudy old style",15,"bold"),\
                   cursor="hand2",bg="#0b5377",fg="white",command=addsubjectwindow)
add_subject.place(x=330,y=5,height=40,width=150)
add_teacher=Button(menu_frame,text="Add Teacher",font=("Goudy old style",15,"bold"),
                   cursor="hand2",bg="#0b5377",fg="white")
add_teacher.place(x=500,y=5,height=40,width=150)
add_result=Button(menu_frame,text="Add Result",font=("Goudy old style",15,"bold"),\
                  cursor="hand2",bg="#0b5377",fg="white",command=addmarkwindow)
add_result.place(x=690,y=5,height=40,width=150)
show_results_view=Button(menu_frame,text="View Result",font=("Goudy old style",15,"bold"),\
                cursor="hand2",bg="#0b5377",fg="white",command=show_results)
show_results_view.place(x=900,y=5,height=40,width=150)
add_exit=Button(menu_frame,text="Exit",font=("Goudy old style",15,"bold"),cursor="hand2",bg="#0b5377",fg="white")
add_exit.place(x=1100,y=5,height=40,width=150)


root.mainloop()
