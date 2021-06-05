# from pytube import YouTube


# def ytDownload(url):
#     # yt = YouTube("https://www.youtube.com/watch?v=OHU80BsabxQ")
#     yt = YouTube(url)
#     for strm in yt.streams.all():
#         print(strm)
#         print(strm.filesize)


# from kivymd.app import MDApp
# from kivy.lang import Builder
# from kivy.factory import Factory
# from kivy.utils import get_hex_from_color

# from kivymd.uix.dialog import MDInputDialog, MDDialog
# from kivymd.theming import ThemeManager
# from kivymd.uix.label import MDLabel


# Builder.load_string('''
# <ExampleDialogs@BoxLayout>
#     orientation: 'vertical'
#     spacing: dp(5)

#     MDToolbar:
#         id: toolbar
#         title: app.title
#         left_action_items: [['menu', lambda x: None]]
#         elevation: 10
#         md_bg_color: app.theme_cls.primary_color

#     FloatLayout:
#         MDRectangleFlatButton:
#             text: "Open input dialog"
#             pos_hint: {'center_x': .5, 'center_y': .7}
#             opposite_colors: True
#             on_release: app.show_example_input_dialog()

#         MDRectangleFlatButton:
#             text: "Open Ok Cancel dialog"
#             pos_hint: {'center_x': .5, 'center_y': .5}
#             opposite_colors: True
#             on_release: app.show_example_okcancel_dialog()
# ''')


# class Example(MDApp):
#     title = "Dialogs"

#     def build(self):
#         return Factory.ExampleDialogs()

#     def callback_for_menu_items(self, *args):
#         from kivymd.toast.kivytoast import toast
#         toast(args[0])

#     def show_example_input_dialog(self):
#         dialog = MDInputDialog(
#             title='Title', hint_text='Hint text', size_hint=(.8, .4),
#             text_button_ok='Yes',
#             events_callback=self.callback_for_menu_items)
#         dialog.open()

#     def show_example_okcancel_dialog(self):
#         dialog = MDDialog(
#             title='Title', size_hint=(.8, .3), text_button_ok='Yes',
#             text="Your [color=%s][b]text[/b][/color] dialog" % get_hex_from_color(
#                 self.theme_cls.primary_color),
#                 # content= MDLabel(text="Prashant"),
#             text_button_cancel='Cancel',
#             events_callback=self.callback_for_menu_items)
#         dialog.open()


# Example().run()
'''



# from kivy.lang import Builder

# from kivymd.toast import toast
# from kivymd.uix.bottomsheet import MDListBottomSheet
# from kivymd.app import MDApp

# KV = 
# '''
# Screen:

#     MDToolbar:
#         title: "Example BottomSheet"
#         pos_hint: {"top": 1}
#         elevation: 10

#     MDRaisedButton:
#         text: "Open list bottom sheet"
#         on_release: app.show_example_list_bottom_sheet()
#         pos_hint: {"center_x": .5, "center_y": .5}
# '''


# class Example(MDApp):
#     def build(self):
#         return Builder.load_string(KV)

#     def callback_for_menu_items(self, *args):
#         toast(args[0])

#     def show_example_list_bottom_sheet(self):
#         bottom_sheet_menu = MDListBottomSheet()
#         for i in range(1, 11):
#             bottom_sheet_menu.add_item(
#                 f"Standart Item {i}",
#                 lambda x, y=i: self.callback_for_menu_items(
#                     f"Standart Item {y}"
#                 ),
#             )
#         bottom_sheet_menu.open()


# Example().run()


# from kivy.core.window import Window
# from kivy.lang import Builder
# from kivy.uix.boxlayout import BoxLayout
# from kivymd.app import MDApp
# from kivymd.uix.filemanager import MDFileManager
# from kivymd.toast import toast


# KV = '''
# BoxLayout:
#     orientation: 'vertical'

#     MDToolbar:
#         title: "File Manager"

#     FloatLayout:
#         MDRoundFlatIconButton:
#             text: "Open Manager"
#             icon: "folder"
#             pos_hint: {'x': .5, 'y': .5}
#             on_release: app.file_manager_open()
# '''

# ispath = " "


# class Example(MDApp):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         Window.bind(on_keyboard=self.events)
#         self.manager_open = False
#         self.file_manager = MDFileManager(
#             exit_manager=self.exit_manager,
#             select_path=self.select_path,
#             previous=True
#         )

#     # def build(self):
#     #     return Builder.load_string(KV)

#     def file_manager_open(self):
#         self.file_manager.show('/')
#         self.manager_open = True

#     def select_path(self, path):
#         self.exit_manager()
#         toast(path)
#         global ispath
#         ispath = path

#     def exit_manager(self, *args):
#         self.manager_open = False
#         self.file_manager.close()

#     def events(self, instance, keyboard, keycode, text, modifiers):
#         if keyboard in (1001, 27):
#             if self.manager_open:
#                 self.file_manager.back()
#         return True


# if __name__ == "__main__":
#     Example().run()
#     print(ispath)


# sample: https://www.youtube.com/watch?v=d3D7Y_ycSms

# from pytube import YouTube
# import os

# # on_progress_callback takes 4 parameters.
# def progress_Check(stream = None, chunk = None, file_handle = None, remaining = None):
#     #Gets the percentage of the file that has been downloaded.
#     percent = (100*(file_size-remaining))/file_size
#     print("{:00.0f}% downloaded".format(percent))

# #Grabs the file path for Download
# def file_path():
#     home = os.path.expanduser('~')
#     download_path = os.path.join(home, 'Downloads')
#     return download_path

# def start():
#     print("Your video will be saved to: {}".format(file_path()))
#     #Input
#     yt_url = input("Copy and paste your YouTube URL here: ")
#     print(yt_url)
#     print ("Accessing YouTube URL...")

#     # Searches for the video and sets up the callback to run the progress indicator.
#     try:
#         video = YouTube(yt_url, on_progress_callback=progress_Check)
#     except:
#         print("ERROR. Check your:\n  -connection\n  -url is a YouTube url\n\nTry again.")
#         redo = start()

#     #Get the first video type - usually the best quality.
#     video_type = video.streams.filter(progressive = True, file_extension = "mp4").first()

#     #Gets the title of the video
#     title = video.title

#     #Prepares the file for download
#     print ("Fetching: {}...".format(title))
#     global file_size
#     file_size = video_type.filesize
#     #Starts the download process
#     video_type.download(file_path())

#     print ("Ready to download another video.\n\n")
#     again = start()

# file_size = 0
# begin = start()


# from kivy.lang import Builder
# from kivymd.uix.bottomsheet import MDCustomBottomSheet
# from kivymd.app import MDApp
# from kivy.factory import Factory
# KV = '''
# <ItemForCustomBottomSheet@OneLineIconListItem>
#     on_press: app.custom_sheet.dismiss()
#     icon: ""
#     IconLeftWidget:
#         icon: root.icon
# <ContentCustomSheet@BoxLayout>:
#     orientation: "vertical"
#     size_hint_y: None
#     height: "400dp"
#     MDToolbar:
#         title: 'Custom bottom sheet:'
#     ScrollView:
#         MDGridLayout:
#             cols: 1
#             adaptive_height: True
#             ItemForCustomBottomSheet:
#                 icon: "page-previous"
#                 text: "Preview"
#             ItemForCustomBottomSheet:
#                 icon: "exit-to-app"
#                 text: "Exit"
# Screen:
#     MDToolbar:
#         title: 'Example BottomSheet'
#         pos_hint: {"top": 1}
#         elevation: 10
#     MDRaisedButton:
#         text: "Open custom bottom sheet"
#         on_release: app.show_example_custom_bottom_sheet()
#         pos_hint: {"center_x": .5, "center_y": .5}
# '''


# class Example(MDApp):
#     custom_sheet = None

#     def build(self):
#         return Builder.load_string(KV)

#     def show_example_custom_bottom_sheet(self):
#         self.custom_sheet = MDCustomBottomSheet(
#             screen=Factory.ContentCustomSheet())
#         self.custom_sheet.open()


# Example().run()

from kivymd.app import MDApp
from kivy.lang import Builder

kv = '''
NavigationLayout:
    ScreenManager:
        Screen:
            id: s1
            BoxLayout:
                orientation: 'vertical'
                MDToolbar:
                    id: tb
                    title: 'Prashant'
                    left_action_items: [['menu', lambda x: nav.toggle_nav_drawer()]]
                Button:
                    id: btn
                    text: 'Fatlu'
                    on_press: app.ch()
        
        Screen:
            id: s2
            MDLabel:
                text: 'Prashant Mohania'
    MDNavigationDrawer:
        id: nav
'''


class bbb(MDApp):
    def build(self):
        return Builder.load_string(kv)

    def ch(self):
        # self.root.ids.tb.title = 'Mohania'
        self.root.ids.btn.text = "Press me"
        



bbb().run()
