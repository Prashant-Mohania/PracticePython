# from kivy.lang import Builder

# from kivymd.app import MDApp
# from kivymd.uix.bottomsheet import MDCustomBottomSheet
# from kivy.factory import Factory
# KV = '''
# #:import utils kivy.utils
# <ItemForCustomBottomSheet@OneLineIconListItem>
#     on_press:
#         app.custom_sheet.dismiss()
#         print("Hello")
#     icon: ""

#     IconLeftWidget:
#         icon: root.icon


# <ContentCustomSheet@BoxLayout>:
#     orientation: "vertical"
#     size_hint_y: None
#     height: "400dp"
#     FloatLayout:
#         GridLayout:
#             cols: 3
#             pos_hint: {'top': 1, 'left': 1}
#             size_hint: 1, .1
#             canvas:
#                 Color:
#                     rgba: utils.get_color_from_hex('#20B3F2')
#                 Rectangle:
#                     size: self.size
#                     pos: self.pos
#             Label:
#                 text: 'Prashant'
#             Label:
#                 text: 'Prashant'
#             Label:
#                 text: 'Prashant'


#             # MDToolbar:
#             #     title: 'Custom bottom sheet:'

#         GridLayout:
#             rows: 1
#             pos_hint: {'top': .9, 'left': 1}

#             ScrollView:

#                 MDGridLayout:
#                     cols: 1
#                     adaptive_height: True

#                     ItemForCustomBottomSheet:
#                         icon: "page-previous"
#                         text: "Preview"
#                         on_release: print("Hello")

#                     ItemForCustomBottomSheet:
#                         icon: "exit-to-app"
#                         text: "Exit"


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


# from plyer import notification
# notification.notify('Hello','Hey iam', 'IamPramo')


# from kivy.lang import Builder
# from kivymd.toast import toast
# from kivymd.uix.bottomsheet import MDListBottomSheet
# from kivymd.app import MDApp
# KV = '''
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

from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.card import MDCardSwipe
KV = '''
<SwipeToDeleteItem>:
    size_hint_y: None
    height: content.height
    MDCardSwipeLayerBox:
        padding: "8dp"
        MDIconButton:
            icon: "trash-can"
            pos_hint: {"center_y": .5}
            on_release: app.remove_item(root)
    MDCardSwipeFrontBox:
        OneLineListItem:
            id: content
            text: root.text
            _no_ripple_effect: True
Screen:
    BoxLayout:
        orientation: "vertical"
        spacing: "10dp"
        MDToolbar:
            elevation: 10
            title: "MDCardSwipe"
        ScrollView:
            MDList:
                id: md_list
                padding: 0
'''


class SwipeToDeleteItem(MDCardSwipe):
    text = StringProperty()


class TestCard(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)

    def build(self):
        return self.screen

    def remove_item(self, instance):
        self.screen.ids.md_list.remove_widget(instance)

    def on_start(self):
        for i in range(20):
            self.screen.ids.md_list.add_widget(
                SwipeToDeleteItem(text=f"One-line item {i}")
            )


TestCard().run()
