from db import DbConnection
dbConn = DbConnection()
# dbConn.insertData()


class registerUser:
    from userLogin import Userregister
    users = Userregister()
    dbConn.registerUser(fName=users.firstName, lName=users.lastName,
                        emailAddress=users.mailAddress, phoneNo=users.phoneNo)

    users.generatePassword()
    users.sendUserDetails()


obj1 = registerUser()
