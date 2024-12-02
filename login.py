from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk     #pip install pillow
from tkinter import messagebox
from hotel import HotelManagementSystem

import mysql.connector;

def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        # bg image
        self.bg=ImageTk.PhotoImage(file=r"images\Taj.jpg")
        
        self.bg = Image.open(r"images\Taj.jpg")
        self.bg = self.bg.resize((1550, 800),Image.Resampling.LANCZOS)  # Resize the image to match the window size
        self.bg = ImageTk.PhotoImage(self.bg)  # Convert the resized image to Tkinter-compatible format

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
         
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"images\login.png")
        img1=img1.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #label
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15))
        self.txtpass.place(x=40,y=250,width=270)

        #====================Icons=========================
        img2=Image.open(r"images\login.png")
        img2=img2.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=650,y=323,width=25,height=25)

        img3=Image.open(r"images\password.png")
        img3=img3.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=650,y=390,width=25,height=25)

        #====================Login Button=========================
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,bg="red",fg="white",cursor="hand2",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #registerButton
        registerbtn=Button(frame,text="New user register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,bg="black",fg="white",cursor="hand2",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)

        #Forgetpassword
        passwordbtn=Button(frame,text="Forget password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,bg="black",fg="white",cursor="hand2",activeforeground="white",activebackground="black")
        passwordbtn.place(x=10,y=370,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.txtuser.get()=="abhishek" and self.txtpass.get()=="12345":
            messagebox.showinfo("Successfull",f"Welcome {self.txtuser.get()}",parent=self.root)
        else:
            conn=mysql.connector.connect(host='localhost',password='Abhi@231210003',user='root',database='management')
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(self.txtuser.get(),self.txtpass.get()))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showinfo("error","Invalid Username & Password")
            else:
                open_main=messagebox.askyesno("YesNo","Go To Main Page")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=HotelManagementSystem(self.new_window)   #project insertion
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    #reset password
    def reset_password(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","select the security question",parent=self.root2)
        elif self.txt_security_A.get()=="":
            messagebox.showerror("Error","enter the security answer",parent=self.root2)
        elif self.txt_new_password.get()=="":
            messagebox.showerror("Error","Enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host='localhost',password='Abhi@231210003',user='root',database='management')
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security_A.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct security question/answer",parent=self.root2)
            else:
                my_cursor.execute("update register set password=%s where email=%s",(self.txt_new_password.get(),self.txtuser.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Your password has been reset, please login with new password",parent=self.root2)
                self.root2.destroy()
                

                
                                         

    #forgot password
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email to reset your password")
        else:
            conn=mysql.connector.connect(host='localhost',password='Abhi@231210003',user='root',database='management')
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)
            if row==None:
                messagebox.showerror("Error","Please enter valid email")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",13),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Best Friend","Your Pet Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)

                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security_A=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security_A.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)

                self.txt_new_password=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_new_password.place(x=50,y=250,width=250)

                btn=Button(self.root2,command=self.reset_password,text="Reset",font=("times new roman",15,"bold"),bg="green",fg="white")
                btn.place(x=100,y=290)

                





class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        #==========================variables=========================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_password=StringVar()
        self.var_cpassword=StringVar()


        # bg image
        self.bg=ImageTk.PhotoImage(file=r"images\Taj.jpg")
        self.bg = Image.open(r"images\Taj.jpg")
        self.bg = self.bg.resize((1550, 900),Image.Resampling.LANCZOS)  # Resize the image to match the window size
        self.bg = ImageTk.PhotoImage(self.bg)  # Convert the resized image to Tkinter-compatible format
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        # left image
        self.bgl=ImageTk.PhotoImage(file=r"images\left.jpg")
        self.bgl = Image.open(r"images\left.jpg")
        self.bgl = self.bgl.resize((470, 550),Image.Resampling.LANCZOS)  # Resize the image to match the window size
        self.bgl = ImageTk.PhotoImage(self.bgl)  # Convert the resized image to Tkinter-compatible format
        bg_lbl=Label(self.root,image=self.bgl)
        left_lbl=Label(self.root,image=self.bgl)
        left_lbl.place(x=50,y=100,width=470,height=550)

        # main frame
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        # label and entry
        #row1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        lname.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        #row2
        contact=Label(frame,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

        #row3
        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",13),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Best Friend","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security_A=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security_A.place(x=370,y=270,width=250)


        #row4
        password=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        password.place(x=50,y=310)

        self.txt_password=ttk.Entry(frame,textvariable=self.var_password,font=("times new roman",15))
        self.txt_password.place(x=50,y=340,width=250)

        cpassword=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        cpassword.place(x=370,y=310)

        self.txt_cpassword=ttk.Entry(frame,textvariable=self.var_cpassword,font=("times new roman",15))
        self.txt_cpassword.place(x=370,y=340,width=250)

        #check button
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman",13,"bold"),bg="white",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        #buttons
        img=Image.open(r"images\register.png")
        img=img.resize((200,55),Image.Resampling.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,font=("times new roman",15,"bold"),cursor="hand2")
        b1.place(x=10,y=420,width=200)

        img1=Image.open(r"images\login_button2.png")
        img1=img1.resize((200,45),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,font=("times new roman",15,"bold"),cursor="hand2")
        b1.place(x=330,y=420,width=200)

    #=========================== function decleration=========================
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_password.get()!=self.var_cpassword.get():
            messagebox.showerror("Error","Password & Confirm Password should be same",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree our Terms & Conditions",parent=self.root)
        else:
            #messagebox.showinfo("Success","Register Successful",parent=self.root)
            conn=mysql.connector.connect(host='localhost',password='Abhi@231210003',user='root',database='management')
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exists, please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_password.get()
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successful")

    def return_login(self):
        self.root.destroy()



if __name__ == "__main__":
    main()