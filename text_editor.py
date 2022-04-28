#importing the code libary for interfaces - called tkinter
from tkinter import *

#use Tk to create a window
window=Tk()
#create a heading
headingLabel=Label(text="text editor").pack()

#create a text entry box
textInput=Text(width=30, height=5)
textInput.pack()

def Save():
    print("Save")

    #create a file
    myFile=open("data.txt","w")

    #write textbox contents to the file
    content=textInput.get("1.0","end")
    print(content)
    myFile.write(content)

    #close the file
    myFile.close()

#create save button
buttonSave=Button(text="Save", command=Save).pack()

#create exit button
buttonClose=Button(text="Close", command=exit).pack()

### DO NOT TYPE BELOW THIS LINE ###
#keep that window on screen
window.mainloop()
