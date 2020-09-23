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
            self.dashboard, text="Groceries", width=20, height=5, font=("Helvetica", 12), bg='#032535', fg='white', cursor="hand2", command=self.Groceries)
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

    def Groceries(self):
        from PIL import Image, ImageTk
        self.groList = Toplevel()
        self.groList.geometry("1920x1080")
        self.listLabel = Label(
            self.groList, text="Groceries", font=("Helvetica", 12), pady=20, padx=20)
        self.listLabel.grid(row=0, column=0)

        self.path = "/home/sg/pythonProject/rice.png"
        self.rice = Image.open(self.path)
        self.resized_rice = self.rice.resize((250, 250), Image.ANTIALIAS)
        self.new_rice = ImageTk.PhotoImage(self.resized_rice)
        self.mylabel = Label(self.groList, image=self.new_rice)
        self.mylabel.grid(row=1, column=1)

        self.groRice = Label(
            self.groList, text="Product:Rice", padx=20, pady=20, font=("Helvetica", 18))
        self.groRice.grid(row=2, column=1)
        self.ricePrice = Label(
            self.groList, text="Price : $23", font=("Helvetica", 15))
        self.ricePrice.grid(row=3, column=1)
        self.label = Label(
            self.groList, text="Enter Quantity", font=("Helvetica", 12))
        self.riceQty = Entry(self.groList)
        self.label.grid(row=4, column=1)
        self.riceQty.grid(row=5, column=1)
        self.riceBtn = Button(
            self.groList, text="Add To Cart", width=17, height=2, cursor='hand2', command=self.btn1)
        self.riceBtn.grid(row=6, column=1)

        self.path1 = "/home/sg/pythonProject/tea.png"
        self.tea = Image.open(self.path1)
        self.resized_tea = self.tea.resize((250, 250), Image.ANTIALIAS)
        self.new_tea = ImageTk.PhotoImage(self.resized_tea)
        self.mylabel1 = Label(self.groList, image=self.new_tea)
        self.mylabel1.grid(row=1, column=2)

        self.groTea = Label(
            self.groList, text="Product:Tea", padx=20, pady=20, font=("Helvetica", 18))
        self.groTea.grid(row=2, column=2)
        self.teaPrice = Label(
            self.groList, text="Price : $23", font=("Helvetica", 15))
        self.teaPrice.grid(row=3, column=2)
        self.tealabels = Label(
            self.groList, text="Enter Quantity", font=("Helvetica", 12))
        self.teaQty = Entry(self.groList)
        self.tealabels.grid(row=4, column=2)
        self.teaQty.grid(row=5, column=2)
        self.teaBtn = Button(
            self.groList, text="Add To Cart", width=17, height=2, cursor='hand2', command=self.btn2)
        self.teaBtn.grid(row=6, column=2)

        self.path3 = "/home/sg/pythonProject/coffee.png"
        self.coffee = Image.open(self.path3)
        self.resized_coffee = self.coffee.resize((250, 250), Image.ANTIALIAS)
        self.new_coffee = ImageTk.PhotoImage(self.resized_coffee)
        self.mylabel3 = Label(self.groList, image=self.new_coffee)
        self.mylabel3.grid(row=1, column=3)

        self.groCoffee = Label(
            self.groList, text="Product:Coffee", padx=20, pady=20, font=("Helvetica", 18))
        self.groCoffee.grid(row=2, column=3)
        self.coffeePrice = Label(
            self.groList, text="Price : $23", font=("Helvetica", 15))
        self.coffeePrice.grid(row=3, column=3)
        self.coffeeLabel = Label(
            self.groList, text="Enter Quantity", font=("Helvetica", 12))
        self.coffeeQty = Entry(self.groList)
        self.coffeeLabel.grid(row=4, column=3)
        self.coffeeQty.grid(row=5, column=3)
        self.coffeeBtn = Button(
            self.groList, text="Add To Cart", width=17, height=2, cursor='hand2', command=self.btn3)
        self.coffeeBtn.grid(row=6, column=3)

        self.path4 = "/home/sg/pythonProject/beans.png"
        self.beans = Image.open(self.path4)
        self.resized_beans = self.beans.resize((250, 250), Image.ANTIALIAS)
        self.new_beans = ImageTk.PhotoImage(self.resized_beans)
        self.mylabel4 = Label(self.groList, image=self.new_beans)
        self.mylabel4.grid(row=1, column=4)

        self.groBeans = Label(
            self.groList, text="Product:Beans", padx=20, pady=20, font=("Helvetica", 18))
        self.groBeans.grid(row=2, column=4)
        self.beansPrice = Label(
            self.groList, text="Price : $23", font=("Helvetica", 15))
        self.beansPrice.grid(row=3, column=4)
        self.beansLabel = Label(
            self.groList, text="Enter Quantity", font=("Helvetica", 12))
        self.beansQty = Entry(self.groList)
        self.beansLabel.grid(row=4, column=4)
        self.beansQty.grid(row=5, column=4)
        self.beansBtn = Button(
            self.groList, text="Add To Cart", width=17, height=2, cursor='hand2', command=self.btn4)
        self.beansBtn.grid(row=6, column=4)

        self.addToCart = Button(
            self.groList, text="View Order", width=70, height=2, bg='#032535', fg='white', cursor='hand2', command=self.viewOrder)
        self.addToCart.place(x=400, y=600)

    def btn1(self):
        from addtocart import addtoCart
        self.productName = "Rice"
        self.productQty = self.riceQty.get()
        addtocart = addtoCart(
            self.email.get(), self.productName, self.productQty)

    def btn2(self):
        from addtocart import addtoCart
        self.productName = "Tea"
        self.productQty = self.teaQty.get()
        addtocart = addtoCart(
            self.email.get(), self.productName, self.productQty)

    def btn3(self):
        from addtocart import addtoCart
        self.productName = "Coffee"
        self.productQty = self.coffeeQty.get()
        addtocart = addtoCart(
            self.email.get(), self.productName, self.productQty)

    def btn4(self):
        from addtocart import addtoCart
        self.productName = "Beans"
        self.productQty = self.beansQty.get()
        addtocart = addtoCart(
            self.email.get(), self.productName, self.productQty)

    def viewOrder(self):
        self.groList.destroy()
        self.orderPage = Toplevel()
        self.orderPage.geometry("500x500")
        from addtocart import getProduct
        productDet = getProduct()
        self.productDetails = productDet.productDetails(email=self.email.get())
        self.label = Label(self.orderPage, text="Products",
                           font=("Helvetica", 12))
        self.label.grid(row=0, column=1, sticky=W)

        self.Quantity = Label(self.orderPage, text="Quantity",
                              font=("Helvetica", 12))
        self.Quantity.place(x=250, y=0)
        i = 1
        for key in self.productDetails:
            productName = key
            productQty = self.productDetails.get(key)
            self.orderProduct = Label(self.orderPage, text=productName)
            self.orderProduct.grid(row=i, column=1, sticky=W)
            self.orderQty = Label(self.orderPage, text=productQty)
            self.orderQty.grid(row=i, column=2, sticky=E, padx=120)
            i += 1

        self.label2 = Label(self.orderPage, text="Confirm  Your Purchase")
        self.label2.grid(row=i+1, column=1, ipady=20)

        self.confirmBtn = Button(
            self.orderPage, text="Confirm Order", cursor='hand2')
        self.confirmBtn.grid(row=i+2, column=1, columnspan=2)


e = Gui(root)
root.mainloop()
