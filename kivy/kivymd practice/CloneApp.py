from kivymd.app import MDApp
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase
from kivy.uix.screenmanager import ScreenManager, Screen


class Tab(FloatLayout, MDTabsBase):
    pass

# class Contact(BoxLayout):
#     pass


class CloneApp(MDApp):
    pass


CloneApp().run()
