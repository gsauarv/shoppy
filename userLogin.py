import smtplib


class Userregister:
    def __init__(self):
        self.firstName = "firstName"
        self.lastName = "lastName"
        self.mailAddress = 'mailAddress'
        self.phoneNo = 'phone'
        # self.firstName, self.lastName, self.mailAddress, self.phoneNo = gui.getTopData()

    def getDetails(self):
        return (self.firstName + "\n" + self.lastName + "\n" + self.mailAddress + "\n" + self.phoneNo)

    def registerUser(self):
        return self.firstName, self.lastName, self.mailAddress, self.phoneNo

    def generatePassword(self):
        import random
        import string
        self.temppassword = []
        for i in range(0, 8):
            self.temp = random.choice(string.ascii_letters)
            self.temppassword.append(self.temp)

        self.generatedPassword = "".join(self.temppassword)

        return self.generatedPassword

    def sendUserDetails(self):
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        self.senderEmail = "gsaurav2000@gmail.com"
        self.senderEmailPassword = "ttrsfkhuayyhzjfn"
        self.subject = "Shoppy | Login Details"
        self.msg = MIMEMultipart()
        self.msg["From"] = self.senderEmail
        self.msg["To"] = self.mailAddress
        self.msg["Subject"] = self.subject
        self.message = MIMEText("Hey Welcome To Our Shop Please Use This User credentials to Start Your Journey in Shoopy. \n " +
                                "UserName: " + self.mailAddress + "\n" + "Password: " + self.generatedPassword)

        self.msg.attach(self.message)

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.senderEmail, self.senderEmailPassword)
            server.sendmail(self.senderEmail,
                            self.mailAddress, self.msg.as_string())
            server.quit()

        except:
            print("SomeThing Went Wrong")


class loginUser:
    from db import DbConnection
    dbConn = DbConnection()
    import hashlib
    tempEmail = ""
    tempPassword = ""
    lists = dbConn.userLogin(email=tempEmail)
    dictDetails = dict(lists)
    userEmail = ""
    userPassword = ""
    for key in dictDetails:
        userEmail = key
        userPassword = dictDetails.get(key)
