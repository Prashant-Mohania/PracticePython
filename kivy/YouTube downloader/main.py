from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivymd.uix.bottomsheet import MDListBottomSheet
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.snackbar import Snackbar
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from pytube import YouTube
import threading


class HomeScreen(Screen):

    bottom_res = None


    class DrawerList(ThemableBehavior, MDList):
        pass

    def progress_check(self, stream, chunk, bytes_remaining):
        '''Check Progress'''
        self.ids.spinner.active = False
        downComp = (fileSize - bytes_remaining)
        percent = (downComp/fileSize)*100
        self.ids.btn.text = f"{percent:0.00f} % Downloaded"
        self.ids.prgsbar.value = f"{percent:0.00f}"
        # toast("Download Complete")
        self.ids.btn.disabled = True

    def download_check(self, stream, chunk, file_path):
        '''call when download complete'''
        # self.show_toast("Downloading Complete")
        self.ids.btn.disabled = True
        Snackbar(text="Download Complete").show()

    def new_thread(self, url):
        '''Start new thread'''
        thread = threading.Thread(self.select_res(url))
        thread.start()

    def select_res(self, instance):
        '''Get video details'''
        print(instance.text)
        self.ids.spinner.active = True
        self.ids.btn.disabled = True
        try:
            self.v_yt = YouTube(instance.text)
            self.ids.url.text = ""
            self.v_yt.register_on_progress_callback(self.progress_check)
            self.v_yt.register_on_complete_callback(self.download_check)
            self.bottom_res = MDListBottomSheet()
            self.bottom_res.add_item(
                "Resolution           Type           Size    ", lambda x: None)

            try:
                self.k128 = self.v_yt.streams.filter(only_audio=True).all()
                self.bottom_res.add_item(
                    f"  128K                  mp3           {self.k128[0].filesize/1000000:.3f} MB", lambda x: self.Download(self.k128))

            except:
                self.bottom_res.add_item(
                    f"  128K                  mp4           Unavailable", lambda x: None)

            try:
                # self.bottom_res.add_item(f"{self.p144[0].title}", lambda x: None)
                self.p144 = self.v_yt.streams.order_by('resolution').filter(
                    mime_type='video/mp4', res='144p', progressive=True).all()
                self.bottom_res.add_item(
                    f"  144p                  mp4           {self.p144[0].filesize/1000000:.3f} MB", lambda x: self.Download(self.p144))

            except:
                self.bottom_res.add_item(
                    f"  144p                  mp4           Unavailable", lambda x: None)

            try:
                self.p240 = self.v_yt.streams.order_by('resolution').filter(
                    mime_type='video/mp4', res='240p', progressive=True).all()
                self.bottom_res.add_item(
                    f"  240p                  mp4           {self.p240[0].filesize/1000000:.3f} MB", lambda x: self.Download(self.p240))

            except:
                self.bottom_res.add_item(
                    f"  240p                  mp4           Unavailable", lambda x: None)

            try:
                self.p360 = self.v_yt.streams.order_by('resolution').filter(
                    mime_type='video/mp4', res='360p', progressive=True).all()
                self.bottom_res.add_item(
                    f"  360p                  mp4           {self.p360[0].filesize/1000000:.3f} MB", lambda x: self.Download(self.p360))

            except:
                self.bottom_res.add_item(
                    f"  360p                  mp4     Unavailable", lambda x: None)

            try:
                self.p480 = self.v_yt.streams.order_by('resolution').filter(
                    mime_type='video/mp4', res='480p', progressive=True).all()
                self.bottom_res.add_item(
                    f"  480p                  mp4           {self.p480[0].filesize/1000000:.3f} MB", lambda x: self.Download(self.p480))

            except:
                self.bottom_res.add_item(
                    f"  480p                  mp4           Unavailable", lambda x: None)

            try:
                self.p720 = self.v_yt.streams.order_by('resolution').filter(
                    mime_type='video/mp4', res='720p', progressive=True).all()
                self.bottom_res.add_item(
                    f"  720p                  mp4               {sep720[0].filesize/1000000:.3f} MB", lambda x: self.Download(self.p720))

            except:
                self.bottom_res.add_item(
                    f"  720p                  mp4           Unavailable", lambda x: None)

            self.bottom_res.open()
        except:
            print("Please Connect to the internet")
            self.ids.btn.text = "Select Resolution"
            self.ids.btn.disabled = False
            # self.show_toast("Please Connect to the internet")
            Snackbar(text="Please connect to the internet").show()
            self.ids.spinner.active = False

    def Download(self, num):
        '''Download selcted resolution video and get file size'''
        self.select_res.bottom_res.on_dismiss()
        global fileSize
        fileSize = num[0].filesize
        num[0].download(f"{isPath}")     # for pc
        # num[0].download(r"\storage\emulated\0\Download")      # for mobile
        toast(f"Downloading vedio download at {isPath}")
        # toast("Download Complete")

    def show_toast(self, popUp):
        '''Show toast'''
        toast(popUp)


class MainApp(MDApp):

    def build(self):
        return Builder.load_file("main.kv")

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
            # previous=True
        )

    def file_manager_open(self):
        self.file_manager.show('/')
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
