import subprocess
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
subprocess_command()
