from tkinter import *
import tkinter.font
from algorithm import *

win = Tk()
win.title('mcnspire')
win.geometry("300x320")
ft = tkinter.font.Font(family = "Helvetica", size = 30)

def convertdeg():
    mse.deg = eval(onAndoff.get())

def convertrad():
    mse.deg = eval(onAndoff.get())

class body:
    def __init__(self):
        self.todisp = ""
        self.toeval = ""
        
    def store1(self):
        self.todisp = self.todisp + "1"
        self.toeval = self.toeval + "1"
        display.set(self.todisp)

    def store2(self):
        self.todisp = self.todisp + "2"
        self.toeval = self.toeval + "2"
        display.set(self.todisp)

    def store3(self):
        self.todisp = self.todisp + "3"
        self.toeval = self.toeval + "3"
        display.set(self.todisp)

    def store4(self):
        self.todisp = self.todisp + "4"
        self.toeval = self.toeval + "4"
        display.set(self.todisp)

    def store5(self):
        self.todisp = self.todisp + "5"
        self.toeval = self.toeval + "5"
        display.set(self.todisp)

    def store6(self):
        self.todisp = self.todisp + "6"
        self.toeval = self.toeval + "6"
        display.set(self.todisp)

    def store7(self):
        self.todisp = self.todisp + "7"
        self.toeval = self.toeval + "7"
        display.set(self.todisp)

    def store8(self):
        self.todisp = self.todisp + "8"
        self.toeval = self.toeval + "8"
        display.set(self.todisp)

    def store9(self):
        self.todisp = self.todisp + "9"
        self.toeval = self.toeval + "9"
        display.set(self.todisp)

    def store0(self):
        self.todisp = self.todisp + "0"
        self.toeval = self.toeval + "0"
        display.set(self.todisp)

    def storedot(self):
        self.todisp = self.todisp + "."
        self.toeval = self.toeval + "."
        display.set(self.todisp)

    def storeplus(self):
        self.todisp = self.todisp + "+"
        self.toeval = self.toeval + "+"
        display.set(self.todisp)

    def storeminus(self):
        self.todisp = self.todisp + "-"
        self.toeval = self.toeval + "-"
        display.set(self.todisp)

    def storetimes(self):
        self.todisp = self.todisp + "x"
        self.toeval = self.toeval + "*"
        display.set(self.todisp)

    def storedivide(self):
        self.todisp = self.todisp + "÷"
        self.toeval = self.toeval + "/"
        display.set(self.todisp)

    def storecomma(self):
        self.todisp = self.todisp + ","
        self.toeval = self.toeval + ","
        display.set(self.todisp)

    def storeop(self):
        self.todisp = self.todisp + "("
        self.toeval = self.toeval + "("
        display.set(self.todisp)

    def storecp(self):
        self.todisp = self.todisp + ")"
        self.toeval = self.toeval + ")"
        display.set(self.todisp)

    def storepie(self):
        self.todisp = self.todisp + "π"
        self.toeval = self.toeval + "pi"
        display.set(self.todisp)

    def storee(self):
        self.todisp = self.todisp + "e"
        self.toeval = self.toeval + "e"
        display.set(self.todisp)

    def storeln(self):
        self.todisp = self.todisp + "ln("
        self.toeval = self.toeval + "ln("
        display.set(self.todisp)

    def storelog(self):
        self.todisp = self.todisp + "log("
        self.toeval = self.toeval + "log("
        display.set(self.todisp)

    def storesin(self):
        self.todisp = self.todisp + "sin("
        self.toeval = self.toeval + "sin("
        display.set(self.todisp)

    def storecos(self):
        self.todisp = self.todisp + "cos("
        self.toeval = self.toeval + "cos("
        display.set(self.todisp)

    def storetan(self):
        self.todisp = self.todisp + "tan("
        self.toeval = self.toeval + "tan("
        display.set(self.todisp)

    def storecot(self):
        self.todisp = self.todisp + "cot("
        self.toeval = self.toeval + "cot("
        display.set(self.todisp)

    def storesqroot(self):
        self.todisp = self.todisp + "√("
        self.toeval = self.toeval + "root(2,"
        display.set(self.todisp)
        
    def clear(self):
        self.todisp = ""
        self.toeval = ""
        display.set(self.todisp)

    def delete(self):
        self.todisp = self.todisp[0:len(self.todisp)-1]
        self.toeval = self.toeval[0:len(self.toeval)-1]
        display.set(self.todisp)

    def equals(self):
        try:
            answer = eval(self.toeval)
            display.set(str(round(answer, 5)))
            self.toeval = ""
        except SyntaxError:
            if self.toeval == "":
                display.set("")
            else:
                display.set("Error:Invalid Syntax")
                self.toeval = ""
        except ZeroDivisionError:
            display.set("Error:Zero Division")
            self.toeval = ""

calc = body()
display = StringVar()
onAndoff = StringVar()

disp = Label(win, width = 16, anchor = "ne", textvariable = display, relief = GROOVE, font = ft)
disp.place(x=10, y=20)

author = Label(win, text = "Powered by mc", relief = SUNKEN, width = 13, bg = 'blue', fg = 'red')
author.place(x=25,y=280)

one = Button(win, text = "1", command = calc.store1)
one.place(x=10, y=80)
two = Button(win, text = "2", command = calc.store2)
two.place(x=50, y=80)
three = Button(win, text = "3", command = calc.store3)
three.place(x=90, y=80)
plus = Button(win, text = "+", command = calc.storeplus)
plus.place(x=130, y=80)
four = Button(win, text = "4", command = calc.store4)
four.place(x=10, y=120)
five = Button(win, text = "5", command = calc.store5)
five.place(x=50, y=120)
six = Button(win, text = "6", command = calc.store6)
six.place(x=90, y=120)
minus = Button(win, text = "-", command = calc.storeminus)
minus.place(x=130, y=120)
seven = Button(win, text = "7", command = calc.store7)
seven.place(x=10, y=160)
eight = Button(win, text = "8", command = calc.store8)
eight.place(x=50, y=160)
nine = Button(win, text = "9", command = calc.store9)
nine.place(x=90, y=160)
times = Button(win, text = "x", command = calc.storetimes)
times.place(x=130, y=160)
zero = Button(win, text = "0", command = calc.store0)
zero.place(x=10, y=200)
dot = Button(win, text = ".", command = calc.storedot)
dot.place(x=50, y=200)
clear = Button(win, text = "c", command = calc.clear)
clear.place(x=90, y=200)
divide = Button(win, text = "÷", command = calc.storedivide)
divide.place(x=130, y=200)
comma = Button(win, text = ",", command = calc.storecomma)
comma.place(x=90, y=240)
eql = Button(win, text = "=", command = calc.equals)
eql.place(x=130, y=240)
delete = Button(win, text = "del", command = calc.delete)
delete.place(x=170, y=240)
op = Button(win, text = "(", command = calc.storeop)
op.place(x=10, y=240)
cp = Button(win, text = ")", command = calc.storecp)
cp.place(x=50, y=240)
pie = Button(win, text = "π", command = calc.storepie)
pie.place(x=175, y=80)
epsilon = Button(win, text = "e", command = calc.storee)
epsilon.place(x=230, y=80)
natural_log = Button(win, text = "ln", command = calc.storeln)
natural_log.place(x=173, y=120)
logarithm = Button(win, text = "log", command = calc.storelog)
logarithm.place(x=220, y=120)
sine = Button(win, text = "sin", command = calc.storesin)
sine.place(x=170, y=160)
cosine = Button(win, text = "cos", command = calc.storecos)
cosine.place(x=220, y=160)
tangent = Button(win, text = "tan", command = calc.storetan)
tangent.place(x=170, y=200)
cotangent = Button(win, text = "cot", command = calc.storecot)
cotangent.place(x=220, y=200)
sqroot = Button(win, text = "√", command = calc.storesqroot)
sqroot.place(x=220, y=240)

degree = Checkbutton(win, text = "deg", command = convertdeg, variable = onAndoff, onvalue = 'True', offvalue = 'False')
degree.place(x=10,y=60)


mainloop()
