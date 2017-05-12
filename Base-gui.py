from Tkinter import *
import subprocess,os,platform,getpass

class windows(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master=master

        self.init_window()

    def init_window(self):
        self.master.title("YouTube downloader")
        self.pack(fill=BOTH,expand=1)
#The enter button
        enterbutton=Button(self,text='Enter',command=self.printit)
        enterbutton.place(x=500,y=10)
#The text entry field
        self.textob=StringVar()
        textfield=Entry(self.master,width=62,textvariable=self.textob)
        textfield.place(x=120,y=14)

#The text that says enter URL inside tk frame
        texty=Label(text="Enter URL")
        texty.place(x=5,y=14)

#The top right menu
        menu=Menu(self.master)
        self.master.config(menu=menu)
#The elements of top right menu
        file=Menu(menu)
        file.add_command(label='Open downloads',command=self.open_folder)
        file.add_command(label='Exit',command=self.enter_client)
        menu.add_cascade(label='File',menu=file)

        edit=Menu(menu)
        edit.add_command(label='Undo')
        menu.add_cascade(label='Edit',menu=edit)

#Other functions
    def printit(self):
        print self.textob.get()
    def User_name(self):
        name=os.environ.get("USERNAME")
        if platform.system()=='Windows':
            whole_name='C:\Users\\'+ name + '\Downloads\YoutubeDownloads'
#        elif platform.system()=='Linux':
#            whole_name='Users\''+name+'\Downloads'
        elif platform.system()=='Darwin':
            name = getpass.getuser()
            whole_name='/Users//' + name + '/Downloads/YoutubeDownloads'

        self.whole_name=whole_name
        return self.whole_name

    def enter_client(self):
        self.master.destroy()

    def open_folder(self):
        newpath=self.User_name()
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        if platform.system() == "Windows":
            os.startfile(newpath)
        elif platform.system() == "Darwin":
            subprocess.Popen(["open", newpath])
        else:
            subprocess.Popen(["xdg-open", newpath])


root=Tk()
root.geometry("600x400+350+200")
app=windows(root)
root.mainloop()
