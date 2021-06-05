from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp

# kv ='''
# <MyFront>:
#     pos: 200, 200
#     size: 100, 100
#     padding: 20
#     spacing: 20

#     MDLabel:
#         text: 'Paste YouTube Video URL'
#         halign: 'center'
#         font_size: 40
        
#     TextInput:
#         id: url
#         hint_text: "Paste URL"
#         multiline: False
#         halign: 'center'
#         size_hint: .4, .4

#     MDRoundFlatButton:
#         id: btn
#         text: "Select Resolution"
#         font_size: 20
#         on_release: 
#             app.show_toast('Enter URL') if url.text == '' else app.new_thread(url)

#     MDSpinner:
#         id: spinner
#         size_hint: None, None
#         size: dp(100), dp(100)    
#         pos_hint: {'center_x': .5, 'center_y': .2}
#         active: False

#     MDLabel:
#         text: ""
#         size_hint: .2, .2
        
#     MDProgressBar:
#         id: prgsbar
#         value: 0
# '''


# class MyFront():
#     pass


class pagal(MDApp):
    def build(self):
        return Builder.load_string('''
BoxLayout:
    orientation: 'vertical'
    MDBackdrop:
        title: "YouTube Downloader"
        md_bg_color: 1, 0, 0, 1
        MDBackdropToolbar:
            title: "Vedio"
        MDBackdropBackLayer:
            MDLabel:
                text: "Mohania"
                halign: 'center'
                font_size: 50
        MDBackdropFrontLayer:
            MDLabel:
                text: "Prashant"
                halign: 'center'
                font_size: 50  
            # MyFront:
            #     id: myf      
''')


pagal().run()
