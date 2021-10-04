from tkinter import*
from PIL import ImageTk #install pillow first
from tkinter import messagebox

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

        lbl_user = Label(login_frame,text="Username",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=140)
        self.txt_user = Entry(login_frame,font=("times new roman",15),bg="lightgray")
        self.txt_user.place(x=90,y=170,width=350,height=35)

        lbl_pass = Label(login_frame,text="Password",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=210)
        self.txt_pass = Entry(login_frame,font=("times new roman",15),bg="lightgray")
        self.txt_pass.place(x=90,y=240,width=350,height=35)

        forget_btn = Button(login_frame,cursor="hand2",text="Forget Password?", bg="white",fg="red",bd=0,font=("times new roman",12)).place(x=90,y=280,height=30)

        login_btn = Button(login_frame,command=self.login_func,cursor="hand2",text="Login", bg="green",fg="white",font=("times new roman",20)).place(x=200,y=320,width=180,height=40)

    def login_func(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.txt_pass.get()!="123456" or self.txt_user.get()!="Pranesh":
            messagebox.showerror("Error","Invalid Username/Password",parent=self.root)
        else:
            messagebox.showinfo("Welcome",f"Welcome {self.txt_user.get()}\nYour Password: {self.txt_pass.get()}",parent=self.root)



root = Tk()
obj = login(root)
root.mainloop()