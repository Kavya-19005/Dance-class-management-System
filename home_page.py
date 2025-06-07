from tkinter import *
import Admission_page
import view_detail
from PIL import ImageTk, Image
#=========Base=================
root=Tk()
root.title("Dance Class Management System")
root.geometry("1920x1080+0+0")
root.config(bg="#F8F1E9")

img_resize=Image.open(r'C:\Users\HP\Desktop\The Actual Project').resize((1440,720))
pic=ImageTk.PhotoImage(img_resize)
label=Label(root,image=pic)
label.place(x=0)

#==============Heading=====================================
Title= Label(root,text=" Dance School Management System ",fg="white",bg="#AA6F73",font=("Times New Roman",18,"bold"),bd=7,relief="ridge")
Title.place(x=0,y=0,width=1355,height=70)

 

def ad_mision():
    Admission_page.display()
    
def view_detail_fun():
    view_detail.display()


#============== Buttons=======================
admission_b=Button(root,text="Admission",font=("Times New Roman",15,"bold"),command=ad_mision,bg="#BF656F",fg="white",padx=50,pady=50,relief="ridge")
admission_b.place(x=350,y=150,height=50,width=200)

view_b=Button(root,text="View Student Details",font=("Times New Roman",15,"bold"),command=view_detail_fun,bg="#BF656F",fg="white",padx=50,pady=50,relief="ridge")
view_b.place(x=850,y=150,height=50,width=200)


root.mainloop()
