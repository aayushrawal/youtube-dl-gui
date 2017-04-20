from Tkinter import *
import subprocess,os,platform,getpass,time

class windows(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master=master

        self.init_window()

        self.master.geometry("600x200")

    def init_window(self):
        self.master.title("YouTube downloader")
        self.pack(fill=BOTH,expand=1)

#The enter button
        enter_button=Button(self,text='Show Qualities',command=self.choose_video_url)
        enter_button.place(x=450,y=14)
#The button to start download
        download_button=Button(self,text='Download',command=self.download_video_url)
        download_button.place(x=450,y=50)
#The text entry field
        self.textob=StringVar()
        text_field=Entry(self.master,width=42,textvariable=self.textob)
        text_field.place(x=70,y=14)

#The text that says enter URL inside tk frame
        texty=Label(text="Enter URL")
        texty.place(x=5,y=14)

#The top left menu
        menu=Menu(self.master)
        self.master.config(menu=menu)
#The elements of top left menu
        file=Menu(menu,tearoff=0)
        file.add_command(label='Open downloads',command=self.open_folder)
        file.add_command(label='Exit',command=self.enter_client)
        menu.add_cascade(label='File',menu=file)

#The dropdown menu for available downloads
        global mylist
        mylist=['']
        var=StringVar(self.master)
        var.set("Select download quality")
        my_menu=OptionMenu(self.master,var,mylist)
        my_menu.place(x=250,y=50)

#Other functions
    def enter_client(self):
                self.master.destroy()
#the subprocess function that gives the available video qualities for the given URL
    def choose_video_url(self):
        video_url=self.textob.get()
        a=subprocess.check_output(['youtube-dl', '-F', video_url])
        global mylist
        print mylist
        mylist=a.split('\n')
        print mylist
        ct=0
        for i in range(7):
            mylist.pop(0)
        mylist.pop()
​
        time.sleep(10)
        self.master.destroy()
​
        root=Tk()
        root.geometry("600x400+350+200")
        app=windows(root)
​
        root.mainloop()
#the subprocess function that inputs quality and downloads the quality
    def download_video_url(self):
        chosen_option=var.get()
        input_code=''
        for i in range(0,3):
            input_code=input_code+chosen_option[i]
        subprocess.call(['youtube-dl', '-f', input_code,'-o',self.whole_name,video_url])
        #this function gets the name of user and returns folder name
    def User_name(self):
        name = getpass.getuser()
        
        if platform.system()=='Windows':
            whole_name='C:\Users\\'+ name + '\Downloads\YoutubeDownloads'
        elif platform.system()=='Darwin':
            whole_name='/Users//' + name + '/Downloads/YoutubeDownloads'
        elif platform.system()=="Linux":
            whole_name=name+'/Documents'
​
        self.whole_name=whole_name
        return self.whole_name
#this function opens download folder and creates if folder is not there
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
​
​
​
​
root=Tk()
​
root.geometry("600x400+350+200")
app=windows(root)
​
root.mainloop()
