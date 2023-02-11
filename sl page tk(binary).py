import mysql.connector
import mysql.connector as sqltor
from tkinter import *
import random
import tkinter as tk
from tkinter import ttk
import winsound
from PIL import *
from PIL import Image, ImageTk
from tkinter import ttk
import webbrowser


#start of GUI
window=tk.Tk()
window.title("VARP Mangement program")
window.attributes("-fullscreen",True)

#notebook deployed
notebook = ttk.Notebook(window)
notebook.place(x=0,y=0)

#frames
frame1 = ttk.Frame(notebook,width=10000,height=900)

frame2 = ttk.Frame(notebook,width=10000,height=900)

frame3 = ttk.Frame(notebook,width=10000,height=900)

frame4 =  ttk.Frame(notebook,width=10000,height=900)

frame5 =  ttk.Frame(notebook,width=10000,height=900)

frame6 =  ttk.Frame(notebook,width=10000,height=900)

frame7 =  ttk.Frame(notebook,width=10000,height=900)

frame8 =  ttk.Frame(notebook,width=10000,height=900)

frame9 =  ttk.Frame(notebook,width=10000,height=900)

frame10 =  ttk.Frame(notebook,width=10000,height=900)

frame11 =  ttk.Frame(notebook,width=10000,height=900)

frame12 = ttk.Frame(notebook,width=10000,height=900)

frame13 = ttk.Frame(notebook,width=10000,height=900)

frame14 = ttk.Frame(notebook,width=10000,height=900)

frame15 =  ttk.Frame(notebook,width=10000,height=900)

frame16 =  ttk.Frame(notebook,width=10000,height=900)

frame17 =  ttk.Frame(notebook,width=10000,height=900)

frame18 =  ttk.Frame(notebook,width=10000,height=900)

frame19 =  ttk.Frame(notebook,width=10000,height=900)

frame20 =  ttk.Frame(notebook,width=10000,height=900)

frame21 =  ttk.Frame(notebook,width=10000,height=900)

frame22 =  ttk.Frame(notebook,width=10000,height=900)


#frames placed
frame1.place(x=0,y=0)

frame2.place(x=0,y=0)

frame3.place(x=0,y=0)

frame4.place(x=0,y=0)

frame5.place(x=0,y=0)

frame6.place(x=0,y=0)

frame7.place(x=0,y=0)

frame8.place(x=0,y=0)

frame9.place(x=0,y=0)

frame10.place(x=0,y=0)

frame11.place(x=0,y=0)

frame12.place(x=0,y=0)

frame13.place(x=0,y=0)

frame14.place(x=0,y=0)

frame15.place(x=0,y=0)

frame16.place(x=0,y=0)

frame17.place(x=0,y=0)

frame18.place(x=0,y=0)

frame19.place(x=0,y=0)

frame20.place(x=0,y=0)

frame21.place(x=0,y=0)

frame22.place(x=0,y=0)

#frames deployed
notebook.add(frame1, text='0')

notebook.add(frame2, text='1')

notebook.add(frame3, text='2')

notebook.add(frame4, text='3')

notebook.add(frame5, text='4')

notebook.add(frame6, text='5')

notebook.add(frame7, text='6')

notebook.add(frame8, text='7')

notebook.add(frame9, text='8')

notebook.add(frame10, text='9')

notebook.add(frame11, text='10')

notebook.add(frame12, text='11')

notebook.add(frame13, text='12')

notebook.add(frame14, text='13')

notebook.add(frame15, text='14')

notebook.add(frame16, text='15')

notebook.add(frame17, text='16')

notebook.add(frame18,text='17')

notebook.add(frame19, text='18')

notebook.add(frame20, text='19')

notebook.add(frame21, text='20')

notebook.add(frame22, text='21')



#hiding the tab tiles

#variables
winsound.PlaySound('song (1).wav',winsound.SND_ASYNC  + winsound.SND_LOOP)
e=0

#commands(switch if and else before sumission)
def play_music():
    global e
    e+=1
    if e%2==0:
        print(e)
        winsound.PlaySound('song (1).wav',winsound.SND_ASYNC  + winsound.SND_LOOP)
    else:
        print(e)
        winsound.PlaySound(None, winsound.SND_PURGE)


####################
photo1=Image.open("item1.png")
resize_button_img1=photo1.resize((180,300))
img1=ImageTk.PhotoImage(resize_button_img1)

photo2=Image.open("item2.png")
resize_button_img2=photo2.resize((180,300))
img2=ImageTk.PhotoImage(resize_button_img2)

photo3=Image.open("item3.png")
resize_button_img3=photo3.resize((180,300))
img3=ImageTk.PhotoImage(resize_button_img3)

photo4=Image.open("item4.png")
resize_button_img4=photo4.resize((180,300))
img4=ImageTk.PhotoImage(resize_button_img4)

photo5=Image.open("item5.png")
resize_button_img5=photo5.resize((180,300))
img5=ImageTk.PhotoImage(resize_button_img5)

photo6=Image.open("item6.png")
resize_button_img6=photo6.resize((180,300))
img6=ImageTk.PhotoImage(resize_button_img6)

photo7=Image.open("item7.png")
resize_button_img7=photo7.resize((180,300))
img7=ImageTk.PhotoImage(resize_button_img7)

photo8=Image.open("item8.png")
resize_button_img8=photo8.resize((180,300))
img8=ImageTk.PhotoImage(resize_button_img8)

photo9=Image.open("item9.png")
resize_button_img9=photo9.resize((180,300))
img9=ImageTk.PhotoImage(resize_button_img9)

photo10=Image.open("item10.png")
resize_button_img10=photo10.resize((180,300))
img10=ImageTk.PhotoImage(resize_button_img10)


#################
        
price=0

def go_to_main_menu():
    notebook.select(0)

def go_to_settings():
    notebook.select(1)



def go_to_entry():
    notebook.select(2)

def go_to_login():
    notebook.select(3)

def go_to_otp():
    notebook.select(4)

def go_to_functions():
    notebook.select(5)

def check_otp():
    pass

def go_to_drinks():#6
    notebook.select(6)

def go_to_food():#7
    notebook.select(7)
    global price
    price=0
    bill.set(price)


def go_to_final_bill():#7
    notebook.select(8)
    global price
    if var1.get() ==1:
        price+=1
    if var2.get()==1:
        price+=2
    if var3.get()==1:
        price+=3
    if var4.get()==1:
        price+=4
    if var5.get()==1:
        price+=5
    if var6.get()==1:
        price+=6
    if var6.get()==1:
        price+=6
    if var7.get()==1:
        price+=7
    if var8.get()==1:
        price+=8
    if var9.get()==1:
        price+=9
    if var10.get()==1:
        price+=10
    print("bill: ",price)
    bill.set(price)
        
        

def go_to_pincode():#6
    notebook.select(9)

def go_to_parking():#6
    notebook.select(10)

def go_to_website():#6
    webbrowser.open('https://cafe.synergize.co/index.php?/archives/1-Rate-Us.html')

def go_to_reservation():#6
    notebook.select(11)

def go_to_reservation_entry():#in 12 frame
    notebook.select(12)
    
def go_to_reservation_check():#in 12 frame
    notebook.select(13)

def go_to_parking_entry():#in 11 frame
    notebook.select(14)

def go_to_parking_check():#in 11 frame
    notebook.select(15)
def go_to_parking_checkout():#in 11 frame
    notebook.select(17)
def go_to_check_out():
    notebook.select(16)

def end():#17
    notebook.select(16)
def dele():
    ea.place_forget()
def del2():
    ea2.place_forget()
def del1():
    ea1.place_forget()
def del3():
    ea3.place_forget()
def del4():
    ea4.place_forget()
def del5():
    ea5.place_forget()
def login_check():
    #sql
    mycon=sqltor.connect(host="localhost",user='root',passwd='vrishank',database='data')

    #creating cursor
    cursor=mycon.cursor(buffered=True)
    #selecting the data
    sql = '''SELECT * from userdata'''

    #Executing the query
    cursor.execute(sql)


    #fetching data from sql
    userdata_sql=cursor.fetchall()

    k=dict(userdata_sql)
    username= E4.get()
    password= E5.get()
    if username in k and password ==k[username]:
        global ea
        ea=Label(frame4,text='login approved',font=('LucidaConsole 25 bold'),borderwidth=2,bd=2,fg='green')
        ea.place(x=500,y=450)
        notebook.select(5)
        window.after(800,dele)
        
    elif username not in k:
        global ea1
        ea1=Label(frame4,text='username invalid',font=('LucidaConsole 25 bold'),borderwidth=2,bd=2,fg='red')
        ea1.place(x=500,y=450)
        window.after(800,del1)
    elif username in k and password !=k[username]:
        global ea2
        ea2=Label(frame4,text='password invalid',font=('LucidaConsole 25 bold'),borderwidth=2,bd=2,fg='red')
        ea2.place(x=500,y=450)
        window.after(800,del2)
    

    #ending
    cursor.close()
    mycon.close()
################################################
#sql
mycon=sqltor.connect(host="localhost",user='root',passwd='vrishank',database='data')


    #creating cursor
cursor=mycon.cursor(buffered=True)
cursor2=mycon.cursor(buffered=True)
    #selecting the data
sql = '''SELECT * from userdata'''
sql2 = '''SELECT * from gmail_id'''

    #Executing the query
cursor.execute(sql)
cursor2.execute(sql2)


#fetching data from sql
userdata_sql=cursor.fetchall()
userdata_sql2=cursor2.fetchall()

k=dict(userdata_sql)
#proper list in python
gmail=[]


#to store data in the properlist
for t in userdata_sql2:
    for x in t:
        gmail.append(x)

        
tor=gmail
print(tor)

    #ending
cursor.close()
mycon.close()
####################
def signin():
    username=E1.get()
    password=E2.get()
    g=E3.get()
    if username in k:
        if g in tor:
            global ea5
            ea5=Label(frame3,text='gmail is already in use',font=('LucidaConsole 25 bold'),borderwidth=2,bd=2,fg='green')
            ea5.place(x=500,y=450)
            window.after(500,del5)
        else:
            ea5=Label(frame3,text='username already taken,chose a new one',font=('LucidaConsole 25 bold'),borderwidth=2,bd=2,fg='green')
            ea5.place(x=500,y=450)
            window.after(500,del5)
    elif username not in k:
        if g not in tor:
            import smtplib
            server=smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login("botforproject@gmail.com", "dprzhddfvxtotxxb")
            import random
            x=E3.get()
            global y
            y=random.randint(1000,9999)
            global n
            n=str(y)
            if x==g:
                server.sendmail("botforproject@gmail.com",x,n)
                server.quit()
            else:
                pass
            import mysql.connector
            import mysql.connector as sqltor


            #connection
            mycon=sqltor.connect(host="localhost",user='root',passwd='vrishank',database='data')

            #making cursor
            cursor=mycon.cursor()

            #adding data through cursor
            cursor.execute("insert into userdata(username,password) values(%s,%s)",(username, password))
            mycon.commit()

            #end
            cursor.close()
            mycon.close()



            #saving gmail id
            mycon1=sqltor.connect(host="localhost",user='root',passwd='vrishank',database='data')

            #making cursor
            cursor=mycon1.cursor()


            #adding data through cursor
            cursor.execute("insert into gmail_id(gmail) value(%s)",[g])
            mycon1.commit()

            cursor.close()
            mycon1.close()
            notebook.select(4)
        



def otp_check():
    print(n)
    z=E6.get()
    u=str(z)
    if u==n:
        window.after(400,go_to_main_menu)
        global ea3
        ea3=Label(frame5,text='sign up approved',font=('LucidaConsole 25 bold'),borderwidth=2,bd=2,fg='green')
        ea3.place(x=500,y=450)
        window.after(400,del3)
    elif u!=n:
        global ea4
        ea4=Label(frame5,text='OTP was wrong',font=('LucidaConsole 25 bold'),borderwidth=2,bd=2,fg='red')
        ea4.place(x=500,y=450)
        window.after(800,del4)
        print('this',u)
    elif u=='':
        print("error")

def dele97():
    e97.place_forget()
def pincode_s():
    import mysql.connector
    import mysql.connector as sqltor
    from collections import ChainMap

    #connection
    mycon=sqltor.connect(host="localhost",user='root',passwd='vrishank',database='data')

    #creating cursor
    cursor=mycon.cursor(buffered=True)

    #selecting the data
    sql = '''SELECT * from pincode'''

    #Executing the query
    cursor.execute(sql)


    #fetching data from sql
    userdata_sql=cursor.fetchall()
    z={}

    x=userdata_sql

    y=[]
    for t in x:
        for x in t:
            y.append(x)
    w=[]
    print(y)
    oz=E7.get()
    op=int(oz)
    print(op)
    z=[]
    for i in range(0,len(y)):
        pl=int(y[i])
        zzzz=pl-op
        if zzzz>=0:
            z.append(zzzz)
        elif zzzz<=0:
            zzpos=zzzz*-1
            z.append(zzpos)
    mini=min(z)
    print(mini)
    print(y)
    pincode=op+mini
    pincode2=op-mini
    global e97
    pincode_str=str(pincode)
    pincode_str2=str(pincode2)
    if pincode_str in y:
        print(pincode)
        pin= StringVar()
        pin.set(pincode_str)
        e97=Label(frame10,textvariable =pin,font=('Helvetica 22 bold'))
        e97.place(x=600,y=350,height=30)
        window.after(800,dele97)
        ea98=Label(frame10,text="this the nearest pincode",font=('LucidaConsole 25 bold'),borderwidth=2,bd=2,fg='red')
        ea98.place(x=200,y=350)
    elif pincode_str2 in y:
        print(pincode2)
        pin= StringVar()
        pin.set(pincode_str2)
        e97=Label(frame10,textvariable =pin,font=('Helvetica 22 bold'))
        e97.place(x=600,y=350,height=30)
        window.after(800,dele97)
        ea98=Label(frame10,text="this the nearest pincode",font=('LucidaConsole 25 bold'),borderwidth=2,bd=2,fg='red')
        ea98.place(x=200,y=350)
            
        


    #ending
    cursor.close()
    mycon.close()



def dele100():
    e100.place_forget()
def dele102():
    e102.place_forget()
def dele103():
    e103.place_forget()
def dele104():
    e104.place_forget()
def dele105():
    e105.place_forget()

def checkout():
    #To check out rooms booked under same username
    import pickle
    pincode=E16.get()
    f=pincode+".dat"
    fh=open(f,'rb')
    y=[]
    x=-1
    z=True
    try:
       while z==True:
          try:
             hotel=pickle.load(fh)
             print(hotel)
             y.append(hotel[1])
          except EOFError:
             z=False
             break
    except EOFError:
       print('End of File')
    found = False
    d={}
    print(y)
    try:
        uname=E17.get()
        for i in range(len(y)):
            if uname in y[i]:
                print(i)
                x=i
                global e100
                e100=Label(frame17,text="check out successful",font=('Helvetica 22 bold'))
                e100.place(x=600,y=300,height=30)
                window.after(800,dele100)
            else:
                global e102
                e102=Label(frame17,text="name invalid",font=('Helvetica 22 bold'))
                e102.place(x=600,y=300,height=30)
                window.after(800,dele102)
        fh.close()
        if x>=0:
            fh=open(f,'wb')
            fh.close()
            y.pop(x)
            for i in range(len(y)):
                fh=open(f,'ab')
                z=[1,y[i]]
                dt=dict([z])
                pickle.dump(dt,fh)
        else:
            pass
    except EOFError:
        if found == True:
            print("Check-out successful!")
        else :
            print("Username not found!")
    print(y)
    fh.close()
def search():
    #To check rooms boooked under one username
    import pickle
    pincode=E18.get()
    f=pincode+".dat"
    uname=E9.get()
    file=open(f, "rb")
    found=False
    try:
        while True:
            hotel=pickle.load(file)
            for i in hotel:
                if hotel[i][1]==uname:
                    done = StringVar()
                    done.set(hotel[i])
                    global e103
                    e103=Label(frame14,textvariable =done,font=('Helvetica 22 bold'))
                    e103.place(x=735,y=300,height=30)
                    window.after(800,dele103)
                    print(hotel[i])
                    found=True
                    break
    except EOFError:
        if found==False:
            global e104
            e104=Label(frame14,text="username not found",font=('Helvetica 22 bold'))
            e104.place(x=600,y=300,height=30)
            window.after(800,dele104)
        else:
            print ("Rooms successfully checked.")

    file.close()

def entry_in_hotel():
    import os
    import pickle
    pincode=E11.get()
    f=pincode+".dat"
    fh=open(f,'ab')
    hotel={}
    for i in range(0,120):
        val=[]
        date1=E12.get()
        if(os.path.getsize(f)==0 or len(hotel)==0):#check and put date booking
            print("Room",i+1,"is available")
            uname=E10.get()
            date2=E19.get()
            status="Reserved"
            hotel[i+1]=[status, uname, date1, date2]
            print("Username:", hotel[i+1][1])
            print("Check-in date:", hotel[i+1][2])
            print("Check in time is 12:00 p.m.") 
            print("Check-out date:", hotel[i+1][3])
            print("Check out time is 11:00 a.m.")
            pickle.dump(hotel,fh)
            global e105
            e105=Label(frame13,text="reservation complete",font=('Helvetica 22 bold'))
            e105.place(x=550,y=386,height=30)
            window.after(800,dele105)
            fh.close()
            print(hotel)
            break
        else:
            print("Room is not available.")
            ch=input("Try again(y/n):")
            if ch=='n':
                fh.close()
                break               
    else:
        print("No rooms available")
        file.close()
    fh.close()

def dele108():
    e108.place_forget()
def parking_checkout():#frame 17 check out
    import mysql.connector
    import mysql.connector as sqltor


    #connection
    mycon=sqltor.connect(host="localhost",user='root',passwd='vrishank',database='data')

    #creating cursor
    cursor=mycon.cursor(buffered=True)
    username=E21.get()
    pincode=E20.get()
    #selecting the data
    sql = 'delete from valet where username= '+'"'+username+'"'' and pincode='+'"'+pincode+'"'+';'
    print(sql)
    #Executing the query
    cursor.execute(sql)
    mycon.commit()
    global e108
    e108=Label(frame18,text="checkout complete",font=('Helvetica 22 bold'))
    e108.place(x=600,y=300,height=30)
    window.after(800,dele108)
    
    #ending
    cursor.close()
    mycon.close()
def dele99():
    e99.place_forget()
def parking_search():
    import mysql.connector
    import mysql.connector as sqltor
    from collections import ChainMap

    #connection
    mycon=sqltor.connect(host="localhost",user='root',passwd='vrishank',database='data')

    #creating cursor
    cursor=mycon.cursor(buffered=True)

    #selecting the data
    sql = '''SELECT * from valet'''

    #Executing the query
    cursor.execute(sql)


    #fetching data from sql
    userdata_sql=cursor.fetchall()
    z={}

    x=userdata_sql
    print(x)
    y=[]
    for t in x:
        for x in t:
            y.append(x)
    w=[]
    print(y)
    for i in range(0,len(y),4):
        if i==len(y)-3:
            break
        else:
            q=[y[i+1],y[i+2],y[i+3]]
            p=dict(details=q,user=y[i])
            i+=2
            w.append(p)
    print(w)


    res  = {}
    user=E8.get()
    for i in range(0,len(w)):
        res.update(w[i])
        if user== res['user']:
            print(res['details'])
            done = StringVar()
            done.set(res['details'])
            global e99
            e99=Label(frame16,textvariable =done,font=('Helvetica 22 bold'))
            e99.place(x=735,y=300,height=30)
            window.after(1200,dele99)
        elif user != res['user']:
            continue
        else:
            continue
            
    #ending
    cursor.close()
    mycon.close()
def dele106():
    e106.place_forget()
def dele107():
    e107.place_forget()
def parking_entry():
    import mysql.connector
    import mysql.connector as sqltor
    import mysql.connector
    import mysql.connector as sqltor
    from collections import ChainMap

    #connection
    mycon=sqltor.connect(host="localhost",user='root',passwd='vrishank',database='data')

    #creating cursor
    cursor=mycon.cursor(buffered=True)

    #selecting the data
    sql = '''SELECT * from valet'''

    #Executing the query
    cursor.execute(sql)


    #fetching data from sql
    userdata_sql=cursor.fetchall()
    z={}

    x=userdata_sql
    print(x)
    y=[]
    for t in x:
        for x in t:
            y.append(x)
    w=[]
    print(y)
    for i in range(0,len(y),4):
        if i==len(y)-3:
            break
        else:
            q=[y[i+1],y[i+2],y[i+3]]
            p=dict(details=q,user=y[i])
            i+=2
            w.append(p)
    print(w)
    #ending
    cursor.close()
    mycon.close()



    #data input
    username=E13.get()
    pincode=E22.get()
    PAC=E14.get()
    time=E15.get()
    res={}
    foundz=False
    for i in range(0,len(w)):
        res.update(w[i])
        if username== res['user']:
            if i==len(w):
                global e106
                e106=Label(frame15,text="username already has parked his car",font=('Helvetica 22 bold'))
                e106.place(x=600,y=450,height=30)
                window.after(800,dele106)
                foundz=True
            else:
                foundz=True
                continue
    if foundz==False:
        #saving gmail id
        mycon1=sqltor.connect(host="localhost",user='root',passwd='vrishank',database='data')
        
        #making cursor
        cursor=mycon1.cursor()

        #adding data through cursor
        cursor.execute("insert into valet value(%s,%s,%s,%s)",(username,pincode,PAC,time))
        mycon1.commit()
        global e107
        e107=Label(frame15,text="reservation done",font=('Helvetica 22 bold'))
        e107.place(x=600,y=300,height=30)
        window.after(800,dele107)

        cursor.close()
        mycon1.close()
    elif foundz==True:
        e106=Label(frame15,text="username already has parked his car",font=('Helvetica 22 bold'))
        e106.place(x=600,y=450,height=30)
        window.after(800,dele106)






    



        



#variables


#main frames(add 3 buttons one-AI one-2player and one-settings
button=Button(frame1,text="settings",width=8,height=2,bg="#afd6de",font= ('Helvetica 10 bold'),command=go_to_settings)
button.place(x=1210,y=0)

button=Button(frame1,text="sign up",width=20,height=14,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_entry)
button.place(x=700,y=100)

button=Button(frame1,text="login",width=20,height=14,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_login)
button.place(x=180,y=100)


#settings frame
button=Button(frame2,text="MUSIC",width=24,height=4,bg="#afd6de",font= ('Helvetica 25 bold'),command=play_music)
button.place(x=400,y=100)

button=Button(frame2,text="MAIN MENU",width=24,height=4,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_main_menu)
button.place(x=400,y=300)

l1=Label(frame2,text="SETTINGS",font=('Helvetica 35 bold'))
l1.place(x=510,y=30,height=37)

#signup page
button=Button(frame3,text="MAIN MENU",width=16,height=2,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_main_menu)
button.place(x=250,y=540)

l1=Label(frame3,text="username: ",font=('Helvetica 22 bold'))
l1.place(x=260,y=180,height=25)

Name=StringVar()
E1=Entry(frame3,textvariable=Name,width=40,bg="#afd6de",font= ('Helvetica 25 bold'))
E1.place(x=430,y=175)

l2=Label(frame3,text="password: ",font=('Helvetica 22 bold'))
l2.place(x=260,y=280,height=25)


password=StringVar()
E2=Entry(frame3,textvariable=password,width=40,bg="#afd6de",font= ('Helvetica 25 bold'))
E2.place(x=430,y=275)

l3=Label(frame3,text="gmail: ",font=('Helvetica 22 bold'))
l3.place(x=320,y=385,height=25)

gmail=StringVar()
E3=Entry(frame3,textvariable=gmail,width=40,bg="#afd6de",font= ('Helvetica 25 bold'))
E3.place(x=430,y=380)

button=Button(frame3,text="verification",width=16,height=2,bg="#afd6de",font= ('Helvetica 25 bold'),command=signin)
button.place(x=750,y=540)


#login
button=Button(frame4,text="MAIN MENU",width=16,height=2,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_main_menu)
button.place(x=250,y=540)

l1=Label(frame4,text="username: ",font=('Helvetica 22 bold'))
l1.place(x=260,y=250,height=25)

Name_login=StringVar()
E4=Entry(frame4,textvariable=Name_login,width=40,bg="#afd6de",font= ('Helvetica 25 bold'))
E4.place(x=430,y=245)

l2=Label(frame4,text="password: ",font=('Helvetica 22 bold'))
l2.place(x=260,y=350,height=25)

password=StringVar()
E5=Entry(frame4,textvariable=password,width=40,bg="#afd6de",font= ('Helvetica 25 bold'))
E5.place(x=430,y=345)

button=Button(frame4,text="login",width=16,height=2,bg="#afd6de",font= ('Helvetica 25 bold'),command=login_check)
button.place(x=750,y=540)

#otp
button=Button(frame5,text="MAIN MENU",width=16,height=2,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_main_menu)
button.place(x=250,y=540)

button=Button(frame5,text="verification",width=16,height=2,bg="#afd6de",font= ('Helvetica 25 bold'),command=otp_check)
button.place(x=750,y=540)

l1=Label(frame5,text="enter OTP: ",font=('Helvetica 22 bold'))
l1.place(x=260,y=375,height=25)

ote=StringVar()
E6=Entry(frame5,textvariable=ote,width=40,bg="#afd6de",font= ('Helvetica 25 bold'))
E6.place(x=430,y=370)

#functions

button=Button(frame6,text="Menu",width=12,height=10,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_drinks)
button.place(x=120,y=120)

button=Button(frame6,text="valet parking",width=12,height=10,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_parking)
button.place(x=385,y=120)

button=Button(frame6,text="Search hotels",width=12,height=10,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_pincode)
button.place(x=650,y=120)

button=Button(frame6,text="reservation",width=12,height=10,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_reservation)
button.place(x=915,y=120)

button=Button(frame6,text="<<  log out  >>",width=16,height=2,bg="#afd6de",font= ('Helvetica 27 bold'),command=go_to_main_menu)
button.place(x=460,y=540)

#go_to_pincode
l7=Label(frame10,text="current location's pincode: ",font=('Helvetica 22 bold'))
l7.place(x=40,y=250,height=25)
pincode=StringVar()
E7=Entry(frame10,textvariable=pincode,width=40,bg="#afd6de",font= ('Helvetica 25 bold'))
E7.place(x=450,y=245)

button=Button(frame10,text="confirm",width=22,height=2,bg="#afd6de",font= ('Helvetica 27 bold'),command=pincode_s)
button.place(x=450,y=420)

button=Button(frame10,text="<-- Go Back",width=22,height=2,bg="#afd6de",font= ('Helvetica 27 bold'),command=go_to_functions)
button.place(x=450,y=540)

#go_to_parking
button=Button(frame11,text="Search your Parking Details",width=24,height=3,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_parking_check)
button.place(x=400,y=50)

button=Button(frame11,text="Enter your Paking Details",width=24,height=3,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_parking_entry)
button.place(x=400,y=210)

button=Button(frame11,text="checkout",width=24,height=3,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_parking_checkout)
button.place(x=400,y=370)


button=Button(frame11,text="<-- Go Back",width=22,height=2,bg="#afd6de",font= ('Helvetica 27 bold'),command=go_to_functions)
button.place(x=400,y=540)

#go_to_reservation
button=Button(frame12,text="Verification of Reservation",width=24,height=3,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_reservation_check)
button.place(x=400,y=50)

button=Button(frame12,text="Book an Reservation",width=24,height=3,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_reservation_entry)
button.place(x=400,y=210)

button=Button(frame12,text="Checkout",width=24,height=3,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_check_out)
button.place(x=400,y=370)

button=Button(frame12,text="<-- Go Back",width=22,height=2,bg="#afd6de",font= ('Helvetica 27 bold'),command=go_to_functions)
button.place(x=400,y=540)

#the verification COULD TELL TIME OF RESERVATIO ALSO

#go to parking check frame 16
l7=Label(frame16,text="Enter your Username: ",font=('Helvetica 22 bold'))
l7.place(x=115,y=250,height=25)
pk_un=StringVar()
E8=Entry(frame16,textvariable=pk_un,width=40,bg="#afd6de",font= ('Helvetica 25 bold'))
E8.place(x=430,y=245)

button=Button(frame16,text="<-- Go Back",width=22,height=2,bg="#afd6de",font= ('Helvetica 27 bold'),command=go_to_functions)
button.place(x=400,y=540)
button=Button(frame16,text="confirm",width=22,height=2,bg="#afd6de",font= ('Helvetica 27 bold'),command=parking_search)
button.place(x=400,y=420)


#go to reservation check
l7=Label(frame14,text="Enter your pincode: ",font=('Helvetica 22 bold'))
l7.place(x=115,y=150,height=25)
r_pc=StringVar()
E18=Entry(frame14,textvariable=r_pc,width=40,bg="#afd6de",font= ('Helvetica 25 bold'))
E18.place(x=430,y=145)

l8=Label(frame14,text="Enter your Username: ",font=('Helvetica 22 bold'))
l8.place(x=115,y=250,height=25)
r_un=StringVar()
E9=Entry(frame14,textvariable=r_un,width=40,bg="#afd6de",font= ('Helvetica 25 bold'))
E9.place(x=430,y=245)

button=Button(frame14,text="<-- Go Back",width=22,height=2,bg="#afd6de",font= ('Helvetica 27 bold'),command=go_to_functions)
button.place(x=400,y=540)
button=Button(frame14,text="confirm",width=22,height=2,bg="#afd6de",font= ('Helvetica 27 bold'),command=search)
button.place(x=400,y=420)

#go to reservation entry
#need

l8=Label(frame13,text="Enter your Username: ",font=('Helvetica 22 bold'))
l8.place(x=115,y=50,height=25)
re_un=StringVar()
E10=Entry(frame13,textvariable=re_un,width=40,bg="#afd6de",font= ('Helvetica 25 bold'))
E10.place(x=430,y=45)


l9=Label(frame13,text="Enter the pincode: ",font=('Helvetica 22 bold'))
l9.place(x=150,y=145,height=25)
red_un=StringVar()
E11=Entry(frame13,textvariable=red_un,width=40,bg="#afd6de",font= ('Helvetica 25 bold'))
E11.place(x=430,y=150)


l10=Label(frame13,text="Enter the check-in date(yyyy-mm-dd): ",font=('Helvetica 17 bold'))
l10.place(x=5,y=250,height=25)
ret_un=StringVar()
E12=Entry(frame13,textvariable=ret_un,width=40,bg="#afd6de",font= ('Helvetica 25 bold'))
E12.place(x=430,y=245)

l10=Label(frame13,text="Enter the check-out date(yyyy-mm-dd): ",font=('Helvetica 17 bold'))
l10.place(x=5,y=350,height=25)
re_pc=StringVar()
E19=Entry(frame13,textvariable=re_pc,width=40,bg="#afd6de",font= ('Helvetica 25 bold'))
E19.place(x=430,y=345)

button=Button(frame13,text="confirm",width=22,height=2,bg="#afd6de",font= ('Helvetica 27 bold'),command=entry_in_hotel)
button.place(x=400,y=440)

button=Button(frame13,text="<-- Go Back",width=22,height=2,bg="#afd6de",font= ('Helvetica 27 bold'),command=go_to_functions)
button.place(x=400,y=560)


#go to parking entry
l11=Label(frame15,text="Enter your Username: ",font=('Helvetica 22 bold'))
l11.place(x=115,y=50,height=27)
pke_un=StringVar()
E13=Entry(frame15,textvariable=pke_un,width=40,bg="#afd6de",font= ('Helvetica 25 bold'))
E13.place(x=430,y=45)

l11=Label(frame15,text="Enter your pincode: ",font=('Helvetica 22 bold'))
l11.place(x=125,y=140,height=27)
pke_pc=StringVar()
E22=Entry(frame15,textvariable=pke_pc,width=40,bg="#afd6de",font= ('Helvetica 25 bold'))
E22.place(x=430,y=135)


l12=Label(frame15,text="Parking Area Code: ",font=('Helvetica 22 bold'))
l12.place(x=135,y=225,height=27)
pkes_un=StringVar()
E14=Entry(frame15,textvariable=pkes_un,width=40,bg="#afd6de",font= ('Helvetica 25 bold'))
E14.place(x=430,y=230)


l13=Label(frame15,text="Time of Parking: ",font=('Helvetica 22 bold'))
l13.place(x=160,y=315,height=27)
pket_un=StringVar()
E15=Entry(frame15,textvariable=pket_un,width=40,bg="#afd6de",font= ('Helvetica 25 bold'))
E15.place(x=430,y=320)

button=Button(frame15,text="confirm",width=22,height=2,bg="#afd6de",font= ('Helvetica 27 bold'),command=parking_entry)
button.place(x=400,y=430)

button=Button(frame15,text="<-- Go Back",width=22,height=2,bg="#afd6de",font= ('Helvetica 27 bold'),command=go_to_functions)
button.place(x=400,y=550)


#frame 7 menu
var1=IntVar()
radio1= Checkbutton(frame7,borderwidth=50,variable=var1,offvalue=0,onvalue=1,image=img1)
radio1.place(x=20,y=50)

var2=IntVar()
radio2= Checkbutton(frame7,borderwidth=50,variable=var2,offvalue=0,onvalue=1,image=img2)
radio2.place(x=270,y=50)

var3=IntVar()
radio3= Checkbutton(frame7,borderwidth=50,variable=var3,offvalue=0,onvalue=1,image=img3)
radio3.place(x=520,y=50)

var4=IntVar()
radio4= Checkbutton(frame7,borderwidth=50,variable=var4,offvalue=0,onvalue=1,image=img4)
radio4.place(x=770,y=50)

var5=IntVar()
radio5= Checkbutton(frame7,borderwidth=50,variable=var5,offvalue=0,onvalue=1,image=img5)
radio5.place(x=1020,y=50)

button=Button(frame7,text="next page -->",width=22,height=2,bg="#afd6de",font= ('Helvetica 27 bold'),command=go_to_food)
button.place(x=650,y=550)

button=Button(frame7,text="Payment",width=22,height=2,bg="#afd6de",font= ('Helvetica 27 bold'),command=go_to_final_bill)
button.place(x=370,y=430)

button=Button(frame7,text="<-- Go Back",width=22,height=2,bg="#afd6de",font= ('Helvetica 27 bold'),command=go_to_functions)
button.place(x=100,y=550)

#frame 8 menu part 2
var6=IntVar()
radio6= Checkbutton(frame8,borderwidth=50,variable=var6,offvalue=0,onvalue=1,image=img6)
radio6.place(x=20,y=90)

var7=IntVar()
radio7= Checkbutton(frame8,borderwidth=50,variable=var7,offvalue=0,onvalue=1,image=img7)
radio7.place(x=270,y=90)

var8=IntVar()
radio8= Checkbutton(frame8,borderwidth=50,variable=var8,offvalue=0,onvalue=1,image=img8)
radio8.place(x=520,y=90)

var9=IntVar()
radio9= Checkbutton(frame8,borderwidth=50,variable=var9,offvalue=0,onvalue=1,image=img9)
radio9.place(x=770,y=90)

var10=IntVar()
radio10= Checkbutton(frame8,borderwidth=50,variable=var10,offvalue=0,onvalue=1,image=img10)
radio10.place(x=1020,y=90)

button=Button(frame8,text="Payment",width=22,height=2,bg="#afd6de",font= ('Helvetica 27 bold'),command=go_to_final_bill)
button.place(x=650,y=550)

button=Button(frame8,text="<-- Go Back",width=22,height=2,bg="#afd6de",font= ('Helvetica 27 bold'),command=go_to_drinks)
button.place(x=100,y=550)


#frame9 the bill

button=Button(frame9,text="Payment confirmed",width=22,height=2,bg="#afd6de",font= ('Helvetica 27 bold'),command=go_to_functions)
button.place(x=650,y=550)

button=Button(frame9,text="<-- go back",width=22,height=2,bg="#afd6de",font= ('Helvetica 27 bold'),command=go_to_food)
button.place(x=100,y=550)

button=Button(frame9,text="Rate Us",width=22,height=2,bg="#afd6de",font= ('Helvetica 27 bold'),command=go_to_website)
button.place(x=370,y=430)

bill = StringVar()
l14=Label(frame9,text="the Amount to be paid=",font=('Helvetica 22 bold'))
l14.place(x=400,y=330,height=30)

l15=Label(frame9,textvariable = bill,font=('Helvetica 22 bold'))
l15.place(x=735,y=330,height=30)

img11=Image.open("gpay.png")
resize_img=img11.resize((225,225))
img_11=ImageTk.PhotoImage(resize_img)
ImgLabel=Label(frame9,image=img_11)
ImgLabel.img11=img_11
ImgLabel.place(x=470, y=20)

l16=Label(frame9,text="payment QR code",font=('Helvetica 22 bold'),borderwidth=2,bd=2,fg='blue')
l16.place(x=455,y=257,height=30)

#frame 17 check out
l7=Label(frame17,text="Enter your pincode: ",font=('Helvetica 22 bold'))
l7.place(x=115,y=150,height=25)
co_pc=StringVar()
E16=Entry(frame17,textvariable=co_pc,width=40,bg="#afd6de",font= ('Helvetica 25 bold'))
E16.place(x=430,y=145)

l18=Label(frame17,text="Enter your Username: ",font=('Helvetica 22 bold'))
l18.place(x=115,y=250,height=25)
co_un=StringVar()
E17=Entry(frame17,textvariable=co_un,width=40,bg="#afd6de",font= ('Helvetica 25 bold'))
E17.place(x=430,y=245)


button=Button(frame17,text="<-- Go Back",width=22,height=2,bg="#afd6de",font= ('Helvetica 27 bold'),command=go_to_functions)
button.place(x=400,y=540)
button=Button(frame17,text="CheckOut",width=22,height=2,bg="#afd6de",font= ('Helvetica 27 bold'),command=checkout)
button.place(x=400,y=420)

#frame 18 parking check out
l7=Label(frame18,text="Enter your pincode: ",font=('Helvetica 22 bold'))
l7.place(x=115,y=150,height=25)
pco_pc=StringVar()
E20=Entry(frame18,textvariable=pco_pc,width=40,bg="#afd6de",font= ('Helvetica 25 bold'))
E20.place(x=430,y=145)

l18=Label(frame18,text="Enter your Username: ",font=('Helvetica 22 bold'))
l18.place(x=115,y=250,height=25)
pco_un=StringVar()
E21=Entry(frame18,textvariable=pco_un,width=40,bg="#afd6de",font= ('Helvetica 25 bold'))
E21.place(x=430,y=245)


button=Button(frame18,text="<-- Go Back",width=22,height=2,bg="#afd6de",font= ('Helvetica 27 bold'),command=go_to_functions)
button.place(x=400,y=540)
button=Button(frame18,text="CheckOut",width=22,height=2,bg="#afd6de",font= ('Helvetica 27 bold'),command=parking_checkout)
button.place(x=400,y=420)










