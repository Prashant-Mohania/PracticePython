# from kivy.lang import Builder
# from kivymd.uix.bottomsheet import MDCustomBottomSheet
# from kivymd.app import MDApp
# from kivy.factory import Factory

# KV = '''
# # <ItemForCustomBottomSheet@OneLineIconListItem>
# # on_press: app.custom_sheet.dismiss()
# # icon: ""
# # IconLeftWidget:
# # icon: root.icon
# # <ContentCustomSheet@BoxLayout>:
# # orientation: "vertical"
# # size_hint_y: None
# # height: "400dp"
# # MDToolbar:
# # title: 'Custom bottom sheet:'
# # ScrollView:
# # MDGridLayout:
# # cols: 1
# <ItemForCustomBottomSheet@OneLineIconListItem>
#     on_release: app.custom_sheet.dismiss()
#     icon: ""
#     IconLeftWidget:
#         icon: root.icon
# <ContentCustomSheet@BoxLayout>:
#     orientation: "vertical"
#     size_hint_y: None
#     height: "400dp"
#     MDToolbar:
#         title: 'Custom bottom sheet:'
#         md_bg_color: 1, 0 , 0, 1
#     ScrollView:
#         GridLayout:
#             cols: 1
#             adaptive_height: True
#             ItemForCustomBottomSheet:
#                 icon: "page-previous"
#                 text: "Preview"
#             MDSeparator:
#                 height: "10dp"

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



# from kivy.lang import Builder

# from kivymd.app import MDApp

# KV = '''
# <TooltipMDIconButton@MDIconButton+MDTooltip>


# Screen:

#     TooltipMDIconButton:
#         icon: "language-python"
#         tooltip_text: self.icon
#         pos_hint: {"center_x": .5, "center_y": .5}
# '''


# class Test(MDApp):
#     def build(self):
#         return Builder.load_string(KV)


# Test().run()





# from kivy.lang import Builder

# from kivymd.app import MDApp
# from kivymd.uix.taptargetview import MDTapTargetView

# KV = '''
# Screen:

#     MDFloatingActionButton:
#         id: button
#         icon: "plus"
#         pos: 10, 10
#         on_release: app.tap_target_start()
# '''


# class TapTargetViewDemo(MDApp):
#     def build(self):
#         screen = Builder.load_string(KV)
#         self.tap_target_view = MDTapTargetView(
#             widget=screen.ids.button,
#             title_text="This is an add button",
#             description_text="This is a description of the button",
#             widget_position="left_bottom",
#         )

#         return screen

#     def tap_target_start(self):
#         if self.tap_target_view.state == "close":
#             self.tap_target_view.start()
#         else:
#             self.tap_target_view.stop()


# TapTargetViewDemo().run()








from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
BoxLayout:

    # Will always be at the bottom of the screen.
    MDBottomAppBar:

        MDToolbar:
            title: "Title"
            icon: "git"
            type: "bottom"
            left_action_items: [["menu", lambda x: x]]
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)


Test().run()