import customtkinter
from customtkinter import *
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as tb
import re
import serial
import time
import shutil
import datetime
import pandas as pd
import serial.tools.list_ports
from threading import Thread
from PIL import ImageTk, Image
import asyncio
import os
import string


async def loading():
 p = CTkProgressBar(win, mode="indeterminate")
 p.pack(side=BOTTOM)

 for i in range(10):
  p.start()
  win.update()
  time.sleep(0.02)

  p.update_idletasks()



async def splash():
 global arduino
 global win
 win=Tk()
 win.configure(background="#E5FDEF")
 win.geometry("750x190")
 win.eval('tk::PlaceWindow . center')
 win.overrideredirect(True)

 image=PhotoImage(file="ss.png")
 labb=Label(win,image=image)
 labb.pack()

 lab_ser=CTkLabel(win,text="detecting port .....",font=("",16))
 lab_ser.pack(side=BOTTOM)




 for i in range(10):
  port="COM"+str(i)
  time.sleep(0.3)
  await loading()

  try:
   global arduino
   arduino = serial.Serial(port=port, baudrate=9600, timeout=0.3)
  except :

   continue

 ports = serial.tools.list_ports.comports()



 for p in ports:
  with open("temp.txt","w") as d:
   d.write(p.description)
 with open("temp.txt","r+") as dd:
  ss=dd.readline()
  if "CH340" not in ss:
    root = Tk()
    root.overrideredirect(1)
    root.withdraw()
    messagebox.showerror("Error", "error no port detected please make sure you connect the reader to your pc")
    exit()
  else:
   win.destroy()

asyncio.run(splash())
window = tb.window.Window(title="CLOGIN")
window.iconbitmap("icon.ico")
frame_image = Frame(window, borderwidth=2, bg="white", relief=SUNKEN)
frame_image.pack(side=TOP, fill="x")






def dark():
 if dark.config('text')[-1] == 'darkly':
  dark.config(text='cosmo')
  tb.Style("cosmo")


 else:

  dark.config(text='darkly')
  tb.Style("darkly")
  list.configure(bg="black")
  label.configure(fg_color="white")


ima=PhotoImage(file="theme.png")

dark=Button(window,text="cosmo",font=("",12),command=dark,image=ima)
dark.pack(anchor=NE)



def in_prograss():
 global df
 global my_img
 global image2
 global image

 t1="q"

 while True:
  col = 0



  data1 = arduino.readline()
  df = pd.read_csv("info.csv", sep=",")


  if re.findall(r'\d+', str(data1.decode())):

   laaa.configure(text="")
   with open("temp2.txt","a") as ee:
    ee.write("\n"+str(data1.decode())[0:-2])
   #print(df[df["id"] == str(data1)])
   list.insert(END, str(df[df["id"] == str(data1.decode())[0:-2]])[37::]+"      "+str(datetime.datetime.now())[0:-10])
   if str(str(df[df["id"] == str(data1.decode())[0:-2]]))[0]=="E":
    list.insert(END,"No ID ..............")
    messagebox.showerror("Error","No ID found for this card")


   rea = pd.read_csv("info.csv")


   if str(data1.decode())[0:-2] in rea.to_string():


    try:
     col = col + 1
     print(string.ascii_letters)




     t= Image.open("images\\"+str(data1.decode()[0:-2]+str(".jpg")))

     image2 = t.resize((130, 130), Image.ANTIALIAS)
     my_img = ImageTk.PhotoImage(image2)

     frame_image.picture = my_img
     frame_image.label = Label(frame_image, image=frame_image.picture)
     frame_image.label.grid(row=1,column=col)





     def showSelected(event):
      global temp
      for sa in list.curselection():
       temp = str(list.get(sa))
       print("temp====" + str(temp)[-33:-22])
      frame_image.label.pack_forget()


      print("ok")
      try:

       image = Image.open("images\\" + str(temp[-33:-22]+ str(".jpg")))
       image2 = image.resize((130, 130), Image.ANTIALIAS)
       my_img = ImageTk.PhotoImage(image2)

       frame_image.picture=my_img
       frame_image.label = Label(frame_image, image=frame_image.picture)
       frame_image.label.grid(row=1,column=col)

      except FileNotFoundError:

       image = Image.open("images\\" + str(temp[-31:-22] + str(".jpg")))

       image2 = image.resize((130, 130), Image.ANTIALIAS)
       my_img = ImageTk.PhotoImage(image2)

       frame_image.picture = my_img
       frame_image.label = Label(frame_image, image=frame_image.picture)
       frame_image.label.grid(row=1,column=col)




     list.bind('<<ListboxSelect>>', showSelected)

    except:

     imagen = Image.open("images\\" + "no-photo.png")

     image2 = imagen.resize((130, 130), Image.ANTIALIAS)
     my_img = ImageTk.PhotoImage(image2)

     frame_image.picture = my_img
     frame_image.label = Label(frame_image, image=frame_image.picture)
     frame_image.label.pack(side=LEFT)



















def main_window():
 global list
 global laaa
 global label

 dark.pack(anchor=NE)


 window.geometry("900x660")


 def reading():

  list.destroy()
  button.destroy()
  laaa.destroy()
  dark.pack_forget()
  try:
   frame_image.pack_forget()
  except:




   window.geometry("800x600")


  window.geometry("920x600")

  label = CTkLabel(window, text="please pass the card at the reader and press Scan",font=("",14,"bold"))
  label.pack(side=TOP)
  if dark.config('text')[-1] == 'cosmo':
   label.configure(bg_color="white")
  else:
   label.configure(text_color="white")






  def sign():
   import re
   global lab_name
   global enter_name
   global lab_job
   global enter_job
   global lab_job2
   global enter_job2
   global back
   global b_submit
   global l_id
   global des
   global B_pic
   global button
   global file
   global e12
   label.configure(text="scanning")
   c=0





   while True:
     c+=1
     point="."*c
     label.configure(text="scanning"+point)
     if c==6:
      c=0

     window.update_idletasks()
     time.sleep(0.2)
     data = arduino.readall()
     print(data.decode())


     if len(data.decode()[0:-2])>8:
      break





     else:
      if len(data.decode()[0:-2])==8 or len(data.decode()[0:-2])==7 or len(data.decode()[0:-2])==5:
       inv=CTkLabel(window,text="invalid card please try again..")
       inv.configure(text_color="red")
      continue



   csv=pd.read_csv("info.csv")
   imgz = Image.open("images\\no-photo.png")
   imgz = imgz.resize((140, 140))
   imgz = ImageTk.PhotoImage(imgz)
   e12 = Label(window)
   e12.image=imgz
   e12['image']=imgz
   e12.pack(anchor=CENTER)

   if str(data.decode())[0:-2] in csv.to_string():
    result = messagebox.askyesno("ID info", "the ID is already used do you want to change it ?")

    if result is True:
     dfa = csv.drop(csv[csv.id == str(data.decode())[0:-2]].index)
     dfa.to_csv('info.csv', index=False)

     label.configure(text="ID: " + str(data.decode())[0:-2], font=("", 18, "bold"))
     check.destroy()

     enter_name = tb.Entry(window, font=("", 15, "bold"), bootstyle="info")
     lab_name = CTkLabel(window, text="Name  ", font=("", 17))
     lab_name.pack(side=LEFT)
     enter_name.pack(side=LEFT)
     lab_job = CTkLabel(window, text="Job  ", font=("", 17))
     lab_job.pack(side=LEFT, ipadx=10, ipady=6)
     enter_job = tb.Entry(window, font=("", 15, "bold"), bootstyle="info")
     enter_job.pack(side=LEFT)

     if dark.config('text')[-1] == 'cosmo':
      lab_name.configure(text_color="black")
      aqw1 = tb.Style()
      aqw1.configure('custom.TEntry', foreground='black')
      enter_name.configure(style="custom.TEntry")
      enter_job.configure(style="custom.TEntry")

     else:

      lab_name.configure(text_color="white")
      lab_job.configure(text_color="white")
      aqw = tb.Style()
      aqw.configure('custom.TEntry', foreground='white')
      enter_name.configure(style="custom.TEntry")
      enter_job.configure(style="custom.TEntry")

     def open_file():
      global file2
      file2 = filedialog.askopenfile(mode='r', filetypes=(("image files",('*.jpg')), ("All Files", "*.*")))
      imgz2 = Image.open(file)
      imgz2 = imgz2.resize((140, 140))
      imgz2 = ImageTk.PhotoImage(imgz2)
      e12.image = imgz2
      e12['image'] = imgz2

     B_pic=CTkButton(master=window,text="add picture",font=("", 15, "bold"),command=open_file)
     B_pic.pack(side=RIGHT)



     def submit():
      global dframe

      if enter_name.get() == "":
       messagebox.showinfo("Name", "please Enter Name before click submit")
      else:
       des = str("images\\" + str(data.decode())[0:-2] + str(".jpg"))
       print(des)
       try:

        shutil.copy(file.name, des)
        df_1 = pd.read_csv("info.csv")

        dict = {"name": [enter_name.get() + str("    ")], "job": [enter_job.get() + str("   ")],
                "id": [str(data.decode())[0:-2]]}

        df_2 = pd.DataFrame(dict)

        new_df = pd.concat([df_1, df_2], axis=0)

        new_df.to_csv("info.csv", index=False)
        messagebox.showinfo("Restart", "you need to restart program to save your information")
        window.destroy()
        os.system("python main.py")
       except:
        df_1 = pd.read_csv("info.csv")
        da = arduino.readlines()

        dict = {"name": [enter_name.get() + str("    ")], "job": [enter_job.get() + str("   ")],
                "id": [str(data.decode())[0:-2]]}

        df_2 = pd.DataFrame(dict)

        new_df = pd.concat([df_1, df_2], axis=0)

        new_df.to_csv("info.csv", index=False)
        messagebox.showinfo("Restart", "you need to restart program to save your information")
        window.destroy()
        os.system("clogin.exe")



     style = tb.Style()
     style.configure("success.TButton", font=(" ", 14, "bold"))

     b_submit = tb.Button(window, text="submit", command=submit, bootstyle="success", width=10, style="success.TButton")
     b_submit.pack(side=BOTTOM,pady=10)



    elif result is False:
     main_window()
     check.pack_forget()
     label.pack_forget()
     b_back.pack_forget()
     e12.destroy()



   else:


    label.configure(text="ID: " + str(data.decode()[0:-2]), font=("", 18, "bold"))
    check.destroy()

    enter_name = tb.Entry(window,font=("",15,"bold"),bootstyle="info")
    lab_name = CTkLabel(window, text="Name  ", font=("", 17))
    lab_name.pack(side=LEFT)
    enter_name.pack(side=LEFT)

    lab_job = CTkLabel(window, text="Job  ", font=("", 17))
    lab_job.pack(side=LEFT, ipadx=10, ipady=6)
    enter_job = tb.Entry(window, font=("", 15, "bold"), bootstyle="info")
    enter_job.pack(side=LEFT)

    if dark.config('text')[-1] == 'cosmo':
     lab_name.configure(text_color="black")
     aqw1 = tb.Style()
     aqw1.configure('custom.TEntry', foreground='black')
     enter_name.configure(style="custom.TEntry")
     enter_job.configure(style="custom.TEntry")

    else:


     lab_name.configure(text_color="white")
     lab_job.configure(text_color="white")
     aqw = tb.Style()
     aqw.configure('custom.TEntry', foreground='white')
     enter_name.configure(style="custom.TEntry")
     enter_job.configure(style="custom.TEntry")

    def open_file():
     global file
     global z


     file = filedialog.askopenfilename(
                                   filetypes=(("image files",('*.jpg')), ("All Files", "*.*")))


     imgz2=Image.open(file)
     imgz2=imgz2.resize((140,140))
     imgz2=ImageTk.PhotoImage(imgz2)
     e12.image=imgz2
     e12['image']=imgz2









    B_pic = CTkButton(master=window, text="add picture", font=("", 15, "bold"), command=open_file)
    B_pic.pack(side=RIGHT)







    def submit():
     global dframe
     global des

     if enter_name.get()=="":

       messagebox.showinfo("Name","please select Name before click submit")
     else:
       des=str("images\\"+str(data.decode())[0:-2]+str(".jpg"))
       print(des)
       try:



        shutil.copy(file,des)
        df_1 = pd.read_csv("info.csv")


        dict = {"name": [enter_name.get() + str("    ")], "job": [enter_job.get() + str("   ")],
                "id": [str(data.decode())[0:-2]]}

        df_2 = pd.DataFrame(dict)

        new_df = pd.concat([df_1, df_2], axis=0)

        new_df.to_csv("info.csv", index=False)
        messagebox.showinfo("Restart", "you need to restart program to save your information")
        window.destroy()
        os.system("python main.py")
       except:
        df_1 = pd.read_csv("info.csv")
        da=arduino.readlines()

        dict = {"name": [enter_name.get()+str("    ")],"job":[enter_job.get()+str("   ")],"id":[str(data.decode())[0:-2]]                                      }

        df_2 = pd.DataFrame(dict)

        new_df = pd.concat([df_1, df_2], axis=0)

        new_df.to_csv("info.csv", index=False)
        messagebox.showinfo("Restart","you need to restart program to save your information")
        window.destroy()
        os.system("clogin.exe")




    style=tb.Style()
    style.configure("success.TButton",font=(" ",14,"bold"))

    b_submit=tb.Button(window,text="submit",command=submit,bootstyle="success",width=12,style="success.TButton")
    #b_submit.place(x=330,y=500)
    b_submit.pack(side=BOTTOM,pady=10)



  check = CTkButton(window, text="Scan", command=sign,font=("",15,"bold"))
  check.pack(anchor=CENTER)

  def back():

   check.pack_forget()
   label.pack_forget()
   b_back.pack_forget()
   label.pack_forget()
   b_back.pack_forget()
   e12.pack_forget()



   try:
    b_submit.destroy()
    B_pic.pack_forget()
    enter_name.pack_forget()
    enter_job.pack_forget()
    lab_name.pack_forget()
    lab_job.pack_forget()
    lab_job2.pack_forget()
    e12.destroy()

   except:
    main_window()
   else:
    main_window()






  b_back = CTkButton(window, text="back", command=back,font=("",15))
  b_back.pack(side=BOTTOM, fill=BOTH)

 var = StringVar(value=dir())
 list=Listbox(master=window, listvariable=var,selectmode='extended')
 list.configure(bg="#E5E7E9",height=14,width=132,font=("", 16))

 list.pack(side=TOP,fill="x")



 if list.get(1)=="":
  laaa=CTkLabel(window,text=".....No sign in yet.....",font=("",16))
  laaa.pack()
 image_user=PhotoImage(file="user-plus.png")

 button=CTkButton(window,text="add new user",command=reading,image=image_user,font=("",15))
 button.pack(side=BOTTOM)



if __name__ == '__main__':

    a = Thread(target = main_window)
    b = Thread(target = in_prograss)
    a.start()
    b.start()


    window.mainloop()