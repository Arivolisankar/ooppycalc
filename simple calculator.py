from tkinter import *

def btnclk(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+ str(number))

def clr():
    e.delete(0,END)



def equals():
    if math=="add":
        secondnum=e.get()
        secondnum=int(secondnum)
        e.delete(0,END)
        e.insert(0,fnum+secondnum)

    if math=="sub":
        secondnum=e.get()
        secondnum=int(secondnum)
        e.delete(0,END)
        e.insert(0,fnum-secondnum)
    
    if math=="mul":
        secondnum=e.get()
        secondnum=int(secondnum)
        e.delete(0,END)
        e.insert(0,fnum*secondnum)
    
    if math=="div":
        secondnum=e.get()
        secondnum=int(secondnum)
        e.delete(0,END)
        e.insert(0,fnum/secondnum)

def btn_add():
    firnum=e.get()
    global fnum
    global math
    math="add"
    fnum=int(firnum)
    e.delete(0,END)

def btn_sub():
    firnum=e.get()
    global fnum
    global math
    math="sub"
    fnum=int(firnum)
    e.delete(0,END)

def btn_mul():
    firnum=e.get()
    global fnum
    global math
    math="mul"
    fnum=int(firnum)
    e.delete(0,END)

def btn_div():
    firnum=e.get()
    global fnum
    global math
    math="div"
    fnum=int(firnum)
    e.delete(0,END)

root=Tk()
root.title("simple Calculator")

e=Entry(root,width=40,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

btn1=Button(root,text="1",padx=40,pady=20,command=lambda : btnclk(1))
btn2=Button(root,text="2",padx=40,pady=20,command=lambda : btnclk(2))
btn3=Button(root,text="3",padx=40,pady=20,command=lambda : btnclk(3))
btn4=Button(root,text="4",padx=40,pady=20,command=lambda : btnclk(4))
btn5=Button(root,text="5",padx=40,pady=20,command=lambda : btnclk(5))
btn6=Button(root,text="6",padx=40,pady=20,command=lambda : btnclk(6))
btn7=Button(root,text="7",padx=40,pady=20,command=lambda : btnclk(7))
btn8=Button(root,text="8",padx=40,pady=20,command=lambda : btnclk(8))
btn9=Button(root,text="9",padx=40,pady=20,command=lambda : btnclk(9))
btn0=Button(root,text="0",padx=40,pady=20,command=lambda : btnclk(0))

btnadd=Button(root,text="+",padx=40,pady=20,command=btn_add)
btnclr=Button(root,text="C",padx=40,pady=20,command=clr)
btnequ=Button(root,text="=",padx=140,pady=20,command=equals)

btnsub=Button(root,text="-",padx=40,pady=20,command=btn_sub)
btnmul=Button(root,text="*",padx=40,pady=20,command=btn_mul)
btndiv=Button(root,text="/",padx=40,pady=20,command=btn_div)

btn7.grid(row=1,column=0)
btn8.grid(row=1,column=1)
btn9.grid(row=1,column=2)

btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)

btn1.grid(row=3,column=0)
btn2.grid(row=3,column=1)
btn3.grid(row=3,column=2)

btn0.grid(row=5,column=0)
btnadd.grid(row=5,column=1)
btnclr.grid(row=5,column=2)

btnequ.grid(row=6,columnspan=3)

btnsub.grid(row=7,column=0)
btnmul.grid(row=7,column=1)
btndiv.grid(row=7,column=2)
root.mainloop()