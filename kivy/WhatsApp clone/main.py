from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.toast import toast
from kivy.lang import Builder
from kivy.uix.screenmanager import SlideTransition

from kivy.core.window import Window

Window.size = (350, 600)



class Tab(FloatLayout, MDTabsBase):
    pass


class HomeScreen(Screen):
    pass


class ContactScreen(Screen):
    pass


class MainApp(MDApp):
    def build(self):
        return Builder.load_file("main.kv")

    def change_screen(self, screen_name, screen_dir):
        # print(self.root.ids)
        screen_Manager = self.root.ids["screen_manager"]
        screen_Manager.transition = SlideTransition(direction=screen_dir)
        screen_Manager.current = screen_name
    
    def show_toast(self, popUp):
        toast(popUp)


if __name__ == "__main__":
    MainApp().run()
