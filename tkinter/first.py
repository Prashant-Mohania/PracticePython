import tkinter
from tkinter import ttk
win = tkinter.Tk()
win.title('TechPramo')


# create label
name = ttk.Label(win, text="Enter your name:- ")
name.grid(row=0, column=0, sticky=tkinter.W)

# create entry
varName = tkinter.StringVar()
entry = ttk.Entry(win, width=16, textvariable=varName)
entry.grid(row=0, column=1)
entry.focus()

# create combobox
varCombobox = tkinter.StringVar()
combobox = ttk.Combobox(
    win, width=13, textvariable=varCombobox, state='readonly')
combobox['values'] = ('Select', 'Mobiles', 'Laptops', 'Accessories')
combobox.current(0)
combobox.grid(row=1, column=1)

# create radio button
varRadio = tkinter.StringVar()
ttk.Label(win, text='Respose').grid(row=2, column=0, sticky=tkinter.W)
radio = ttk.Radiobutton(win, text='Like', value='like',
                        variable=varRadio).grid(row=2, column=1)
radio = ttk.Radiobutton(win, text='Unlike', value='unlike',
                        variable=varRadio).grid(row=2, column=2)

# check button
varCheck = tkinter.IntVar()
check = ttk.Checkbutton(win, text="Terns and Condition",
                        variable=varCheck).grid(row=3, columnspan=3)


def action():
    enterName = varName.get()
    enterCombobox = varCombobox.get()
    enterRadio = varRadio.get()
    if varCheck.get() == 0:
        enterCheck = 'No'
    else:
        enterCheck = 'Yes'
    # print(enterName)
    # print(enterCombobox)
    with open('tk.txt', 'w') as fl:
        fl.write(f"{enterName}\n{enterCombobox}\n{enterRadio}\n{enterCheck}")
    entry.delete(0, tkinter.END)
    name.configure(foreground='red')


ttk.Button(win, text='Submits', command=action).grid(row=5, column=1)


win.mainloop()
# print(action())
