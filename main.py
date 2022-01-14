from tkinter import *

master = Tk()



def close_window():
    exit()

def one():
    float(input(1))

def two():
	float(input(2))

def three():
	float(input(3))

def four():
	float(input(4))

def five():
	float(input(5))

def six():
	float(input(6))

def seven():
	float(input(7))

def eight():
	float(input(8))

def nine():
	float(input(9))

def zero():
	float(input(0))


def which_button(button_press):
    print(button_press)

def plus():
    float(input('+'))    

def minus():
    float(input('-'))
  

def equal():
    print("=")



# def add(num1, num2):
# 	result = num1 + num2


buttonexit = Button(master, text = 'Exit', command = close_window)
b0 = Button(master, text = '0', command= zero)
b1 = Button(master, text = '1', command = one)
b2 = Button(master, text = '2', command = two)
b3 = Button(master, text = '3', command = three)
b4 = Button(master, text = '4', command = four)
b5 = Button(master, text = '5', command = five)
b6 = Button(master, text = '6', command = six)
b7 = Button(master, text = '7', command = seven)
b8 = Button(master, text = '8', command = eight)
b9 = Button(master, text = '9', command = nine)
bp = Button(master, text = '+', command = plus)
bm = Button(master, text = '-', command = minus)
be = Button(master, text = '=', command = equal)


b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)
b0.grid(row=3, column=0)
bp.grid(row=2, column=3)
bm.grid(row=3, column=3)
be.grid(row=3, column=2)


print("What is your first number?")
num1 = Button(input())


print("What is your second number?")
num2 = Button(input()) 

print("What do you want to do?")
answer= input() 

if answer == ('+'):
    addnumber = num1 + num2
    print(addnumber)
    
if answer == ('-'):
    subnumber= num1 - num2
    print(subnumber)

mainloop()




#create buttons that work for numbers
#create addition/subtraction
#get addition and subtraction to work
#organize a little bit
#add in more complicated features
#text box etc