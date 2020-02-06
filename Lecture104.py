class Customer:
    name = ""
    lastname = ""
    age = 0

    def addCart(self):
        print("added product to" ,self.name, self.lastname ,"'s cart who had" , self.age,"years old" )

customer1 = Customer()
customer1.name = "Natapat"
customer1.lastname = "Pimsang"
customer1.age = 23

customer1.addCart()