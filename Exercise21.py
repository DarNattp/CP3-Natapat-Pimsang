from tkinter import *
import math
def leftClickButton(even):
    Result = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    #labelResult.configure(text= "%.1f" %Result)
    if Result >= 30.0:
        labelResult.configure(text="คุณอ้วนมาก", font=20, fg="red")
    elif Result >= 25.0 and Result <= 29.9:
        labelResult.configure(text="คุณอ้วน", font=20, fg="Orange")
    elif Result >= 23.0 and Result <= 24.9:
        labelResult.configure(text="คุณน้ำหนักเกิน", font=20, fg="yellow")
    elif Result >= 18.6 and Result <= 22.9:
        labelResult.configure(text="คุณน้ำหนักปกติเหมาะสม", font=20, fg="green")
    else:
        labelResult.configure(text="คุณผอมเกินไป", font=20, fg="red")

MainWindow = Tk()
labelHeight = Label(MainWindow, text = "ส่วนสูง (cm)", font=20)
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeight = Label(MainWindow, text = "น้ำหนัก (kg)", font=20)
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text = "คำนวณ", font=20)
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2,column=0)
labelResult = Label(MainWindow, text = "ผลลัพท์", font=20)
labelResult.grid(row=2,column=1)

MainWindow.mainloop()