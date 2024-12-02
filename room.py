from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime

class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management Syatem")
        self.root.geometry("1295x550+230+220")

        #variables
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailabe = StringVar()
        self.var_meal = StringVar()
        self.var_noofdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()


        #*************** title ***************
        lbl_title = Label(self.root, text="ROOM BOOKING DETAILS", font=("times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

         #*************** logo *************** 
        img2 = Image.open(r"images\logo.jpg")
        img2 = img2.resize((100, 40), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=40)

        #*******************label frame********************
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="ROOM BOOKING DETAILS", font=("times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)

        #*******************labels and entrye********************
        #customer contact
        lbl_cust_contact = Label(labelframeleft, text="Customer Contact", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0,sticky=W)

        enty_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact, font=("arial", 13, "bold"),width=20)
        enty_contact.grid(row=0, column=1,sticky=W)

        #fetch data button
        btnFetchdata= Button(labelframeleft,command=self.Fetch_contact, text="Fetch data", font=("arial", 8, "bold"), bg="black", fg="gold", width=8)
        btnFetchdata.place(x=340, y=4)

         #checkin date
        check_in_date = Label(labelframeleft, text="check_in date", font=("arial", 12, "bold"), padx=2, pady=6)
        check_in_date.grid(row=1, column=0,sticky=W)

        enty_check_in=ttk.Entry(labelframeleft,textvariable=self.var_checkin, font=("arial", 13, "bold"),width=29)
        enty_check_in.grid(row=1, column=1)

         #check_out date
        lbl_check_out = Label(labelframeleft, text="Check_Out Date", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_check_out.grid(row=2, column=0,sticky=W)
        lbl_check_out=ttk.Entry(labelframeleft,textvariable=self.var_checkout, font=("arial", 13, "bold"),width=29)
        lbl_check_out.grid(row=2, column=1)

        #Room Type
        label_RoomType = Label(labelframeleft, text="Room Type", font=("arial", 12, "bold"), padx=2, pady=6)
        label_RoomType.grid(row=3, column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",user="root",password="Abhi@231210003",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomType from details")
        ide=my_cursor.fetchall()

        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype, font=("arial", 13, "bold"),width=27, state="readonly")
        combo_RoomType["values"]=ide
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3, column=1)

        #Available rooms
        lblRoomAvailable = Label(labelframeleft, text="Available room", font=("arial", 12, "bold"), padx=2, pady=6)
        lblRoomAvailable.grid(row=4, column=0,sticky=W)

        # txtRoomAvailable=ttk.Entry(labelframeleft,textvariable=self.var_roomavailabe, font=("arial", 13, "bold"),width=29)
        # txtRoomAvailable.grid(row=4, column=1)
        conn=mysql.connector.connect(host="localhost",user="root",password="Abhi@231210003",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows=my_cursor.fetchall()
        combo_RoomNo=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailabe, font=("arial", 13, "bold"),width=27, state="readonly")
        combo_RoomNo["values"]=rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4, column=1)

        #Meal
        lblMeal = Label(labelframeleft, text="Meal", font=("arial", 12, "bold"), padx=2, pady=6)
        lblMeal.grid(row=5, column=0,sticky=W)
        txtMeal=ttk.Entry(labelframeleft,textvariable=self.var_meal, font=("arial", 13, "bold"),width=29)
        txtMeal.grid(row=5, column=1)

         #No of days
        lblNoOfDays = Label(labelframeleft, text="No. of Days::", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNoOfDays.grid(row=6, column=0,sticky=W)
        txtMeal=ttk.Entry(labelframeleft,textvariable=self.var_noofdays, font=("arial", 13, "bold"),width=29)
        txtMeal.grid(row=6, column=1)

         #paid tax
        lblpaidtax = Label(labelframeleft, text="paidTax:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblpaidtax.grid(row=7, column=0,sticky=W)
        txtpaidtax=ttk.Entry(labelframeleft,textvariable=self.var_paidtax, font=("arial", 13, "bold"),width=29)
        txtpaidtax.grid(row=7, column=1)

         #sub total
        lblsubtotal = Label(labelframeleft, text="sub Total", font=("arial", 12, "bold"), padx=2, pady=6)
        lblsubtotal.grid(row=8, column=0,sticky=W)
        txtsubtotal=ttk.Entry(labelframeleft,textvariable=self.var_actualtotal, font=("arial", 13, "bold"),width=29)
        txtsubtotal.grid(row=8, column=1)

        #Total cost
        lbltotal = Label(labelframeleft, text="Total Cost:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbltotal.grid(row=9, column=0,sticky=W)
        txttotal=ttk.Entry(labelframeleft,textvariable=self.var_total, font=("arial", 13, "bold"),width=29)
        txttotal.grid(row=9, column=1)

        #Bill Button
        btnBill = Button(labelframeleft,command=self.total, text="Bill",width=9, font=("arial", 12, "bold"), bg="black", fg="gold")
        btnBill.grid(row=10,sticky=W, column=0,padx=1)



        #buttons
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btn_frame,command=self.add_data, text="Add",width=9, font=("arial", 12, "bold"), bg="black", fg="gold")
        btnAdd.grid(row=0, column=0,padx=1)

        btnUpdate = Button(btn_frame,command=self.update, text="Update",width=9, font=("arial", 12, "bold"), bg="black", fg="gold")
        btnUpdate.grid(row=0, column=1,padx=1)

        btnDelete = Button(btn_frame,command=self.mDelete, text="Delete",width=9, font=("arial", 12, "bold"), bg="black", fg="gold")
        btnDelete.grid(row=0, column=2,padx=1)

        btnReset = Button(btn_frame,command=self.reset, text="Reset",width=9, font=("arial", 12, "bold"), bg="black", fg="gold")
        btnReset.grid(row=0, column=3,padx=1)

        # Right side image
        img3 = Image.open(r"images\bed.jpg")
        img3 = img3.resize((520, 200), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lblimg.place(x=760, y=55, width=520, height=200)

        #label frame search system
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and search system", font=("times new roman", 12, "bold"), padx=2)
        Table_Frame.place(x=435, y=280, width=860, height=260)

        lblSearchBy=Label(Table_Frame, text="Search By:", font=("arial", 12, "bold"),bg="red", fg="white")
        lblSearchBy.grid(row=0, column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["values"]=("select","Contact","ROOM")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search, font=("arial", 13, "bold"),width=24)
        txtSearch.grid(row=0, column=2,padx=2)

        btnSearch = Button(Table_Frame,command=self.search, text="Search",width=9, font=("arial", 12, "bold"), bg="black", fg="gold")
        btnSearch.grid(row=0, column=3,padx=1)

        btnShowAll = Button(Table_Frame,command=self.fetch_data, text="Show All",width=9, font=("arial", 12, "bold"), bg="black", fg="gold")
        btnShowAll.grid(row=0, column=4,padx=1)


        #show data table
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=180)

        scroll_x=Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=Scrollbar(details_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(details_table,columns=("contact","checkin","checkout","roomtype","roomavailabe","meal","noofdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("checkin",text="Checkin")
        self.room_table.heading("checkout",text="Checkout")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("roomavailabe",text="Room No")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noofdays",text="No of Days")

        self.room_table["show"]="headings"

        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailabe",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noofdays",width=100)

        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Abhi@231210003",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                        self.var_contact.get(),
                                                        self.var_checkin.get(),
                                                        self.var_checkout.get(),
                                                        self.var_roomtype.get(),
                                                        self.var_roomavailabe.get(),
                                                        self.var_meal.get(),
                                                        self.var_noofdays.get()
                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("succes","Room booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"something went wrong:{str(es)}",parent=self.root)



    #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Abhi@231210003",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for row in rows:
                self.room_table.insert("",END,values=row)
            conn.commit()
        conn.close()


    #get cursor
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailabe.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])

    #update fubction
    def update(self):
        if self.var_contact.get()=="" :
            messagebox.showerror("Error","please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Abhi@231210003",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,room=%s,meal=%s,noofdays=%s where contact=%s",(
                                                        self.var_checkin.get(),
                                                        self.var_checkout.get(),
                                                        self.var_roomtype.get(),
                                                        self.var_roomavailabe.get(),
                                                        self.var_meal.get(),
                                                        self.var_noofdays.get(),
                                                        self.var_contact.get(),
                                                        ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("update","room details has been updated successfully",parent=self.root)

    #delete function
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer?",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",user="root",password="Abhi@231210003",database="management")
            my_cursor=conn.cursor()
            query="delete from room where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        # self.var_roomtype.set("")
        self.var_roomavailabe.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")


    #all data fetch
    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Contact must be required")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Abhi@231210003", database="management")
            my_cursor = conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","No record found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe=Frame(self.root,bd=4,padx=2,relief=RIDGE)
                showDataframe.place(x=450,y=55,width=300,height=180)

                lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)

                #gender
                conn = mysql.connector.connect(host="localhost", user="root", password="Abhi@231210003", database="management")
                my_cursor = conn.cursor()
                query=("select gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=30)

                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=30)

                #email
                conn = mysql.connector.connect(host="localhost", user="root", password="Abhi@231210003", database="management")
                my_cursor = conn.cursor()
                query=("select email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                lblemail=Label(showDataframe,text="email:",font=("arial",12,"bold"))
                lblemail.place(x=0,y=60)

                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=60)

                #Nationality
                conn = mysql.connector.connect(host="localhost", user="root", password="Abhi@231210003", database="management")
                my_cursor = conn.cursor()
                query=("select Nationality from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                lblNationality=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"))
                lblNationality.place(x=0,y=90)

                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=90)

                #Address
                conn = mysql.connector.connect(host="localhost", user="root", password="Abhi@231210003", database="management")
                my_cursor = conn.cursor()
                query=("select Address from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                lblAddress=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
                lblAddress.place(x=0,y=120)

                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=120)

    #search system
    def search(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Abhi@231210003",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for row in rows:
                self.room_table.insert("",END,values=row)
            conn.commit()
        conn.close()


    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)

        if (self.var_meal.get()=="breakfast" and self.var_roomtype.get()=="single"):
            q1=float(300)
            q2=float(400)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str('%.2f'%((q5*0.1)))
            ST="Rs."+str('%.2f'%((q5)))
            TT="Rs."+str('%.2f'%((q5+(q5*0.1))))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(400)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str('%.2f'%((q5*0.1)))
            ST="Rs."+str('%.2f'%((q5)))
            TT="Rs."+str('%.2f'%((q5+(q5*0.1))))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Double"):
            q1=float(500)
            q2=float(300)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str('%.2f'%((q5*0.1)))
            ST="Rs."+str('%.2f'%((q5)))
            TT="Rs."+str('%.2f'%((q5+(q5*0.1))))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

                
       

        
        






if __name__ == "__main__":
    root = Tk()
    obj = Roombooking(root)
    root.mainloop()
