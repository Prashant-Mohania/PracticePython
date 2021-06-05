import tkinter
from tkinter import ttk
win = tkinter.Tk()
win.title('TechPramo')
# win.configure(bg='grey')
labels = ['Name', 'Age']
for i in range(len(labels)):
    cur_label = 'label' + str(i)
    cur_label = tkinter.Label(win, text=labels[i] +":- ").grid(
        row=i, column=0, sticky=tkinter.W, pady=2)

d = {
    'Name': tkinter.StringVar(),
    'Age': tkinter.IntVar()
}

c = 0
for i in d:
    cur_entry = 'entry' + i
    cur_entry = tkinter.Entry(
        win, width=16, textvariable=d[i]).grid(row=c, column=1)
    c += 1


def submit():
    name = d['Name'].get()
    age = d['Age'].get()
    print(f"{name}\n{age}")


ttk.Button(win, text='Submit', command=submit).grid(row=5, columnspan=2)
win.mainloop()
