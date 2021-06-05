import tkinter
from tkinter import ttk
win = tkinter.Tk()
win.title('GUI')

# creating label
name_label = ttk.Label(
    win, text='Enter your Name :- ').grid(row=0, column=0, sticky=tkinter.W)

age_label = ttk.Label(
    win, text='Enter your Age :- ').grid(row=1, column=0, sticky=tkinter.W)

email_label = ttk.Label(
    win, text='Enter email email :- ').grid(row=2, column=0, sticky=tkinter.W)

gender_label = ttk.Label(
    win, text='Gender :- ').grid(row=3, column=0, sticky=tkinter.W)

# creating entry
name_var = tkinter.StringVar()
name_enterybox = ttk.Entry(
    win, width=16, textvariable=name_var).grid(row=0, column=1)
# name_enterybox.focus()

age_var = tkinter.IntVar()
age_enterybox = ttk.Entry(
    win, width=16, textvariable=age_var).grid(row=1, column=1)

email_var = tkinter.StringVar()
email_enterybox = ttk.Entry(
    win, width=16, textvariable=email_var).grid(row=2, column=1)

gender_var = tkinter.StringVar()
gender_combobox = ttk.Combobox(
    win, width=13, textvariable=gender_var, state='readonly')
gender_combobox['values'] = ('select', 'Male', 'Female', 'Others')
gender_combobox.grid(row=3, column=1)
gender_combobox.current(0)

# create radio button
usertype_var = tkinter.StringVar()
ttk.Radiobutton(win, text="Student", value="Student",
                variable=usertype_var).grid(row=4, column=0)
ttk.Radiobutton(win, text="Teacher", value="Teacher",
                variable=usertype_var).grid(row=4, column=1)


# create check button
checkbtn_var = tkinter.IntVar()
ttk.Checkbutton(
    win, text='Check the box for accept terms and condition', variable=checkbtn_var).grid(row=5, columnspan=2)
# create action for submit button


def action():
    name = name_var.get()
    email = email_var.get()
    age = age_var.get()
    gender = gender_var.get()
    Usertype = usertype_var.get()
    if checkbtn_var.get() == 0:
        subscribed = 'No'
    else:
        subscribed = 'Yes'
    print(
        f" Name:- {name}\n Age:- {age}\n Gender:- {gender}\n EMAIL:- {email}\n User Type :- {Usertype}\n Terms & Condition :- {subscribed}")
    # write the data in file
    with open('form.txt', 'a') as f:
        f.write(
            f" Name:- {name}\n Age:- {age}\n Gender:- {gender}\n EMAIL:- {email}\n User Type :- {Usertype}\n Terms & Condition :- {subscribed}\n\n")
    # name_enterybox.delete(0, tkinter.END)


    # create button
submit_button = ttk.Button(win, text='Submit', command=action)
submit_button.grid(row=6, column=0)


win.mainloop()
