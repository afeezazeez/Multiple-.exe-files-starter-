import tkinter as tk
from tkinter import filedialog, Text #for dialog and text
import os #allows us to run apps to bbe added to this app

app= tk.Tk()
applications=[]  

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps= f.read()
        tempApps= tempApps.split(',')
        applications=[x for x in tempApps if x.strip()]
       

def addApp():
    for widget in frame.winfo_children():
         widget.destroy()
    
    filename=filedialog.askopenfilename(initialdir='/', title='select file',
    filetypes=(( "executables","*.exe"),("all files", "*.*")) )
    
    applications.append(filename)
    for application in applications:
        label=tk.Label(frame, text=application, bg="grey")
        label.pack()
def runApps():
    for application in applications:
        os.startfile(application)
                                          


canvas= tk.Canvas(app, height=700, width=700, bg='#263D42')#main interface
canvas.pack()

frame=tk.Frame(app,bg='white')
frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1 )

openFile=tk.Button(app, text="Open File", padx=10,pady=5,
                    fg="white", bg="#263D42", command=addApp)
openFile.pack()

runApps=tk.Button(app, text="Run Apps", padx=10,pady=5,
                    fg="white", bg="#263D42", command=runApps)
runApps.pack()


for application in applications:
    label= tk.Label(frame, text=application)
    label.pack()

app.mainloop()

with open('save.txt','w') as f:
    for application in applications:
        f.write(application+',')