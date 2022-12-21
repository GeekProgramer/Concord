from tkinter import *
from tkinter import messagebox
from madlad import Madlad
import json

lp=Tk() #lp means login page
lp.title("Login")
lp.geometry("1200x600")
lp.configure(bg='black')
lp.resizable(True,False)
    
def error_msg( ):
    # pop up window
    messagebox.showerror("Incorrect username/password","Enter the correct credentials")    
    
client = Madlad()
def log_in(): #to log in (used below)
    username=user.get()
    password=passw.get()
    response = client.login(username, password)
    print(response)
    
    dat = json.loads(response)
    if "0" not in dat.keys():
        lp.destroy()
        import ctkinter
    
    else:
        error_msg() #a pop will show-up
        

def sign_up():
    lp.destroy()
    import signup
        

photo=PhotoImage(master = lp,file="g1.png")
Label(lp,image=photo,bg='black').place(x=50,y=110)

frame=Frame(lp,width=350,height=500,bg='black')
frame.place(x=425,y=70)

heading=Label(text="Log in",fg="#57a1f8",bg="#080808",font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=570,y=80)

def on_enter(e):
    name = user.get()
    if name == 'Enter Username':
        user.delete(0, 'end')
    else:
        pass
    
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Enter Username')
        
user=Entry(frame,width=295,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
user.place(x=25,y=80)
user.insert(1,'Enter Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

def on_enter(e):
    name = passw.get()
    if name == 'Enter Password':
        passw.delete(0, 'end')
    else:
        pass
def on_leave(e):
    name=passw.get()
    if name=='':
        passw.insert(0,'Enter Password')
        
passw=Entry(frame,width=295,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
passw.place(x=25,y=140)
passw.insert(1,'Enter Password')
passw.bind('<FocusIn>',on_enter)
passw.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=167)

login_b=Button(frame,width=45,pady=7,text='Log in',bg='#57a1f8',fg='white',border=0,command=log_in).place(x=24,y=204) #log_in user defined function
l1=Label(text="Don't haver an account?",fg='white',bg='#080808',font=('Microsoft YaHei UI Light',11)) #l1=dont have an acc
l1.place(x=530,y=320)

sign_up=Button(frame,width=6,text='Sign up',border=0,bg='#080808',cursor='hand2',fg='#57a1f8',command=sign_up)
sign_up.place(x=160,y=280)


lp.mainloop()