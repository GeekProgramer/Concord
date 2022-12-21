from tkinter import *
from tkinter import messagebox
from madlad import Madlad
import json

sp=Tk() #sp means sign in page
sp.title("Sign up")
sp.geometry("900x600")
sp.configure(bg='black')
sp.resizable(False,False)
client = Madlad()
    
photo=PhotoImage(master = sp, file="itachi.png")
Label(sp,image=photo,bg='black',).place(x=380,y=50)

frame=Frame(sp,width=350,height=500,bg='black')
frame.place(x=30,y=70)

heading=Label(text="Sign up",fg="#57a1f8",bg="black",font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=150,y=80)

pfp = ""


def userData(username):
    dic = {"username": username}
    with open("userData.json", "w") as outfile:
        json.dump(dic, outfile)
    
    
def sign_up():
    name=user.get()
    password=passw.get()
    c_password=cpassw.get()
    
    if c_password==password :
        response = client.register(name, password)
        dat = json.loads(response)
        if len(dat) != 0:
            print(response)
            userData(name)
            messagebox.showinfo("Successfull!","You've successfully signed up!!")
            sp.destroy()
            import ctkinter
        else:
            messagebox.showerror("ERROR","Username taken")
         
    else:
        messagebox.showerror("ERROR","Confirmed password does not match")
def log_in():
    sp.destroy()
    import login 
    

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
user.place(x=25,y=85)
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
passw.place(x=25,y=130)
passw.insert(1,'Enter Password')
passw.bind('<FocusIn>',on_enter)
passw.bind('<FocusOut>',on_leave)

def on_enter(e):
    name = cpassw.get()
    if name == 'Confirm Password':
        cpassw.delete(0, 'end')
    else:
        pass
def on_leave(e):
    name=cpassw.get()
    if name=='':
        cpassw.insert(0,'Confirm Password')
        
cpassw=Entry(frame,width=295,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
cpassw.place(x=25,y=170)
cpassw.insert(1,'Confirm Password')
cpassw.bind('<FocusIn>',on_enter)
cpassw.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=167)


sign_b=Button(frame,width=50,pady=7,text='Sign up',bg='#57a1f8',fg='white',border=0,command=sign_up).place(x=24,y=248) #sign_in user defined function
s1=Label(frame,text="Already haver an account?",fg='white',bg='black',font=('Microsoft YaHei UI Light',11)).place(x=90,y=290)

log_i=Button(frame,width=6,text='Log in',border=0,bg='black',cursor='hand2',fg='#57a1f8',command=log_in)
log_i.place(x=160,y=330)


sp.mainloop()