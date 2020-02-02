def login():
    username = input("Username : ")
    password = input("Password : ")
    if username == "Natapat" and password == "1234":
        return showMenu()
    else:
        print("Wrong user or password !")
        return login()

def showMenu():
    print("1. VAT Calculator")
    print("2. Price Calculator")
    return menuSelect()

def menuSelect():
    userSelected = int(input("Select number : "))
    if userSelected == 1:
        return vatCalculate(totalPrice=int(input("Total Price: ")))
    elif userSelected == 2:
        return priceCalculate()

def vatCalculate(totalPrice):
    vat = float(input("VAT(%): "))
    print("Price including vat: "+str(totalPrice + (totalPrice*vat/100)))

def priceCalculate():
    price1 = int(input("First Product Price: "))
    price2 = int(input("Second Product Price: "))
    return vatCalculate(price1 + price2)

login()