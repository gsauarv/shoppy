from tkinter import *
root = Tk()
root.title("Shoppy")
root.geometry("400x300")


class Gui:
    def __init__(self, master):
        myFrame = Frame(master)
        self.myLabel = Label(master, text="Email", pady=10, padx=10)
        self.email = Entry(master)
        self.myLabel1 = Label(master, text="Password",
                              pady=10, padx=10)
        self.password = Entry(master, show="*")
        self.loginBtn = Button(master, text="Login",
                               command=self.clicker, width=15, height=1, cursor="hand2")
        self.signupBtn = Button(master, text="SignUp",
                                width=15, height=1, cursor="hand2", command=self.newWindow)

        self.label3 = Label(master, text="Or Register your Account")
        self.myLabel.grid(row=3, column=2, sticky=W)
        self.email.grid(row=3, column=3, ipadx=25, ipady=5, padx=5)
        self.myLabel1.grid(row=4, column=2, sticky=W)
        self.password.grid(row=4, column=3, ipadx=25, ipady=5, padx=5)
        self.loginBtn.grid(row=6, column=3, pady=10)
        self.label3.grid(row=7, column=3)
        self.signupBtn.grid(row=8, column=3, pady=10)

    def clicker(self):
        from userLogin import loginUser
        import hashlib
        from db import DbConnection
        dbConn = DbConnection()
        login = loginUser()
        # tempEmail = self.email.get()
        # tempPassword = self.password.get()
        tempEmail = "vitabinary@gmail.com"
        tempPassword = "ISATPvLA"
        lists = dbConn.userLogin(email=tempEmail)
        dictDetails = dict(lists)
        userEmail = ""
        userPassword = ""
        for key in dictDetails:
            userEmail = key
            userPassword = dictDetails.get(key)

        if(userEmail == tempEmail and userPassword == (hashlib.md5(tempPassword.encode()).hexdigest())):
            self.userDashboard()
        else:
            print("SO")

    def newWindow(self):
        self.top = Toplevel()
        self.top.geometry("505x450")
        self.grettings = Label(self.top, text="Register Your Account")
        self.fname = Label(self.top, text="Enter FirstName")
        self.lname = Label(self.top, text="Enter LastName")
        self.emailAdd = Label(self.top, text="Enter Email")
        self.phoneNo = Label(self.top, text="Enter Phone No")

        self.fnameEntry = Entry(self.top)
        self.lnameEntry = Entry(self.top)
        self.emailAddEntry = Entry(self.top)
        self.phoneNoEntry = Entry(self.top)
        self.submitBtn = Button(self.top, text="SignUp",
                                cursor="hand2", width=15, height=1, command=self.getTopData)
        self.grettings.grid(row=0, column=0)
        self.fname.grid(row=1, column=0, sticky=W)
        self.fnameEntry.grid(row=1, column=1, ipadx=25,
                             ipady=5, padx=10, pady=10)
        self.lname.grid(row=2, column=0, sticky=W)
        self.lnameEntry.grid(row=2, column=1, ipadx=25,
                             ipady=5, padx=10, pady=10)
        self.emailAdd.grid(row=3, column=0, sticky=W)
        self.emailAddEntry.grid(row=3, column=1, ipadx=25,
                                ipady=5, padx=10, pady=10)
        self.phoneNo.grid(row=4, column=0, sticky=W)
        self.phoneNoEntry.grid(row=4, column=1, ipadx=25,
                               ipady=5, padx=10, pady=10)
        self.submitBtn.grid(row=5, column=1)

    def getTopData(self):
        namefirst = self.fnameEntry.get()
        nameLast = self.lnameEntry.get()
        addEmail = self.emailAddEntry.get()
        noPhone = self.phoneNoEntry.get()
        from userLogin import Userregister
        userLog = Userregister()
        a = userLog.generatePassword()
        from db import DbConnection
        db = DbConnection()
        db.registerUser(namefirst, nameLast, addEmail, noPhone, a)
        userLog.mailAddress = addEmail
        userLog.sendUserDetails()
        alertLabel = Label(
            self.top, text="Register SuccessFull Check Your Email To Login")
        alertLabel.grid(row=7, column=1, pady=10)
        backButton = Button(
            self.top, text="Login", command=self.quit, cursor="hand2", width=15, height=1)
        backButton.grid(row=8, column=1)

    def quit(self):
        self.top.destroy()

    def userDashboard(self):
        self.dashboard = Toplevel()
        self.dashboard.geometry("1920x1080")
        self.userLogo = Label(
            self.dashboard, text="Shoppy", font=("Helvetica", 14))
        self.userLogo.grid(row=0, column=0, padx=20, pady=20, sticky=W)
        self.userButton = Button(
            self.dashboard, text="Profile", font=("Helvetica", 12), cursor="hand2")
        self.userButton.grid(row=0, column=3)

        self.dashGreetings = Label(
            self.dashboard, text="Welcome To Shoppy,Choose the Categories For Shopping.", font=("Helvetica", 12))
        self.dashGreetings.grid(row=2, column=0, sticky=W, padx=20, pady=40)

        self.shopBtn = Button(
            self.dashboard, text="Groceries", width=20, height=5, font=("Helvetica", 12), bg='#032535', fg='white', cursor="hand2")
        self.shopBtn1 = Button(
            self.dashboard, text="Vegetables", width=20, height=5, font=("Helvetica", 12), bg='#004A2F', fg='white', cursor="hand2")
        self.shopBtn2 = Button(
            self.dashboard, text="Chocolates", width=20, height=5, font=("Helvetica", 12), bg='#8C5E58', fg='white', cursor="hand2")
        self.shopBtn3 = Button(
            self.dashboard, text="Dairy", width=20, height=5, font=("Helvetica", 12), bg='#0E2431', fg='white', cursor="hand2")

        self.shopBtn.grid(row=3, column=0, padx=100, pady=150, sticky=W)
        self.shopBtn1.grid(row=3, column=1, padx=30)
        self.shopBtn2.grid(row=3, column=2, padx=50)
        self.shopBtn3.grid(row=3, column=3, padx=50)


e = Gui(root)
root.mainloop()
