import mysql.connector


class DbConnection:
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='password',
        database='shoppy'
    )
    mycursor = db.cursor()

    # def insertData(self):
    #     self.name = input("Enter UserName")
    #     self.email = input("Enter Email")
    #     self.password = input("Enter Password")
    #     self.sql = "INSERT INTO user (userName,email,password) VALUES (%s,%s,%s)"
    #     self.val = (self.name, self.email, self.password)
    #     dbConn = DbConnection()
    #     dbConn.mycursor.execute(self.sql, self.val)
    #     dbConn.db.commit()

    def registerUser(self, fName, lName, emailAddress, phoneNo, password):
        import hashlib
        self.sql = "INSERT INTO requestedUser(fName,lName,email,phoneNo,password) VALUES (%s,%s,%s,%s,%s)"
        self.hashedPassword = (hashlib.md5(password.encode()).hexdigest())
        self.value = (fName, lName, emailAddress, phoneNo, self.hashedPassword)
        dbConn = DbConnection()
        dbConn.mycursor.execute(self.sql, self.value)
        dbConn.db.commit()

    def userLogin(self, email):
        self.sql = "SELECT email,password from requestedUser where email = %s"
        self.value = (email,)
        dbConn = DbConnection()
        dbConn.mycursor.execute(self.sql, self.value)
        self.result = dbConn.mycursor.fetchall()
        return self.result

    def addToCart(self, userEmail, productname, quantity):
        self.sql = "Insert into cartList values(%s,%s,%s)"
        self.value = (userEmail, productname, quantity)
        dbConn = DbConnection()
        dbConn.mycursor.execute(self.sql, self.value)
        dbConn.db.commit()

    def getProductDetails(self, email):
        self.sql = "SELECT productName,qty from cartList where userEmail = %s"
        self.value = (email,)
        dbConn = DbConnection()
        dbConn.mycursor.execute(self.sql, self.value)
        self.result = dbConn.mycursor.fetchall()
        return self.result
