from kivymd.app import MDApp
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase
from kivy.uix.screenmanager import ScreenManager, Screen


class Tab(FloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''

# class Contact(Screen):
#     pass

# class MainWindow(ScreenManager):
#     pass


class MainApp(MDApp):
    # data = {
    #     'contacts': 'Contacts',
    #     'phone': 'call',
    # }
    # data1 = {
    #     'pen': '',
    #     'camera': ''
    # }
    # def build(self):
        # self.theme_cls.primary_palette = "Green"
        # self.theme_cls.accent_palette = "Green"
        # self.menu_items = [{"icon": "", "text": "New Group"}, {"icon": "", "text": "New Broadcast"}, {
        #     "icon": "", "text": "WhatsApp Web"}, {"icon": "", "text": "Starred Message"}, {"icon": "", "text": "Settings"}]

        # def set_item(self, instance):
        #     self.VARIABLE = instance
    pass


MainApp().run()
