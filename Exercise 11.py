number = int(input("seleact number : "))
blank = " "
text = ""
for i in range(number):
    for j in range(i+1):
        text = blank*(number-i) + "*"*(i*2+1)
    print(text)