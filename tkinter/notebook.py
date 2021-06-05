import tkinter
from tkinter import ttk
win = tkinter.Tk()
win.title('TechPramo')
nb = ttk.Notebook(win)
page1 = ttk.Frame(nb)
page2 = ttk.Frame(nb)
nb.add(page1, text='ONE')
nb.add(page2, text='TWO')
# nb.grid(row=0, column=0)
nb.pack(expand=True, fill='both')


# PAGE 1
labels = ['Name', 'Age']
for i in range(len(labels)):
    cur_label = 'label' + str(i)
    cur_label = tkinter.Label(page1, text=labels[i] + ":- ").grid(
        row=i+1, column=0, sticky=tkinter.W, pady=2)

d = {
    'Name': tkinter.StringVar(),
    'Age': tkinter.IntVar()
}

c = 0
for i in d:
    cur_entry = 'entry' + i
    cur_entry = tkinter.Entry(
        page1, width=16, textvariable=d[i]).grid(row=c+1, column=1)
    c += 1


def submit():
    name = d['Name'].get()
    age = d['Age'].get()
    print(f"{name}\n{age}")


ttk.Button(page1, text='Submit', command=submit).grid(row=5, columnspan=2)


# PAGE 2
labels = ['Name', 'Age']
for i in range(len(labels)):
    cur_label = 'label' + str(i)
    cur_label = tkinter.Label(page2, text=labels[i] + ":- ").grid(
        row=i, column=0, sticky=tkinter.W, pady=2)

d = {
    'Name': tkinter.StringVar(),
    'Age': tkinter.IntVar()
}

c = 0
for i in d:
    cur_entry = 'entry' + i
    cur_entry = tkinter.Entry(
        page2, width=16, textvariable=d[i]).grid(row=c, column=1)
    c += 1


def submit():
    name = d['Name'].get()
    age = d['Age'].get()
    print(f"{name}\n{age}")


ttk.Button(page2, text='Submit', command=submit).grid(row=5, columnspan=2)
win.mainloop()