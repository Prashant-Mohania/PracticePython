from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image


class HomePage(Screen):
    pass


class SettingPage(Screen):
    pass

class ImageButton(ButtonBehavior, Image):
    pass

GUI = Builder.load_file('main.kv')


class MainApp(App):
    def build(self):
        return GUI

    def s(self):
        ch = self.root.ids['home_page'].ids['streak']
        ch.text = '20 Days Streaks'
        self.root.ids['setting_page'].ids['btn'].text = 'icon'

    def change_page(self, page_name, page_dir):
        '''changge screen ,  give name and direction'''
        sm = self.root.ids['screen_manager']
        sm.transition = SlideTransition(direction=page_dir)
        sm.current = page_name


if __name__ == "__main__":
    MainApp().run()
