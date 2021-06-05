import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title('My Notepad')


# def action():
#     print("Action")


def newFile():
    

# my_menu = tkinter.Menu(win)
# my_menu.add_command(label='File1', command=action)
# my_menu.add_command(label='File2', command=action)
# my_menu.add_command(label='File3', command=action)
# my_menu.add_command(label='File4', command=action)
# my_menu.add_command(label='help5', command=action)


main_menu = tkinter.Menu(win)
file_menu = tkinter.Menu(main_menu, tearoff=0)
file_menu.add_command(label="new File", command=action)
file_menu.add_command(label="open File", command=action)
file_menu.add_command(label="save File", command=action)
file_menu.add_command(label="save as", command=action)

main_menu.add_cascade(label='File', menu=file_menu)

win.config(menu=main_menu)

win.mainloop()
