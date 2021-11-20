from tkinter import *
from tkinter import messagebox
import sqlite3

class Bank:
    def __init__(self,w):
        self.conn = sqlite3.connect("atm_databse.db")
        self.login = False
        self.w = w
        self.header = Label(self.w,text=" !!.... WELCOME TO OUR  ATM SERVICES ....!! ",bg="salmon",fg="white",font="arial 18 bold")
        self.header.pack(fill=X)
        self.l1 =Label(self.w,text="Enter Account No:-",font={"arial" ,"bold"},bg="purple4",fg="white")
        self.l1.place(x=100,y=100,width=180,height=40)
        self.e1 = Entry(self.w,bd=10)
        self.e1.place(x=300,y=100)
        self.l2 = Label(self.w,text="Enter Pin:-",font={"arial" ,"bold"},bg="purple4",fg="white")
        self.l2.place(x=100,y=160,width=180,height=40)
        self.e2 = Entry(self.w,show="*",bd=10)
        self.e2.place(x=300,y=160)
        self.b1 = Button(self.w,text="  Ok  ",bg="midnight blue",fg="white",bd=7,font="arial 10 bold",command=self.verify)
        self.b1.place(x=360,y=230)
        self.b2 = Button(self.w,text=" Cancel ",bg="midnight blue",fg="white",bd=7,font="arial 10 bold",command = self.w.destroy)        
        self.b2.place(x=450,y=230)
    def database_fetch(self):
        self.acc_list = []
        self.temp = self.conn.execute("select name,pass,acc_no,acc_type,bal from atm where acc_no = ? ",(self.ac,))
        for i in self.temp:
            self.acc_list.append("Name = {}".format(i[0]))
            self.acc_list.append("Account no = {}".format(i[2]))
            self.acc_list.append("Account type = {}".format(i[3]))
            self.ac = i[2]
            self.acc_list.append("Balance = {}".format(i[4]))

    def verify(self):
        ac = False
        self.temp = self.conn.execute("select name,pass,acc_no,acc_type,bal from atm where acc_no = ? ", (self.e1.get()),)
        for i in self.temp:
            self.ac = i[2]
            if i[2] == self.e1.get():
                ac = True
            elif i[1] == self.e2.get():
                ac = True
                m = "{} Login SucessFull".format(i[0])
                self.database_fetch()
                messagebox._show("Login Info", m)
                self.w.destroy()
                self.MainMenu()
            else:
                ac = True
                m = " Login UnSucessFull ! Wrong Password"
                messagebox._show("Login Info!", m)
        if not ac:
            m = " Wrong Acoount Number !"
            messagebox._show("Login Info!", m)


    def MainMenu(self):
        root=Tk()
        self.root = root
        self.root.geometry("1250x600")
        self.root.configure(background="slate grey")
        self.l1=Label(self.root,text="!!.... WELCOME IN ATM SERVICES ....!!",font="arial 18 bold",bg="salmon",fg="white")
        self.l1.pack(fill=X)
        self.b1=Button(self.root,text="  Account Details  ",font={"arial",20},bd=20,bg="midnight blue",fg="white",command=self.account_detail)
        self.b1.place(x=1000,y=400,width=250,height=80)
        self.b2=Button(self.root,text="Balance Inquiry ",font={"arial",20},bd=20,bg="midnight blue",fg="white",command=self.Balance)
        self.b2.place(x=1000,y=260,width=250,height=80)
        self.b3=Button(self.root,text="    Pin Change     ",font={"arial",30},bd=20,bg="midnight blue",fg="white",command=self.pin_change)
        self.b3.place(x=1000,y=120,width=250,height=80)
        self.b4=Button(self.root,text="    Deposit Cash    ",font={"arial",30},bd=20,bg="midnight blue",fg="white",command=self.deposit_money)
        self.b4.place(x=0,y=120,width=250,height=80)
        self.b=Button(self.root,text="   Withdrawl Cash   ",font={"arial",20},bd=20,bg="midnight blue",fg="white",command=self.withdrawl_money)
        self.b.place(x=0,y=260,width=250,height=80)
        self.q = Button(self.root, text="Quit",font={"arial",10} ,bd=10,bg="midnight blue",fg="white", command=self.root.destroy)
        self.q.place(x=580, y=520, width=100, height=40)
        self.root=mainloop()

    def account_detail(self):
        self.database_fetch()
        text = self.acc_list[0]+"\n"+self.acc_list[1]+"\n"+self.acc_list[2]
        self.label = Label(self.root,text=text,font="arial 10 bold")
        self.label.place(x=520, y=400, width=250, height=80)

    def Balance(self):
        self.database_fetch()
        self.label = Label(self.root, text=self.acc_list[3],font="arial 10 bold")
        self.label.place(x=520, y=400, width=250, height=80)

    def deposit_money(self):
        self.money_box = Entry(self.root,bg="honeydew",highlightcolor="white",highlightthickness=2,highlightbackground="white")
        self.money_box.place(x=500,y=200,width=150,height=25)
        self.submitButton = Button(self.root,text="Submit",bg="salmon",fg="white",font="arial 10 bold")
        self.submitButton.place(x=650,y=200,width=60,height=25)
        self.submitButton.bind("<Button-1>",self.deposit_trans)

    def deposit_trans(self,flag):
        self.label = Label(self.root, text="Transaction Completed !", font="arial 10 bold")
        self.label.place(x=520, y=400, width=250, height=80)
        self.conn.execute("update atm set bal = bal + ? where acc_no = ?",(self.money_box.get(),self.ac))
        self.conn.commit()

    def withdrawl_money(self):
        self.money_box = Entry(self.root,bg="honeydew",highlightcolor="white",highlightthickness=2,highlightbackground="white")
        self.submitButton = Button(self.root,text="Submit",bg="salmon",fg="white",font="arial 10 bold")
        self.money_box.place(x=500,y=200,width=150,height=25)
        self.submitButton.place(x=650,y=200,width=60,height=25)
        self.submitButton.bind("<Button-1>",self.withdrawl_trans)

    def withdrawl_trans(self,flag):
        self.label = Label(self.root, text="Money Withdrawl !", font="arial 10 bold")
        self.label.place(x=520, y=400, width=250, height=80)
        self.conn.execute("update atm set bal = bal - ? where acc_no = ?",(self.money_box.get(),self.ac))
        self.conn.commit()
    def pin_change(self):
        self.pin_box = Entry(self.root,bg="honeydew",highlightcolor="white",highlightthickness=2,highlightbackground="white")
        self.submitButton = Button(self.root,text="Submit",bg="salmon",fg="white",font="arial 10 bold")
        self.pin_box.place(x=500,y=200,width=150,height=25)
        self.submitButton.place(x=650,y=200,width=60,height=25)
        self.submitButton.bind("<Button-1>",self.pin_trans)

    def pin_trans(self,flag):
        self.label = Label(self.root, text="Successfully Updated!  !",font="arial 10 bold")
        self.label.place(x=520, y=400, width=250, height=80)
        self.conn.execute("update atm set pass = ? where acc_no = ?",(self.pin_box.get(),self.ac))
        self.conn.commit()

w = Tk()
w.title("Sign In")
w.geometry("1050x500")
w.configure(background="grey")
obj = Bank(w)
w.mainloop()


