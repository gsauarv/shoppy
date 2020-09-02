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

    def registerUser(self, fName, lName, emailAddress, phoneNo):
        self.sql = "INSERT INTO requestedUser(fName,lName,email,phoneNo) VALUES (%s,%s,%s,%s)"
        self.value = (fName, lName, emailAddress, phoneNo)
        dbConn = DbConnection()
        dbConn.mycursor.execute(self.sql, self.value)
        dbConn.db.commit()
