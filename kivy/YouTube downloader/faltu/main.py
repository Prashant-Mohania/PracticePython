from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivymd.uix.bottomsheet import MDListBottomSheet
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.filemanager import MDFileManager
from kivy.core.window import Window
from pytube import YouTube
import threading

# Global variables
isPath = " "
fileSize = 0


class MainApp(MDApp):

    def build(self):
        return Builder.load_file("main.kv")

    def progress_check(self, stream, chunk, bytes_remaining):
        '''Check Progress'''
        # self.root.ids.spinner.active = False
        downComp = (fileSize - bytes_remaining)
        percent = (downComp/fileSize)*100
        self.root.ids.btn.text = f"{percent:0.00f} % Downloaded"
        self.root.ids.prgsbar.value = f"{percent:0.00f}"
        # toast("Download Complete")

    def download_check(self, stream, chunk, file_path):
        '''call when download complete'''
        # self.show_toast("Downloading Complete")
        Snackbar(text="Download Complete").show()

    def new_thread(self, url):
        '''Start new thread'''
        thread = threading.Thread(self.select_res(url))
        thread.start()

    def select_res(self, instance):
        '''Get video details'''
        self.root.ids.btn.text = "loading.........."
        self.root.ids.toolbar.title = "Prashant"
        try:
            print(instance.text)
            self.root.ids.url.text = ""
            self.root.ids.spinner.active = True
            self.root.ids.btn.disabled = True
            self.v_yt = YouTube(instance.text)
            self.v_yt.register_on_progress_callback(self.progress_check)
            self.v_yt.register_on_complete_callback(self.download_check)
            bottom_res = MDListBottomSheet()
            bottom_res.add_item(
                "Resolution                 Type                 Size    ", lambda x: None)

            try:
                self.k128 = self.v_yt.streams.filter(only_audio=True).all()
                bottom_res.add_item(
                    f"128K                    mp3                        size = {self.k128[0].filesize/1000000:.3f} MB", lambda x: self.Download(self.k128))

            except:
                bottom_res.add_item(
                    f"128K                    mp4                        Unavailable", lambda x: None)

            try:
                # bottom_res.add_item(f"{self.p144[0].title}", lambda x: None)
                self.p144 = self.v_yt.streams.order_by('resolution').filter(
                    mime_type='video/mp4', res='144p', progressive=True).all()
                bottom_res.add_item(
                    f"144p                    mp4                        size = {self.p144[0].filesize/1000000:.3f} MB", lambda x: self.Download(self.p144))

            except:
                bottom_res.add_item(
                    f"144p                    mp4                        Unavailable", lambda x: None)

            try:
                self.p240 = self.v_yt.streams.order_by('resolution').filter(
                    mime_type='video/mp4', res='240p', progressive=True).all()
                bottom_res.add_item(
                    f"240p                    mp4                        size = {self.p240[0].filesize/1000000:.3f} MB", lambda x: self.Download(self.p240))

            except:
                bottom_res.add_item(
                    f"240p                    mp4                        Unavailable", lambda x: None)

            try:
                self.p360 = self.v_yt.streams.order_by('resolution').filter(
                    mime_type='video/mp4', res='360p', progressive=True).all()
                bottom_res.add_item(
                    f"360p                    mp4                        size = {self.p360[0].filesize/1000000:.3f} MB", lambda x: self.Download(self.p360))

            except:
                bottom_res.add_item(
                    f"360p                    mp4                       Unavailable", lambda x: None)

            try:
                self.p480 = self.v_yt.streams.order_by('resolution').filter(
                    mime_type='video/mp4', res='480p', progressive=True).all()
                bottom_res.add_item(
                    f"480p                    mp4                        size = {self.p480[0].filesize/1000000:.3f} MB", lambda x: self.Download(self.p480))

            except:
                bottom_res.add_item(
                    f"480p                    mp4                        Unavailable", lambda x: None)

            try:
                self.p720 = self.v_yt.streams.order_by('resolution').filter(
                    mime_type='video/mp4', res='720p', progressive=True).all()
                bottom_res.add_item(
                    f"720p                    mp4                        size = {self.p720[0].filesize/1000000:.3f} MB", lambda x: self.Download(self.p720))

            except:
                bottom_res.add_item(
                    f"720p                    mp4                        Unavailable", lambda x: None)

            bottom_res.open()
        except:
            print("Please Connect to the internet")
            self.root.ids.btn.text = "Select Resolution"
            self.root.ids.btn.disabled = False
            # self.show_toast("Please Connect to the internet")
            Snackbar(text="Please connect to the internet").show()
            # self.root.ids.spinner.active = False

    def Download(self, num):
        '''Download selcted resolution video and get file size'''
        global fileSize
        fileSize = num[0].filesize
        num[0].download(f"{isPath}")     # for pc
        # num[0].download(r"\storage\emulated\0\Download")      # for mobile
        toast(f"Downloading vedio download at {isPath}")
        # toast("Download Complete")

    def show_toast(self, popUp):
        '''Show toast'''
        toast(popUp)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            previous=True
        )
        self.file_manager.backgroung_color = 'red'

    def file_manager_open(self):
        self.file_manager.show('/PRAMO_CD')
        self.manager_open = True

    def select_path(self, path):
        self.exit_manager()
        toast(path)
        global isPath
        isPath = path

    def exit_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True


if __name__ == "__main__":
    MainApp().run()
