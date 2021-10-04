from tkinter import*
from PIL import ImageTk #install pillow first

class login:
    def __init__(self,root):
        self.root = root
        self.root.title("Login System to practice Git")
        self.root.geometry("1200x650+100+50")

        #Image background
        self.bg = ImageTk.PhotoImage(file="tcs_pic.jpg")
        self.bg_image = Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #Login frame
        login_frame = Frame(self.root,bg="white")
        login_frame.place(x=100,y=200,height=400,width=550)

        title = Label(login_frame,text="Login Here",font=("Impact",35,"bold"),fg="blue",bg="white").place(x=90,y=30)
        about = Label(login_frame,text="Employee Login Area",font=("Goudy old style",15,"bold"),fg="green",bg="white").place(x=90,y=100)


root = Tk()
obj = login(root)
root.mainloop()