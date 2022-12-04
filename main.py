from tkinter import *
import mudopy

root = Tk()
myLabel = Label(root, text="Unextraordinary Music Downloader").grid(row='0', column='0')

Label2 = Label(root, text="Enter Your Music Name").grid(row="1",column='0')
name = Entry(root)
name.grid(row='2',column='0')
linkButton = Button(root, text='Go')
linkButton.grid(row='2', column='1')


root.mainloop()
