import tkinter
from tkinter import ttk
from tkinter import messagebox
def enter_data():
     accepted=accept_var.get()

     if accepted=="accepted":
      firstname=first_name_entry.get()
      lastname=last_name_entry.get() 

      if firstname and lastname:
        title=title_combobox.get()
        age=age_spinbox.get()
        nationality=nationality_combobox.get()

        registration_status= reg_status_var.get()

        print("first name:",firstname,"last name:", lastname)
        print("Title:",title,"age:", age, "nationality", nationality)
        print("registration status",registration_status)  
      else:
         tkinter.messagebox.showwarning(title="error",message="first name or last name is missing")
     else:
       tkinter.messagebox.showwarning(title="error",message="You have not accepted the terms")

win=tkinter.Tk()

win.title('Registration form')
win.geometry("700x500")
frame= tkinter.Frame(win)
frame.pack()

user_info_frame=tkinter.LabelFrame(frame,text="user information",bg='light grey')
user_info_frame.grid(row=0,column=0,padx=20,pady=20)

first_name_label= tkinter.Label(user_info_frame,text="first name")
first_name_label.grid(row=0,column=0)
last_name_label=tkinter.Label(user_info_frame,text="last name")
last_name_label.grid(row=0,column=1)

first_name_entry=tkinter.Entry(user_info_frame)
last_name_entry=tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1,column=0)
last_name_entry.grid(row=1,column=1)

title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms.", "Dr."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label =tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=5, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label=tkinter.Label(user_info_frame,text="Nationality")
nationality_combobox=ttk.Combobox(user_info_frame,values=['Africa',"America",'europe','indian','pakistan','china'])
nationality_label.grid(row=2,column=1)
nationality_combobox.grid(row=3,column=1)
v=tkinter.IntVar()
radio_label=tkinter.Label(user_info_frame,text="Gender")
radio_var=v

radio=tkinter.Radiobutton(user_info_frame, text='Male', variable=v, value=1).grid(row=3,column=3)
radio=tkinter.Radiobutton(user_info_frame, text='Female', variable=v, value=2).grid (row=3,column=2)
radio=tkinter.Radiobutton(user_info_frame, text='Other', variable=v, value=3).grid (row=3,column=4)
radio_label.grid(row=2,column=3 )

for wigdet in user_info_frame.winfo_children():
    wigdet.grid_configure(padx=10,pady=5)

courses_frame=tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registered_label= tkinter.Label(courses_frame, text="Registration Status",bg='light grey')

reg_status_var=tkinter.StringVar(value="not registered")
registered_check=tkinter.Checkbutton(courses_frame, text="Currently Registered" , variable=reg_status_var,onvalue="registered",offvalue="not registered")


registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numcourses_label =tkinter.Label(courses_frame, text="# Completed Courses")
numcourses_spinbox=tkinter. Spinbox (courses_frame, from_= 0, to='infinity')
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label=tkinter.Label(courses_frame, text="# Semesters")  
numsemesters_spinbox=tkinter. Spinbox (courses_frame, from_=0, to="infinity")
numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
     widget.grid_configure (padx=10, pady=5)

terms_frame = tkinter.LabelFrame (frame, text="Terms & Conditions",bg='light grey') 
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=20)

accept_var=tkinter.StringVar(value="not accepted")
terms_check= tkinter.Checkbutton(terms_frame, text ="I accept the terms and conditions.",variable=accept_var,onvalue="accepted", offvalue="not accepted")

terms_check.grid(row=0, column=0)
#Button
button=tkinter.Button(frame, text="Enter data",command=enter_data,bg='rosybrown') 
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

win.mainloop() 