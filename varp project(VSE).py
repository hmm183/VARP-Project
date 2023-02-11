import mysql.connector as sqltor
from tkinter import *
import random
import tkinter as tk
from tkinter import ttk
import winsound
from PIL import *
from PIL import Image, ImageTk
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
style=ttk.Style()
style.layout('TNotebook.Tab',[])

#variables
winsound.PlaySound('music_for_hotel.wav',winsound.SND_ASYNC  + winsound.SND_LOOP)
e=0

#commands(switch if and else before sumission)
def play_music():
    global e
    e+=1
    if e%2==0:
        ##change(e)
        winsound.PlaySound('music_for_hotel.wav',winsound.SND_ASYNC  + winsound.SND_LOOP)
    else:
        ##change(e)
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


#################images for otp
i1=Image.open("OIPF.jpeg")
resize_i1=i1.resize((250,330))
imge1=ImageTk.PhotoImage(resize_i1)
ImgLabel=Label(frame5,image=imge1)
ImgLabel.i1=imge1
ImgLabel.place(x=30, y=10)

i2=Image.open("SD.jpeg")
resize_i2=i2.resize((250,330))
imge2=ImageTk.PhotoImage(resize_i2)
ImgLabel2=Label(frame5,image=imge2)
ImgLabel2.i2=imge2
ImgLabel2.place(x=390, y=10)

i3=Image.open("CSB.jpeg")
resize_i3=i3.resize((250,330))
imge3=ImageTk.PhotoImage(resize_i3)
ImgLabel3=Label(frame5,image=imge3)
ImgLabel3.i3=imge3
ImgLabel3.place(x=660, y=10)

i4=Image.open("OISF.jpeg")
resize_i4=i4.resize((250,330))
imge4=ImageTk.PhotoImage(resize_i4)
ImgLabel4=Label(frame5,image=imge4)
ImgLabel4.i4=imge4
ImgLabel4.place(x=930, y=10)

ora=Label(frame5,text='OR',font=('LucidaConsole 35 bold'),borderwidth=2,bd=2,fg='black')
ora.place(x=300,y=120)





#################

r=1        
price=0


def go_to_main_menu():
    global r
    r+=1
    if r%10==0:
        window.after(800,rate)
    notebook.select(0)

def go_to_settings():
    global r
    r+=1
    if r%10==0:
        window.after(800,rate)
    notebook.select(1)




def go_to_entry():
    global r
    r+=1
    if r%10==0:
        window.after(800,rate)
    notebook.select(2)

def go_to_login():
    global r
    r+=1
    if r%10==0:
        window.after(800,rate)
    notebook.select(3)

def go_to_otp():
    global r
    r+=1
    if r%10==0:
        window.after(800,rate)
    notebook.select(4)

def go_to_functions():
    global r
    r+=1
    if r%10==0:
        window.after(800,rate)
    notebook.select(5)


def go_to_drinks():#6
    global r
    r+=1
    if r%10==0:
        window.after(800,rate)
    notebook.select(6)
    global price
    price=0
    bill.set(price)

def go_to_food():#7
    global r
    r+=1
    if r%10==0:
        window.after(800,rate)
    notebook.select(7)
    global price
    price=0
    bill.set(price)


def go_to_final_bill():#7
    notebook.select(8)
    global price
    if var1.get() ==1:
        price+=200
    if var2.get()==1:
        price+=190
    if var3.get()==1:
        price+=150
    if var4.get()==1:
        price+=20
    if var5.get()==1:
        price+=20
    if var6.get()==1:
        price+=200
    if var7.get()==1:
        price+=200
    if var8.get()==1:
        price+=60
    if var9.get()==1:
        price+=50
    if var10.get()==1:
        price+=25
    ##change("bill: ",price)
    bill.set(price)
        
        

def go_to_pincode():#6
    global r
    r+=1
    if r%10==0:
        window.after(800,rate)
    notebook.select(9)

def go_to_parking():#6
    global r
    r+=1
    if r%10==0:
        window.after(800,rate)
    notebook.select(10)

def go_to_website():#6
    webbrowser.open('https://cafe.synergize.co/index.php?/archives/1-Rate-Us.html')

def go_to_reservation():#6
    global r
    r+=1
    if r%10==0:
        window.after(800,rate)
    notebook.select(11)

def go_to_reservation_entry():#in 12 frame
    global r
    r+=1
    if r%10==0:
        window.after(800,rate)
    notebook.select(12)
    
def go_to_reservation_check():#in 12 frame
    global r
    r+=1
    if r%10==0:
        window.after(800,rate)
    notebook.select(13)

def go_to_parking_entry():#in 11 frame
    global r
    r+=1
    if r%10==0:
        window.after(800,rate)
    notebook.select(14)

def go_to_parking_check():#in 11 frame
    global r
    r+=1
    if r%10==0:
        window.after(800,rate)
    notebook.select(15)
def go_to_parking_checkout():#in 11 frame
    global r
    r+=1
    if r%10==0:
        window.after(800,rate)
    notebook.select(17)
def go_to_check_out():
    global r
    r+=1
    if r%10==0:
        window.after(800,rate)
    notebook.select(16)

def rate():
    window = tk.Tk()
 
    # setting attribute
    width= window.winfo_screenwidth()
    height= window.winfo_screenheight()
    #setting tkinter window size
    window.geometry("%dx%d" % (width, height))
    window.title("Rate us")
     
    # creating text label to display on window screen
    button=Button(window,text="rate us",width=20,height=3,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_website)
    button.place(x=500,y=200)

    button2=Button(window,text="close",width=20,height=3,bg="#afd6de",font= ('Helvetica 25 bold'),command=window.destroy)
    button2.place(x=500,y=500)
    
     
    window.mainloop()




def end():#17
    global r
    r+=1
    if r%10==0:
        window.after(800,rate)
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
    mycon=sqltor.connect(host="localhost",user='root',passwd='VSE@2022',database='data')

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
        E5.delete(0, END)
        
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
mycon=sqltor.connect(host="localhost",user='root',passwd='VSE@2022',database='data')


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
##change(tor)

    #ending
cursor.close()
mycon.close()
####################
def dele85():
    e85.place_forget() 
def signin():
    username=E1.get()
    password=E2.get()
    g=E3.get()
    if E1.get()=='' or E2.get()=='' or E3.get()=='':
        global e85
        e85=Label(frame3,text="details are not filled",font=('Helvetica 22 bold'),borderwidth=2,bd=2,fg='red')
        e85.place(x=600,y=300,height=30)
        window.after(800,dele85)
    else:
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
                notebook.select(4)
            

def dele86():
    e86.place_forget()

def otp_check():
    z=E6.get()
    u=str(z)
    if E6.get()=='':
        global e86
        e86=Label(frame5,text="details are not filled",font=('Helvetica 22 bold'),borderwidth=2,bd=2,fg='red')
        e86.place(x=600,y=300,height=30)
        window.after(800,dele86)
    else:
        username=E1.get()
        password=E2.get()
        g=E3.get()
        if u==n:
            window.after(400,go_to_main_menu)
            global ea3
            ea3=Label(frame5,text='sign up approved',font=('LucidaConsole 25 bold'),borderwidth=2,bd=2,fg='green')
            ea3.place(x=500,y=450)
            window.after(400,del3)
            #connection
            mycon=sqltor.connect(host="localhost",user='root',passwd='VSE@2022',database='data')

            #making cursor
            cursor=mycon.cursor()

            #adding data through cursor
            cursor.execute("insert into userdata(username,password) values(%s,%s)",(username, password))
            mycon.commit()

            #end
            cursor.close()
            mycon.close()
            #saving gmail id
            mycon1=sqltor.connect(host="localhost",user='root',passwd='VSE@2022',database='data')

            #making cursor
            cursor=mycon1.cursor()

            #adding data through cursor
            cursor.execute("insert into gmail_id(gmail) value(%s)",[g])
            mycon1.commit()

            cursor.close()
            mycon1.close()
            E1.delete(0, END)
            E2.delete(0, END)
            E3.delete(0, END)
        elif u!=n:
            global ea4
            ea4=Label(frame5,text='OTP was wrong',font=('LucidaConsole 25 bold'),borderwidth=2,bd=2,fg='red')
            ea4.place(x=500,y=450)
            window.after(800,del4)
            ##change('this',u)

def dele97():
    e97.place_forget()
def dele77():
    e77.place_forget()
def pincode_s():
    global r
    r+=1
    if r%10==0:
        window.after(800,rate)
    y=[600028,682504,303905,180006,560066]
    oz=E7.get()
    if E7.get()=='':
        global e77
        e77=Label(frame10,text="details are not filled",font=('Helvetica 22 bold'),borderwidth=2,bd=2,fg='red')
        e77.place(x=600,y=300,height=30)
        window.after(800,dele77)
    else:
        op=int(oz)
        ##change(op)
        z=[]
        for i in range(0,len(y)):
            zzzz=y[i]-op
            if zzzz>=0:
                z.append(zzzz)
            elif zzzz<=0:
                zzpos=zzzz*-1
                z.append(zzpos)
        mini=min(z)
        ##change(mini)
        ##change(y)
        pincode=op+mini
        pincode2=op-mini
        global e97
        global address
        address="https://www.google.com/maps"
        if pincode in y:
            ##change(pincode)
            pin= StringVar()
            pin.set(pincode)
            e97=Label(frame10,textvariable =pin,font=('Helvetica 22 bold'))
            e97.place(x=600,y=350,height=30)
            window.after(800,dele97)
            ea98=Label(frame10,text="this the nearest pincode",font=('LucidaConsole 25 bold'),borderwidth=2,bd=2,fg='green')
            ea98.place(x=200,y=350)
            #600028,682504,303905,180006
            if pincode==600028:
                address="https://maps.app.goo.gl/rkSiSGgxxsSP5gqB7?g_st=ic"
            elif pincode==682504:
                address="https://maps.app.goo.gl/m8uzVa4zQxiryTRF7?g_st=ic"
            elif pincode==303905:
                address="https://maps.app.goo.gl/7haCcByH2yK166xb8?g_st=ic"
            elif pincode==180006:
                address="https://maps.app.goo.gl/2xU4Kr6bKrX7oKDJ9?g_st=ic"
            elif pincode==560066:
                address="https://maps.app.goo.gl/e46EWSBcc1kg5G6M6?g_st=ic"
                
        elif pincode2 in y:
            ##change(pincode2)
            pin= StringVar()
            pin.set(pincode2)
            e97=Label(frame10,textvariable =pin,font=('Helvetica 22 bold'))
            e97.place(x=600,y=350,height=30)
            window.after(800,dele97)
            ea98=Label(frame10,text="this the nearest pincode",font=('LucidaConsole 25 bold'),borderwidth=2,bd=2,fg='green')
            ea98.place(x=200,y=350)
            if pincode2==600028:
                address="https://maps.app.goo.gl/rkSiSGgxxsSP5gqB7?g_st=ic"
            elif pincode2==682504:
                address="https://maps.app.goo.gl/m8uzVa4zQxiryTRF7?g_st=ic"
            elif pincode2==303905:
                address="https://maps.app.goo.gl/7haCcByH2yK166xb8?g_st=ic"
            elif pincode2==180006:
                address="https://maps.app.goo.gl/2xU4Kr6bKrX7oKDJ9?g_st=ic"
            elif pincode2==560066:
                address="https://maps.app.goo.gl/e46EWSBcc1kg5G6M6?g_st=ic"
                
            

def address_get():
    webbrowser.open(address)


def dele100():
    e95.place_forget()
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
def dele95():
    e95.place_forget()
def dele140():
    e140.place_forget()
def dele141():
    e141.place_forget()
def dele142():
    e142.place_forget()
def dele143():
    e143.place_forget()
def dele144():
    e144.place_forget()
def dele151():
    e151.place_forget()
def checkout():
    import mysql.connector
    import mysql.connector as sqltor


    #connection
    mycon=sqltor.connect(host="localhost",user='root',passwd='VSE@2022',database='data')

    #creating cursor
    cursor=mycon.cursor(buffered=True)
    username=E4.get()
    pincode=E16.get()
    #selecting the data
    sql = '''SELECT * from hoteld'''

    #Executing the query
    cursor.execute(sql)


    #fetching data from sql
    userdata_sql=cursor.fetchall()
    z={}

    x=userdata_sql
    ##change(x)
    y=[]
    for t in x:
        for x in t:
            y.append(x)
    w=[]
    ##change(y)
    for i in range(0,len(y),4):
        if i==len(y)-3:
            break
        else:
            q=[y[i+1],y[i+2],y[i+3]]
            p=dict(details=q,user=y[i])
            i+=2
            w.append(p)
    ##change(w)
    #ending
    cursor.close()
    mycon.close()
    foundf=False
    res={}
    #if E13==NULL or E14=Nulll or E15==nulL
    #then dont execute
    if E4.get()=='' or E16.get()=='':
        global e95
        e95=Label(frame17,text="details are not filled",font=('Helvetica 22 bold'),borderwidth=2,bd=2,fg='red')
        e95.place(x=600,y=300,height=30)
        window.after(800,dele95)
    else:
        for i in range(0,len(w)):
            res.update(w[i])
            if username== res['user']:
                if pincode in res['details']:
                    foundf=True
                else:
                    continue
            else:
                continue
        if foundf==True:
            mycon=sqltor.connect(host="localhost",user='root',passwd='VSE@2022',database='data')

            #creating cursor
            cursor=mycon.cursor(buffered=True)
            sql = 'delete from hoteld where username= '+'"'+username+'"'' and pincode='+'"'+pincode+'"'+';'
            ##change(sql)
            #Executing the query
            cursor.execute(sql)
            mycon.commit()
            cursor.close()
            mycon.close()
            global e100
            e100=Label(frame17,text="check out successful",font=('Helvetica 22 bold'),borderwidth=2,bd=2,fg='green')
            e100.place(x=600,y=300,height=30)
            window.after(800,dele100)
        elif foundf==False:
            global e102
            e102=Label(frame17,text="details invalid",font=('Helvetica 22 bold'),borderwidth=2,bd=2,fg='red')
            e102.place(x=600,y=300,height=30)
            window.after(800,dele102)
def dele542():
    ea542.place_forget()
def dele543():
    ea543.place_forget()
    
def search():
    import mysql.connector
    import mysql.connector as sqltor
    from collections import ChainMap

    #connection
    mycon=sqltor.connect(host="localhost",user='root',passwd='VSE@2022',database='data')

    #creating cursor
    cursor=mycon.cursor(buffered=True)

    #selecting the data
    sql = '''SELECT * from hoteld'''

    #Executing the query
    cursor.execute(sql)


    #fetching data from sql
    userdata_sql=cursor.fetchall()
    z={}

    x=userdata_sql
    ##change(x)
    y=[]
    for t in x:
        for x in t:
            y.append(x)
    w=[]
    ##change(y)
    for i in range(0,len(y),4):
        if i==len(y)-3:
            break
        else:
            q=[y[i+1],y[i+2],y[i+3]]
            p=dict(details=q,user=y[i])
            i+=2
            w.append(p)
    ##change(w)


    res  = {}
    pincode=E18.get()
    user=E4.get()
    foundy=x
    zz='y'
    if E18.get()=='' or E4.get()=='':
        global e140
        e140=Label(frame14,text="details are not provided",font=('Helvetica 22 bold'),borderwidth=2,bd=2,fg='red')
        e140.place(x=600,y=300,height=30)
        window.after(800,dele140)
    else:
        for i in range(0,len(w)):
            res.update(w[i])
            if user== res['user']:
                foundy=True
                zz=foundy
                if pincode in res['details']:
                    done = StringVar()
                    done.set(res['details'])
                    global e141
                    e141=Label(frame14,textvariable =done,font=('Helvetica 22 bold'),borderwidth=2,bd=2,fg='green')
                    e141.place(x=735,y=300,height=30)
                    window.after(1200,dele141)
                    foundy='t'
                    global ea542
                    ea542=Label(frame14,text='these are your details:',font=('LucidaConsole 25 bold'),borderwidth=2,bd=2,fg='green')
                    ea542.place(x=300,y=300)
                    window.after(1200,dele542)
                    break
                else:
                    pass
            elif user != res['user']:
                continue
            else:
                continue
    if foundy==True:
        global e143
        e143=Label(frame14,text="wrong pincode",font=('Helvetica 22 bold'),borderwidth=2,bd=2,fg='red')
        e143.place(x=600,y=300,height=30)
        window.after(800,dele143)
    elif foundy==False:
        global e144
        e144=Label(frame14,text="details are incorrect",font=('Helvetica 22 bold'),borderwidth=2,bd=2,fg='red')
        e144.place(x=600,y=300,height=30)
        window.after(800,dele144)
    elif zz=='y':
        if E18.get()=='' or E4.get()=='':
            pass
        else:
            global e151
            e151=Label(frame14,text="details are incorrect",font=('Helvetica 22 bold'),borderwidth=2,bd=2,fg='red')
            e151.place(x=600,y=300,height=30)
            window.after(800,dele151)
        
        
            
    #ending
    cursor.close()
    mycon.close()
    
    

def entry_in_hotel():
    import mysql.connector
    import mysql.connector as sqltor

    #connection
    mycon=sqltor.connect(host="localhost",user='root',passwd='VSE@2022',database='data')

    #creating cursor
    cursor=mycon.cursor(buffered=True)

    #selecting the data
    sql = '''SELECT * from hoteld'''

    #Executing the query
    cursor.execute(sql)


    #fetching data from sql
    userdata_sql=cursor.fetchall()
    z={}

    x=userdata_sql
    ##change(x)
    y=[]
    for t in x:
        for x in t:
            y.append(x)
    w=[]
    ##change(y)
    for i in range(0,len(y),4):
        if i==len(y)-3:
            break
        else:
            q=[y[i+1],y[i+2],y[i+3]]
            p=dict(details=q,user=y[i])
            i+=2
            w.append(p)
    ##change(w)
    #ending
    cursor.close()
    mycon.close()



    #data input
    pincode=E11.get()
    date1=E12.get()
    username=E4.get()
    date2=E19.get()
    
    res={}
    foundz=False
    if E11.get()=='' or E12.get()=='' or E4.get()=='' or E19.get()=='':
        global e121
        e121=Label(frame13,text="details are not filled",font=('Helvetica 22 bold'),borderwidth=2,bd=2,fg='red')
        e121.place(x=600,y=400,height=30)
        window.after(800,dele121)
    else:
        #if E13==NULL or E14=Nulll or E15==nulL
        #then dont execute
        for i in range(0,len(w)):
            res.update(w[i])
            if username== res['user']:
                if pincode in res['details']:
                    if i==len(w):
                        global e106
                        e106=Label(frame13,text="username has already reserved a room",font=('Helvetica 22 bold'),borderwidth=2,bd=2,fg='red')
                        e106.place(x=600,y=400,height=30)
                        window.after(800,dele106)
                        foundz=True
                    else:
                        foundz=True
                        continue
                else:
                    continue
        if foundz==False:
            #saving gmail id
            mycon1=sqltor.connect(host="localhost",user='root',passwd='VSE@2022',database='data')
            
            #making cursor
            cursor=mycon1.cursor()

            #adding data through cursor
            cursor.execute("insert into hoteld value(%s,%s,%s,%s)",(username,pincode,date1,date2))
            mycon1.commit()
            global e107
            e107=Label(frame13,text="reservation done",font=('Helvetica 22 bold'),borderwidth=2,bd=2,fg='green')
            e107.place(x=600,y=400,height=30)
            window.after(800,dele107)

            cursor.close()
            mycon1.close()
        elif foundz==True:
            e106=Label(frame13,text="username has already reserved a room",font=('Helvetica 22 bold'),borderwidth=2,bd=2,fg='red')
            e106.place(x=600,y=400,height=30)
            window.after(800,dele106)
    
def dele108():
    e108.place_forget()
def dele109():
    e109.place_forget()
def dele110():
    e110.place_forget()

##################parking checkout is below###############################################
def parking_checkout():#frame 17 check out
    import mysql.connector
    import mysql.connector as sqltor


    #connection
    mycon=sqltor.connect(host="localhost",user='root',passwd='VSE@2022',database='data')

    #creating cursor
    cursor=mycon.cursor(buffered=True)
    username=E4.get()
    pincode=E20.get()
    #selecting the data
    sql = '''SELECT * from valet'''

    #Executing the query
    cursor.execute(sql)


    #fetching data from sql
    userdata_sql=cursor.fetchall()
    z={}

    x=userdata_sql
    ##change(x)
    y=[]
    for t in x:
        for x in t:
            y.append(x)
    w=[]
    ##change(y)
    for i in range(0,len(y),4):
        if i==len(y)-3:
            break
        else:
            q=[y[i+1],y[i+2],y[i+3]]
            p=dict(details=q,user=y[i])
            i+=2
            w.append(p)
    ##change(w)
    #ending
    cursor.close()
    mycon.close()
    foundf=False
    res={}
    #if E13==NULL or E14=Nulll or E15==nulL
    #then dont execute
    if E20.get()=='' or E4.get()=='':
        global e110
        e110=Label(frame18,text="details are not filled",font=('Helvetica 22 bold'),borderwidth=2,bd=2,fg='red')
        e110.place(x=600,y=300,height=30)
        window.after(800,dele110)
    else:
        for i in range(0,len(w)):
            res.update(w[i])
            if username== res['user']:
                if pincode in res['details']:
                    foundf=True
                else:
                    continue
            else:
                continue
        if foundf==True:
            mycon=sqltor.connect(host="localhost",user='root',passwd='VSE@2022',database='data')

            #creating cursor
            cursor=mycon.cursor(buffered=True)
            sql = 'delete from valet where username= '+'"'+username+'"'' and pincode='+'"'+pincode+'"'+';'
            ##change(sql)
            #Executing the query
            cursor.execute(sql)
            mycon.commit()
            cursor.close()
            mycon.close()
            global e109
            e109=Label(frame18,text="checkout complete",font=('Helvetica 22 bold'),borderwidth=2,bd=2,fg='green')
            e109.place(x=600,y=300,height=30)
            window.after(800,dele109)
        elif foundf==False:
            global e108
            e108=Label(frame18,text="username not found in this pincode",font=('Helvetica 22 bold'),borderwidth=2,bd=2,fg='red')
            e108.place(x=600,y=300,height=30)
            window.after(800,dele108)
##############checkout is above####################
    

def dele99():
    e99.place_forget()
def dele122():
    e122.place_forget()
def dele123():
    e123.place_forget()
def dele125():
    e125.place_forget()
def dele126():
    e126.place_forget()

##################parking search is below#####################
def parking_search():
    import mysql.connector
    import mysql.connector as sqltor
    from collections import ChainMap

    #connection
    mycon=sqltor.connect(host="localhost",user='root',passwd='VSE@2022',database='data')

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
    ##change(x)
    y=[]
    for t in x:
        for x in t:
            y.append(x)
    w=[]
    ##change(y)
    for i in range(0,len(y),4):
        if i==len(y)-3:
            break
        else:
            q=[y[i+1],y[i+2],y[i+3]]
            p=dict(details=q,user=y[i])
            i+=2
            w.append(p)
    ##change(w)


    res  = {}
    user=E4.get()
    pincode=E30.get()
    foundy='x'
    if E4.get()=='' or E30.get()=='':
        global e122
        e122=Label(frame16,text="details are not provided",font=('Helvetica 22 bold'),borderwidth=2,bd=2,fg='red')
        e122.place(x=600,y=300,height=30)
        window.after(800,dele122)
    else:
        for i in range(0,len(w)):
            res.update(w[i])
            if user== res['user']:
                foundy=True
                if pincode in res['details']:
                    done = StringVar()
                    done.set(res['details'])
                    global e99
                    e99=Label(frame16,textvariable =done,font=('Helvetica 22 bold'),borderwidth=2,bd=2,fg='green')
                    e99.place(x=735,y=300,height=30)
                    window.after(1200,dele99)
                    global ea543
                    ea543=Label(frame16,text='these are your details:',font=('LucidaConsole 25 bold'),borderwidth=2,bd=2,fg='green')
                    ea543.place(x=300,y=300)
                    window.after(1200,dele543)
                    foundy='z'
                    break
                else:
                    pass
            elif user != res['user']:
                continue
            else:
                continue
    if foundy==True:
        global e126
        e126=Label(frame16,text="wrong pincode",font=('Helvetica 22 bold'),borderwidth=2,bd=2,fg='red')
        e126.place(x=600,y=300,height=30)
        window.after(800,dele126)
    elif foundy=='x':
        global e123
        e123=Label(frame16,text="details are incorrect",font=('Helvetica 22 bold'),borderwidth=2,bd=2,fg='red')
        e123.place(x=600,y=300,height=30)
        window.after(800,dele123)
            
    #ending
    cursor.close()
    mycon.close()

#########################parking search is above##############################
def dele106():
    e106.place_forget()
def dele107():
    e107.place_forget()
def dele121():
    e121.place_forget()
##############################parking entry is below####################################
def parking_entry():
    import mysql.connector
    import mysql.connector as sqltor
    import mysql.connector
    import mysql.connector as sqltor
    from collections import ChainMap

    #connection
    mycon=sqltor.connect(host="localhost",user='root',passwd='VSE@2022',database='data')

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
    ##change(x)
    y=[]
    for t in x:
        for x in t:
            y.append(x)
    w=[]
    ##change(y)
    for i in range(0,len(y),4):
        if i==len(y)-3:
            break
        else:
            q=[y[i+1],y[i+2],y[i+3]]
            p=dict(details=q,user=y[i])
            i+=2
            w.append(p)
    ##change(w)
    #ending
    cursor.close()
    mycon.close()



    #data input
    username=E4.get()
    pincode=E22.get()
    PAC=E14.get()
    time=E15.get()
    res={}
    foundz=False
    if E4.get()=='' or E14.get()=='' or E15.get()=='' or E22.get()=='':
        global e121
        e121=Label(frame15,text="details are not filled",font=('Helvetica 22 bold'),borderwidth=2,bd=2,fg='red')
        e121.place(x=600,y=300,height=30)
        window.after(800,dele121)
    else:
        #if E13==NULL or E14=Nulll or E15==nulL
        #then dont execute
        for i in range(0,len(w)):
            res.update(w[i])
            if username== res['user']:
                if pincode in res['details']:
                    if i==len(w):
                        global e106
                        e106=Label(frame15,text="username already has parked his car",font=('Helvetica 22 bold'),borderwidth=2,bd=2,fg='red')
                        e106.place(x=600,y=450,height=30)
                        window.after(800,dele106)
                        foundz=True
                    else:
                        foundz=True
                        continue
                else:
                    continue
        if foundz==False:
            #saving gmail id
            mycon1=sqltor.connect(host="localhost",user='root',passwd='VSE@2022',database='data')
            
            #making cursor
            cursor=mycon1.cursor()

            #adding data through cursor
            cursor.execute("insert into valet value(%s,%s,%s,%s)",(username,pincode,PAC,time))
            mycon1.commit()
            global e107
            e107=Label(frame15,text="reservation done",font=('Helvetica 22 bold'),borderwidth=2,bd=2,fg='green')
            e107.place(x=600,y=300,height=30)
            window.after(800,dele107)

            cursor.close()
            mycon1.close()
        elif foundz==True:
            e106=Label(frame15,text="username already has parked his car",font=('Helvetica 22 bold'),borderwidth=2,bd=2,fg='red')
            e106.place(x=600,y=450,height=30)
            window.after(800,dele106)
########################parking entry is above#######################################
####################payment####################

def dele72():
    e72.place_forget()
def dele73():
    e73.place_forget()

def payment():
    global price
    if price==0:
        global e72
        e72=Label(frame9,text="No Items Selected",font=('Helvetica 22 bold'),borderwidth=2,bd=2,fg='red')
        e72.place(x=600,y=300,height=30)
        window.after(800,dele72)
    else:
        import mysql.connector
        import mysql.connector as sqltor
        from collections import ChainMap

        #connection
        mycon=sqltor.connect(host="localhost",user='root',passwd='VSE@2022',database='data')
        prices=str(price)
        #creating cursor
        cursor=mycon.cursor(buffered=True)
        #selecting the data
        cursor.execute("insert into sales value("+prices+")")
        mycon.commit()
        cursor.close()
        mycon.close()
        global e73
        e73=Label(frame9,text="payment done",font=('Helvetica 22 bold'),borderwidth=2,bd=2,fg='green')
        e73.place(x=600,y=300,height=30)
        window.after(800,dele73)
        notebook.select(5)
        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
        var5.set(0)
        var6.set(0)
        var7.set(0)
        var8.set(0)
        var9.set(0)
        var10.set(0)
        price=0
        bill.set(price)

def logout():
    E1.delete(0, END)
    E2.delete(0, END)
    E3.delete(0, END)
    E4.delete(0, END)
    E5.delete(0, END)
    E6.delete(0, END)
    E7.delete(0, END)
    E30.delete(0, END)
    E18.delete(0, END)
    E11.delete(0, END)
    E12.delete(0, END)
    E19.delete(0, END)
    E22.delete(0, END)
    E14.delete(0, END)
    E15.delete(0, END)
    E16.delete(0, END)
    E20.delete(0, END)
    notebook.select(0)





    



        



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

#menu text
l199=Label(frame7,text="PAGE 1",font=('Helvetica 40 bold'))
l199.place(x=20,y=5,height=50)

l299=Label(frame8,text="PAGE 2",font=('Helvetica 40 bold'))
l299.place(x=20,y=5,height=50)



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

button=Button(frame6,text="<<  log out  >>",width=16,height=2,bg="#afd6de",font= ('Helvetica 27 bold'),command=logout)
button.place(x=460,y=540)

button=Button(frame6,text="settings",width=8,height=2,bg="#afd6de",font= ('Helvetica 10 bold'),command=go_to_settings)
button.place(x=1210,y=0)

#go_to_pincode
l7=Label(frame10,text="current location's pincode: ",font=('Helvetica 22 bold'))
l7.place(x=40,y=250,height=25)
pincode=StringVar()
E7=Entry(frame10,textvariable=pincode,width=40,bg="#afd6de",font= ('Helvetica 25 bold'))
E7.place(x=450,y=245)

button=Button(frame10,text="confirm",width=17,height=2,bg="#afd6de",font= ('Helvetica 27 bold'),command=pincode_s)
button.place(x=50,y=540)

button=Button(frame10,text="<-- Go Back",width=17,height=2,bg="#afd6de",font= ('Helvetica 27 bold'),command=go_to_functions)
button.place(x=450,y=540)

button=Button(frame10,text="directions",width=17,height=2,bg="#afd6de",font= ('Helvetica 27 bold'),command=address_get)
button.place(x=850,y=540)

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




l71=Label(frame16,text="Enter your pincode: ",font=('Helvetica 22 bold'))
l71.place(x=115,y=250,height=25)
pkc_pc=StringVar()
E30=Entry(frame16,textvariable=pkc_pc,width=40,bg="#afd6de",font= ('Helvetica 25 bold'))
E30.place(x=430,y=245)

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



button=Button(frame14,text="<-- Go Back",width=22,height=2,bg="#afd6de",font= ('Helvetica 27 bold'),command=go_to_functions)
button.place(x=400,y=540)
button=Button(frame14,text="confirm",width=22,height=2,bg="#afd6de",font= ('Helvetica 27 bold'),command=search)
button.place(x=400,y=420)

#go to reservation entry
#need




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

button=Button(frame9,text="Payment confirmed",width=22,height=2,bg="#afd6de",font= ('Helvetica 27 bold'),command=payment)
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



button=Button(frame18,text="<-- Go Back",width=22,height=2,bg="#afd6de",font= ('Helvetica 27 bold'),command=go_to_functions)
button.place(x=400,y=540)
button=Button(frame18,text="CheckOut",width=22,height=2,bg="#afd6de",font= ('Helvetica 27 bold'),command=parking_checkout)
button.place(x=400,y=420)










