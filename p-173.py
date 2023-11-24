from tkinter import *
root = Tk()
root.title("P-173")
root.geometry("600x600")





btn1 = Button(root, text = 'Show the Hospital Allotted', bd = '5') 

btn1.place(x=32,y=38)
lbl1 = Label(root,text="")
lbl1.place(x=32,y=100)

btn2 = Button(root, text = 'Show the IT Company Allotted', bd = '5') 

btn2.place(x=32, y=230)
lbl2 = Label(root,text="")
lbl2.place(x=32,y=300)


btn3 = Button(root, text = 'Show the Chemical Company Allotted', bd = '5') 

btn3.place(x=32, y=420)
lbl3 = Label(root,text="")
lbl3.place(x=32,y=500)



def on_button_clicked(btn1):
    if btn1 == "clicked":
        lbl1.config(text="Michael has been alloted to Galaxy")
       


def on_button_clicked(btn2):
   if btn2 == "clicked":
      lbl2.config(text="Jessica has been alloted to I Code")



def on_button_clicked(btn3):
    if btn3 == "clicked":
       lbl3.config(text="Peter has been alloted to DuPoint")




root.mainloop()