# KivyMD libraries
from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import Snackbar

# kivy libraries
from kivy.factory import Factory

# External libraries
from pytube import YouTube
import threading

# Set window sixe
from kivy.core.window import Window
Window.size = (325, 600)

fileSize = 0


class HomePage(Screen):
    pass


class SettingPage(Screen):
    pass


class MainApp(MDApp):

    def build(self):
        return Builder.load_file('main.kv')

    def new_thread(self, url):
        thread = threading.Thread(self.select_res(url))
        thread.start()

    def duringProgress(self, stream, chunk, bytes_remaining):
        percent = ((fileSize - bytes_remaining)/fileSize)*100
        self.root.ids['Home_Page'].ids['prgsbar'].value = percent

    def downloadComplete(self, stream, file_path):
        toast("Downloading Complete")
        self.root.ids['Home_Page'].ids['btn'].disabled = False
        self.root.ids['Home_Page'].ids['btn'].text = 'Select Resolution'
        self.root.ids['Home_Page'].ids['spinner'].active = False

    def select_res(self, url):
        print(url.text)
        self.root.ids['Home_Page'].ids['btn'].disabled = True
        self.root.ids['Home_Page'].ids['btn'].text = 'Please Wait'
        self.root.ids['Home_Page'].ids['spinner'].active = True
        try:
            # video = https://www.youtube.com/watch?v=TLwhqmf4Td4

            self.yt = YouTube(url.text)

            self.yt.register_on_progress_callback(self.duringProgress)
            self.yt.register_on_complete_callback(self.downloadComplete)

            try:
                self.k128 = self.yt.streams.filter(
                    mime_type='audio/mp4').first()
                self.s1 = f"128K                {self.k128.filesize/1000000:0.02f} MB"
            except:
                self.s1 = f"128k                Unavailable"

            try:
                self.k144 = self.yt.streams.filter(
                    mime_type='video/mp4', progressive=True, res='144p').first()
                self.s2 = f"144p                {self.p144.filesize/1000000:0.02f} MB"
            except:
                self.s2 = f"144p                Unavailable"

            try:
                self.p240 = self.yt.streams.filter(
                    mime_type='video/mp4', progressive=True, res='240p').first()
                self.s3 = f"240p                {self.p240.filesize/1000000:0.02f} MB"
            except:
                self.s3 = f"240p                Unavailable"

            try:
                self.p360 = self.yt.streams.filter(
                    mime_type='video/mp4', progressive=True, res='360p').first()
                self.s4 = f"360p                {self.p360.filesize/1000000:0.02f} MB"
            except:
                self.s4 = f"360p                Unavailable"

            try:
                self.p480 = self.yt.streams.filter(
                    mime_type='video/mp4', progressive=True, res='480p').first()
                self.s5 = f"480p                {self.p480.filesize/1000000:0.02f} MB"
            except:
                self.s5 = f"480p                Unavailable"

            try:
                self.p720 = self.yt.streams.filter(
                    mime_type='video/mp4', progressive=True, res='720p').first()
                self.s6 = f"720p                {self.p720.filesize/1000000:0.02f} MB"
            except:
                self.s6 = f"720p                Unavailable"

            self.custom_sheet = MDCustomBottomSheet(
                screen=Factory.ContentCustomSheet())
            self.custom_sheet.open()

        except Exception as e:
            print(e, '\n', 'Please connect to the internet')
            self.root.ids['Home_Page'].ids['btn'].disabled = False
            self.root.ids['Home_Page'].ids['btn'].text = 'Select Resolution'
            self.root.ids['Home_Page'].ids['spinner'].active = False
            Snackbar(text='Please Connect to the Internet').show()

    def v_download(self, instance):
        toast("Downloading Start")
        global fileSize
        fileSize = instance.filesize
        instance.download()
        self.show_toast("Downloading Complete")

    def chng(self, page_name):
        ch = self.root.ids['sm']
        # ch.transition = FadeTransition()
        ch.current = page_name

    def show_toast(self, naam):
        toast(naam)


if __name__ == "__main__":
    MainApp().run()
