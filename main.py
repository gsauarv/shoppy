from db import DbConnection
dbConn = DbConnection()
# dbConn.insertData()

# class registerUser:
#     from userLogin import Userregister
#     users = Userregister()
#     users.generatePassword()
#     dbConn.registerUser(fName=users.firstName, lName=users.lastName,
#                         emailAddress=users.mailAddress, phoneNo=users.phoneNo, password=users.generatedPassword)
#     users.sendUserDetails()


class loginUser:
    from userLogin import UserLogin
    import hashlib
    userLog = UserLogin()
    lists = dbConn.userLogin(email=userLog.userName)
    dictDetails = dict(lists)
    userEmail = ""
    userPassword = ""
    for key in dictDetails:
        userEmail = key
        userPassword = dictDetails.get(key)

    if(userEmail == userLog.userName and userPassword == (hashlib.md5(userLog.Password.encode()).hexdigest())):
        print("Loged In")

    else:
        print("Incorrect Email or Password")


    # obj1 = registerUser()
obj2 = loginUser()
