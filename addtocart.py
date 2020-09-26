from db import DbConnection
dbConn = DbConnection()


class addtoCart:
    def __init__(self, email, productname, productQty):
        self.productName = productname
        self.productQuantity = productQty
        self.emails = email
        dbConn.addToCart(self.emails, self.productName, self.productQuantity)


class getProduct:

    def productDetails(self, email):
        self.a = email
        from db import DbConnection
        dbConn = DbConnection()
        lists = dbConn.getProductDetails(email=self.a)
        dictDetails = dict(lists)
        return dictDetails


class getDetails:
    def getDetail(self):
        from db import DbConnection
        dbConn = DbConnection()
        lis = dbConn.getCustDetails()
        dictDetail = list(lis)
        return dictDetail

    def getCartList(self):
        from db import DbConnection
        dbConn = DbConnection()
        proList = dbConn.getOrderList()
        dictDetails = list(proList)
        return dictDetails

    def getInventory(self):
        from db import DbConnection
        dbConn = DbConnection()
        inventory = dbConn.getInventory()
        dictDetails = list(inventory)
        return dictDetails
