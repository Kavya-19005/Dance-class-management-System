from tkinter import *
import Search_detail
import Updat_detail
import delete_detail
from PIL import ImageTk, Image
#=======Base==============


def search():
        Search_detail.display()
        
def update():
        Updat_detail.display()
def delete():
        delete_detail.display()

def display():
    root_2=Tk()
    root_2.title("Dance Class Management System")
    root_2.geometry("1920x1080+0+0")
    root_2.config(bg="#F8F1E9")

    
    #=======Heading==========
    hdng=Label(root_2,text="Student Details",fg="white",bg="#AA6F73",font=("Times New Roman",16,"bold"),bd=7,relief="ridge")
    hdng.place(x=0,y=0,width=1355,height=70)



    #==============Button================
    search_b=Button(root_2,text="Search and View Student detail",font=("Times New Roman",15,"bold"),command=search,bg="#BF656F",fg="white",padx=50,pady=50,relief="ridge")
    search_b.place(x=520,y=150,height=70,width=300)


    s_update_b=Button(root_2,text="Update Student detail",font=("Times New Roman",15,"bold"),command=update,bg="#BF656F",fg="white",padx=50,pady=50,relief="ridge")
    s_update_b.place(x=520,y=300,height=70,width=300)

    s_delete_b=Button(root_2,text="Delete Student detail",font=("Times New Roman",15,"bold"),command=delete,bg="#BF656F",fg="white",padx=50,pady=50,relief="ridge")
    s_delete_b.place(x=520,y=450,height=70,width=300)

    mainloop()



