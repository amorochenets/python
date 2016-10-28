# !/usr/bin/env python3
# coding UTF-8

from tkinter import *
counter = 'rest'
def printer(event):
    count = 'er'
    print('Now counter is %s' % count)
    return count

root = Tk()
but = Button(root,
             text='Print',
             height=4, width=16,
             bg='blue', fg='yellow')
# but['text'] = 'Print'
but.bind("<Button-1>",printer)
but.pack()
root.mainloop()