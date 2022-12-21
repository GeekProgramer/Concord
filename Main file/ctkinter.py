import customtkinter as ct
import pandas as pd
import mysql.connector as ms
import tkinter as tk
from tkinter import*
from tkinter import scrolledtext as st
from tkinter import messagebox
from PIL import Image,ImageTk
import urllib.request
import io
from madlad import Madlad
import json

def readUserData():
    username = ""
    with open("userData.json", "r") as openFile:
        json_object = json.load(openFile)
        username = json_object["username"]
    return username

usrn = readUserData()

madlad = Madlad()
chatClient = madlad.getChatManager()("8848")
class WebImage:
    def __init__(self, url):
        with urllib.request.urlopen(url) as u:
            raw_data = u.read()
            
            image = Image.open(io.BytesIO(raw_data))
            resize_image=image.resize((60,60))
            self.image = ImageTk.PhotoImage(resize_image)
            
    def get(self):
        return self.image




ct.set_appearance_mode("system")
ct.set_default_color_theme('blue')

def chat(event=None):
   chat=message_entry.get()
   chatClient.sendMessage(usrn, chat)
   message_entry.delete(0,'end')
   
   

def opt_frame():
    
    def close():
        frame2.destroy()
        button1.config(text='≡',command=opt_frame)
          
    frame2=ct.CTkFrame(master=cb,width=1920,height=1000)    #option menu frame
    frame2.place(x=0,y=0)
    button2=ct.CTkButton(master=frame2,text='⬅️',width=30,font=('Microsoft YaHei UI Light',22,'bold'),command=close).place(x=12,y=10)
    
    def logout():
        cb.destroy()
        import login
    log_out_bttn=ct.CTkButton(master=frame2,text='Log out ↪',width=40,command=logout).place(x=12,y=80)

def light_theme():
    ct.set_appearance_mode('light')
    ct.set_default_color_theme('blue')
    message_box.config(bg='#879FB7')
    app_name=ct.CTkLabel(master=frame5,text='Concord',font=('ROG Fonts',30,'bold'),bg_color='#dbdbdb').place(x=670,y=10)
    chat_txt=ct.CTkLabel(master=frame1,text='Chats',width=30,font=('Roboto',30,'bold'),bg_color='#dbdbdb').place(x=10,y=80)

def dark_theme():
    ct.set_appearance_mode('dark')
    ct.set_default_color_theme('dark-blue')
    message_box.config(bg='#444444')
    app_name=ct.CTkLabel(master=frame5,text='Concord',font=('ROG Fonts',30,'bold'),bg_color='#2b2b2b').place(x=670,y=10)
    chat_txt=ct.CTkLabel(master=frame1,text='Chats',width=30,font=('Roboto',30,'bold'),bg_color='#2b2b2b').place(x=10,y=80)
    

cb=ct.CTk() #cb means chat box
cb.geometry("1020x1020")
cb.title("Concord")
cb.config(bg='grey')
cb.state('zoomed')

frame1=ct.CTkFrame(master=cb).pack(pady=0,padx=0,fill='both',expand=True) #Main frame
frame5=ct.CTkFrame(master=frame1,width=1536,height=67,border_width=1,border_color='#13bbef').place(x=0,y=0)

button1=ct.CTkButton(master=frame5,text='≡',width=40,font=('Microsoft YaHei UI Light',25,'bold'),command=opt_frame).place(x=15,y=10)

app_name=ct.CTkLabel(master=frame5,text='Concord',font=('ROG Fonts',30,'bold'),bg_color='#2b2b2b').place(x=670,y=10)


theme_bttn1=ct.CTkButton(master=frame5,text='🔆',width=30,font=('Microsoft YaHei UI Light',25,'bold'),command=light_theme).place(x=1485,y=10)
theme_bttn2=ct.CTkButton(master=frame5,text='🌙',width=30,font=('Microsoft YaHei UI Light',25,'bold'),command=dark_theme).place(x=1425,y=10)

frame3=ct.CTkFrame(master=cb,width=300,height=800,border_width=1,border_color='#13bbef').place(x=0,y=67)
frame4=ct.CTkFrame(master=cb,width=1236,height=800,border_width=1,border_color='#13bbef').place(x=300,y=67)

scrollbar=Scrollbar(master=cb)

message_box=st.ScrolledText(master=cb,font=("Helvetica",23),bg='#444444', fg = "#ffffff",yscrollcommand=scrollbar.set)
scrollbar.config(command=message_box.yview)
message_box.pack()
message_box.place(x=400,y=100)

chatCol = "#444444"


class Example(tk.Frame):
    def __init__(self, parent):

        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth=0, height = 840, width = 1400, background = chatCol)

        self.frame = tk.Frame(self.canvas, background=chatCol)
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw",
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

    def populate(self, username, message, row):
            
        link = "https://th.bing.com/th/id/OIP.BUKBU3OEkRGQRWJrUS4P3QHaHa?pid=ImgDet&rs=1"
        img = WebImage(link).get()
        pfp = tk.Label(self.frame, image = img, width = 60, height = 60)
        usn = tk.Label(self.frame, text=username,background=chatCol,font=('Roboto',15),fg='white')
        mes = tk.Label(self.frame, text=message, background=chatCol,font=('Roboto',18),fg='white')

        pfp.grid(row=row,column=0,)
        pfp.photo = img
        usn.grid(row=row,column=1,sticky=N)
        mes.grid(row=row,column=1,sticky=S)
        
    def onFrameConfigure(self, event):
        
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

frameX=ct.CTkFrame(master=cb)

example = Example(cb)
example.pack(side="top", expand=True)
example.place(x=400, y=100)


chat_txt=ct.CTkLabel(master=frame1,text='Chats',width=30,font=('Roboto',30,'bold'),bg_color='#2b2b2b').place(x=10,y=80)

message_entry = ct.CTkEntry(master=cb,placeholder_text="Start Typing...",font=('Roboto',20,'bold'),width=1100,height=50,border_width=1,border_color='#13bbef',corner_radius=7)
message_entry.pack()
message_entry.bind('<Return>',lambda _:chat())
message_entry.place(x=310,y=785)

button = ct.CTkButton(master=frame1, text="Send",command=chat,height=50,width=100,border_width=1,border_color='#13bbef')
button.place(x=1420,y=785)

row = 0
def gotMessage(username, message):
    global row
    example.populate(username, message, row)
    row += 2
chatClient.onMessage(gotMessage)




cb.mainloop()