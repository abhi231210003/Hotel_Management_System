from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime

class DetailsRoom:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management Syatem")
        self.root.geometry("1295x550+230+220")


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
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="NEW ROOM ADD", font=("times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=540, height=350)

         #Floor
        lbl_floor = Label(labelframeleft, text="Floor", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_floor.grid(row=0, column=0,sticky=W,padx=20)
        self.var_floor=StringVar()

        enty_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor, font=("arial", 13, "bold"),width=20)
        enty_floor.grid(row=0, column=1,sticky=W)

        #Room No
        lbl_room_no = Label(labelframeleft, text="Room No", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_room_no.grid(row=1, column=0,sticky=W,padx=20)
        self.var_RoomNo=StringVar()

        enty_room_no=ttk.Entry(labelframeleft,textvariable=self.var_RoomNo, font=("arial", 13, "bold"),width=20)
        enty_room_no.grid(row=1, column=1,sticky=W)

        #Room Type
        lbl_room_type = Label(labelframeleft, text="Room Type", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_room_type.grid(row=2, column=0,sticky=W,padx=20)
        self.var_RoomType=StringVar()

        enty_room_type=ttk.Entry(labelframeleft,textvariable=self.var_RoomType, font=("arial", 13, "bold"),width=20)
        enty_room_type.grid(row=2, column=1,sticky=W)

        #buttons
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=200, width=412, height=40)

        btnAdd = Button(btn_frame,command=self.add_data, text="Add",width=9, font=("arial", 12, "bold"), bg="black", fg="gold")
        btnAdd.grid(row=0, column=0,padx=1)

        btnUpdate = Button(btn_frame,command=self.update, text="Update",width=9, font=("arial", 12, "bold"), bg="black", fg="gold")
        btnUpdate.grid(row=0, column=1,padx=1)

        btnDelete = Button(btn_frame,command=self.mDelete, text="Delete",width=9, font=("arial", 12, "bold"), bg="black", fg="gold")
        btnDelete.grid(row=0, column=2,padx=1)

        btnReset = Button(btn_frame, text="Reset",command=self.reset,width=9, font=("arial", 12, "bold"), bg="black", fg="gold")
        btnReset.grid(row=0, column=3,padx=1)

        #label frame search system
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="show room details", font=("times new roman", 12, "bold"), padx=2)
        Table_Frame.place(x=600, y=55, width=600, height=350)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)

        self.room_table=ttk.Treeview(Table_Frame,columns=("floor","roomno","roomtype"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor",text="Floor")
        self.room_table.heading("roomno",text="Room no")
        self.room_table.heading("roomtype",text="Room type")

        self.room_table["show"]="headings"

        self.room_table.column("floor",width=100)
        self.room_table.column("roomno",width=100)
        self.room_table.column("roomtype",width=100)

        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_floor.get()=="" or self.var_RoomType.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Abhi@231210003",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                            self.var_floor.get(),
                                                            self.var_RoomNo.get(),
                                                            self.var_RoomType.get()
                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("succes","Room Added successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"something went wrong:{str(es)}",parent=self.root)

     #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Abhi@231210003",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
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

        self.var_floor.set(row[0])
        self.var_RoomNo.set(row[1])
        self.var_RoomType.set(row[2])

    #update fubction
    def update(self):
        if self.var_floor.get()=="" :
            messagebox.showerror("Error","please enter floor number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Abhi@231210003",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set Floor=%s,RoomType=%s where RoomNo=%s",(self.var_floor.get(),self.var_RoomType.get(),self.var_RoomNo.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("update","room details has been updated successfully",parent=self.root)


    #delete function
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this room?",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",user="root",password="Abhi@231210003",database="management")
            my_cursor=conn.cursor()
            query="delete from details where RoomNo=%s"
            value=(self.var_RoomNo.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_floor.set("")
        self.var_RoomNo.set("")
        # self.var_RoomType.set("")
    

    




       








if __name__ == "__main__":
    root = Tk()
    obj =DetailsRoom(root)
    root.mainloop()
