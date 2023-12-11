from tkinter import *
from tkinter import messagebox
root = Tk()

root.title("Consult tha doctor project")
root.geometry("600x600")

Q1_radioButton=StringVar(value="0")


q1 = Label(root,text="Do you have a ear pain?")
q1.pack()

Q1_r1=Radiobutton(root,text="yes",variable=Q1_radioButton,value="yes")
Q1_r1.pack()


Q1_r2=Radiobutton(root,text="no",variable=Q1_radioButton,value="no")
Q1_r2.pack()

Q2_radioButton=StringVar(value="0")


q2 = Label(root,text="Not sleepy?")
q2.pack()

Q2_r1=Radiobutton(root,text="yes",variable=Q2_radioButton,value="yes")
Q2_r1.pack()


Q2_r2=Radiobutton(root,text="no",variable=Q2_radioButton,value="no")
Q2_r2.pack()

Q3_radioButton=StringVar(value="0")


q3= Label(root,text="Are your ears bleeding?")
q3.pack()

Q3_r1=Radiobutton(root,text="yes",variable=Q3_radioButton,value="yes")
Q3_r1.pack()


Q3_r2=Radiobutton(root,text="no",variable=Q3_radioButton,value="no")
Q3_r2.pack()



def fever_score():
    score=0
    if Q1_radioButton.get()=="yes":
        score=score+20
        print(score)
        
    if  Q2_radioButton.get()=="yes":
        score=score+20
        print(score)
        
    if  Q3_radioButton.get()=="yes":
        score=score+20
        print(score)
          
    if score <=20:
        messagebox.showinfo("Report","You don't need to visit the doctor")
        
    elif score >20 and score <=40:
        messagebox.showinfo("Report","You might perphap's have to visit the doctor")
        
    else :
        messagebox.showinfo("Report","I strongly advise to visit the consultant")
        

btn= Button(root,text="click me",command=fever_score)
btn.pack()

root.mainloop()        
        