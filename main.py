from tkinter import *
from tkinter import messagebox
#importing files
#creating new_task
def new_task():
    task=my_entry.get()
    if task != "":
        lb.insert(END,task)
        my_entry.delete(0,'end')
    else:
        messagebox.showwarning('empty task can\'t be added')
#del_task creation
def del_task():
    lb.delete(ANCHOR)

#window creation
ws = Tk()
ws.geometry('500x450+500+200')
ws.title('TO-DO')
ws.config(bg='Black')
ws.resizable(width=FALSE,height=FALSE)

#frame creation
frame =Frame(ws)
frame.pack(pady= 10)

#create#listbox
lb=Listbox(frame,
           width = 25,
           height= 8,
           font=('times',18),
           bd =0,
           fg = 'Blue',
           highlightthickness= 0,
           selectbackground='Red',
           activestyle ='none',
           )
lb.pack(side =LEFT, fill = BOTH)

#sample list of tasks
Task_list=[
    'open pycharm',
    'create github',
    'link both',
    'create one project',
]
for item in Task_list:
    lb.insert(END,item)

#scrollbar creation
sb = Scrollbar(frame)
sb.pack(side=RIGHT,fill = BOTH)
lb.config(yscrollcommand = sb.set)
sb.config(command= lb.yview)

#my entry box creation
my_entry =Entry(ws,font=('times',24))
my_entry.pack(pady =20)

#button frame
button_frame =Frame(ws)
button_frame.pack(pady=20)
#add utton
add_btn=Button(button_frame,
               padx=20,
               pady=10,
               text='add task',
               bg='Orange',
               font=('times 18'),
               command = new_task
               )
add_btn.pack(side=LEFT,expand =True,fill=BOTH)
#del button
del_btn=Button(button_frame,
               padx=20,
               pady=10,
               text='del task',
               bg='Green',
               font=('times 18'),
               command = del_task
               )
del_btn.pack(side=RIGHT,expand=True,fill=BOTH)

ws.mainloop()