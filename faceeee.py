import tkinter as tk
from tkinter import font
import git
"""def fname():
    name=entry_name.get()
    if name:
        conn=sqlite3.Connect('face.db')
        c=conn.Cursor()
        c.execute(create table if not exists na
                  .me)(firstname_char(50),lastname_char(50),mobile_varchar(255),Password_varchar(255),Gender_char(50),DOB_varchar(255))
        c.execute(insert into firstname(""),lastname_char(50),mobile_varchar(255),Password_varchar(255),Gender_char(50),DOB_varchar(255))"""
def gender():
    selected_option=radio_var.get()
def drop(selection):
    print(selection)

"""def save():
    name=entry_name.get()
    if name.strip()=="":
        messagebox.showerror("Error")
        return
    wb=Workbook()
    ws=wb.active
    ws.append(["m","ew","re","rt","jh","kj"])
    ws.append([name,entry_name.get(),entrylast.get(),entrymob.get(),entrypass.get(),radio_male.get(),radio_female.get(),option1.get(),option2.get(),option3.get()])
    wb.save("data.xlsx")

    messagebox.showinfo("Your Data is saved")"""

    
root=tk.Tk()
root.title("FACEBOOK")
root.geometry("600x200")
root.configure(bg="white",highlightcolor="white",relief="solid")

drop_label=tk.Label(root)
drop_labels=tk.Label(root)
drop_labe=tk.Label(root)


options=['Date',1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
optionss=['Month','January','February','March','April','May','June','July','August']
optio=['Year',1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011]

option1=tk.StringVar(root)
option2=tk.StringVar(root)
option3=tk.StringVar(root)


option1.set(options[0])
option2.set(optionss[0])
option3.set(optio[0])


option_menu=tk.OptionMenu(root,option1,*options,command=drop)
option_men=tk.OptionMenu(root,option2,*optionss,command=drop)
optio_men=tk.OptionMenu(root,option3,*optio,command=drop)

label_font=font.Font(weight="bold",size=10)
option_menu.configure(bg="white",font=label_font)

label_font=font.Font(weight="bold",size=10)
option_men.configure(bg="white",font=label_font)

label_font=font.Font(weight="bold",size=10)
optio_men.configure(bg="white",font=label_font)

option_menu.grid(row=8,column=2)
option_men.grid(row=8,column=3)
optio_men.grid(row=8,column=4)

label_font=font.Font(weight="bold",size=20)
labelsign=tk.Label(root,text="Sign Up",bg="white",font=label_font)

label_font=font.Font(weight="bold",size=15)
labelsig=tk.Label(root,text="It's quick and easy.",bg="white")
labelsign.grid(row=0,column=1)
labelsig.grid(row=2,column=1)

label_font=font.Font(weight="bold",size=10)
labelfull=tk.Label(root,text="First name",bg="white",font=label_font)
labelfull.grid(row=3,column=1)
entry_name=tk.Entry(root,width=20,highlightthickness=4)
entry_name.grid(row=3,column=2)

label_font=font.Font(weight="bold",size=10)
labellast=tk.Label(root,text="Surname",bg="white",font=label_font)
labellast.grid(row=3,column=3)
entrylast=tk.Entry(root,width=20,highlightthickness=4)
entrylast.grid(row=3,column=4,padx=5,pady=5)

label_font=font.Font(weight="bold",size=10)
labelmob=tk.Label(root,text="Mobile number or E-mail address",bg="white",font=label_font)
labelmob.grid(row=5,column=1)
entrymob=tk.Entry(root,width=20,highlightthickness=4)
entrymob.grid(row=5,column=2,padx=5,pady=5)

label_font=font.Font(weight="bold",size=10)
labelpass=tk.Label(root,text="New Password",bg="white",font=label_font)
labelpass.grid(row=6,column=1)
entrypass=tk.Entry(root,width=20,highlightthickness=4)
entrypass.grid(row=6,column=2,padx=5,pady=5)

label_font=font.Font(weight="bold",size=10)
labelgen=tk.Label(root,text="Gender",bg="white",font=label_font)
labelgen.grid(row=7,column=1)
radio_var=tk.StringVar(value=0)
radio_male=tk.Radiobutton(root,highlightthickness=4,text="Male",variable=radio_var,value="Male",command=gender,bg="white",font=label_font)
radio_male.grid(row=7,column=2)

label_font=font.Font(weight="bold",size=10)
radio_female=tk.Radiobutton(root,highlightthickness=4,text="Female",variable=radio_var,value="Female",command=gender,bg="white",font=label_font)
radio_female.grid(row=7,column=3)

label_font=font.Font(weight="bold",size=10)
labelpass=tk.Label(root,text="Date of Birth",bg="white",font=label_font)
labelpass.grid(row=8,column=1)


buttonresult = tk.Button(root, text="Sign Up",command=save,bg="grey", fg="white", width=10)
buttonresult.grid(row=9,column=2,padx=5,pady=5)

label_font=font.Font(weight="bold",size=10)
buttonclose = tk.Button(root, text="X",bg="white", fg="black", width=2,font=label_font)
buttonclose.grid(row=0,column=4,padx=5,pady=5)

drop_label.pack()
drop_labels.pack()
drop_labe.pack()

option_menu.pack(pady=10)
option_men.pack(pady=10)
optio_men.pack(pady=10)

root.mainloop()
