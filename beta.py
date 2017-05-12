from Tkinter import *
import subprocess,os,platform,getpass,time

class windows(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master=master

        self.init_window()

        self.master.geometry("500x250+400+300")

    def init_window(self):
        self.master.title("YouTube downloader")
        self.pack(fill=BOTH,expand=1)
        self.list_commands=['youtube-dl']

#The enter button
        enter_button=Button(self,text='Show Qualities',command=self.choose_video_url)
        enter_button.place(x=350,y=14)
#The button to start download
        download_button=Button(self,text='Download',command=self.subprocess_command)
        download_button.place(x=200,y=200)
#The text entry field
        self.textob=StringVar()
        text_field=Entry(self.master,width=42,textvariable=self.textob)
        text_field.place(x=70,y=15)

#The text that says enter URL inside tk frame
        texty=Label(text="Enter URL:")
        texty.place(x=5,y=14)

#The top left menu
        menu=Menu(self.master)
        self.master.config(menu=menu)
#The elements of top left menu
        file=Menu(menu,tearoff=0)
        file.add_command(label='Open downloads',command=self.open_folder)
        file.add_command(label='Exit',command=self.enter_client)
        menu.add_cascade(label='File',menu=file)


#Alternate for dropdown menu
        self.textob1=StringVar()
        text_field_alternate=Entry(self.master,textvariable=self.textob1)
        text_field_alternate.place(x=90,y=55)
        quality=Label(text="Enter quality:")
        quality.place(x=7,y=55)
#other buttons
        subtitle_button=Button(self,text='Download subtitles',command=self.subtitle)
        subtitle_button.place(x=350,y=55)

        thumbnail_button=Button(self,text='Download thumbnail',command=self.thumbnail)
        thumbnail_button.place(x=350,y=90)

        self.textob2=StringVar()
        text_speed=Entry(self.master,textvariable=self.textob2)
        text_speed.place(x=100,y=130)
        text_speed_label=Label(text='Enter speed cap:')
        text_speed_label.place(x=7,y=130)

        self.textob3=StringVar()
        text_speed=Entry(self.master,textvariable=self.textob3)
        text_speed.place(x=100,y=160)
        text_speed_label=Label(text='Enter format:')
        text_speed_label.place(x=7,y=160)

        speed_button=Button(self,text='Cap speed',command=self.speed)
        speed_button.place(x=350,y=130)

        format_button=Button(self,text='Change format',command=self.video_format)
        format_button.place(x=350,y=160)


#Other functions
    def enter_client(self):
        self.master.destroy()
#the subprocess function that gives the available video qualities for the given URL
    def choose_video_url(self):
        self.video_url=self.textob.get()

        a=subprocess.check_output(['youtube-dl', '-F', self.video_url])
        global mylist

        mylist=a.split('\n')

        ct=0
        for i in range(7):
            mylist.pop(0)
        mylist.pop()
        for j in range(0,len(mylist)):
            print mylist[j]


#this function gets the name of user and returns folder name
    def User_name(self):
        name = getpass.getuser()

        if platform.system()=='Windows':
            self.whole_name='C:\Users\\'+name+'\Downloads\YoutubeDownloads'
        elif platform.system()=='Darwin':
            self.whole_name='/Users/'+name+'/Downloads/YoutubeDownloads'
        elif platform.system()=="Linux":
            self.whole_name=name+'/Documents/YoutubeDownloads'


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

    def subtitle(self):
        self.list_commands.append('--write-auto-sub')
    def thumbnail(self):
        self.list_commands.append('--write-thumbnail')
    def speed(self):
        self.speed_download=self.textob2.get()
        self.speed_list=['-r',self.speed_download]
        self.list_commands.extend(self.speed_list)
    def video_format(self):
        self.format=self.textob3.get()
        self.list_format=['--recode-video',self.format]
        self.list_commands.extend(self.list_format)

    def subprocess_command(self):
        self.video_url=self.textob.get()
        chosen_option=self.textob1.get()
        self.input_code=''
        for i in range(0,len(chosen_option)):
            self.input_code=self.input_code+chosen_option[i]
        name=self.User_name()
        list_download=['-f',self.input_code,'-o',name]
        self.list_commands.extend(list_download)
        self.video_url=self.textob.get()
        self.list_commands.append(self.video_url)
        print self.list_commands
        subprocess.call(self.list_commands)


root=Tk()

root.geometry("500x250+400+300")
app=windows(root)

root.mainloop()
