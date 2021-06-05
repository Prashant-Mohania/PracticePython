# # import datetime

# # var = datetime.datetime.now()

# # print(var.date())
# # print(var.today())

# # import kivy
# # from kivy.app import App
# # from kivy.uix.label import Label
# # from kivy.animation import Animation
# # from kivy.properties import NumericProperty, StringProperty


# # class Clock(Label):
# #     a = NumericProperty(2)

# #     def start(self):
# #         Animation.cancel_all(self)
# #         self.anim = Animation(a=0, duration=self.a)

# #         def finish_callback(animation, clock):
# #             clock.text = 'FINISHED'

# #         self.anim.bind(on_complete=finish_callback)
# #         self.anim.start(self)

# #         def on_a(self, instance, value):
# #             self.text = str(round(value, 1))


# # class TimeApp(App):
# #     def build(self):
# #         clock = Clock()
# #         clock.start()
# #         return clock


# # TimeApp().run()

# # import datetime
# # from kivymd.app import MDApp
# # from kivymd.uix.boxlayout import BoxLayout
# # from kivymd.uix.label import MDLabel
# # from kivy.uix.button import Button
# # from kivy.clock import Clock
# # import sys

# # class TimerApp(MDApp):
# #     duration = "0, 0, 5"   # (Hours, minutes, seconds)
# #     h, m, s = duration.split(',')
# #     def build(self):
# #         self.main_box = BoxLayout(orientation='vertical')
# #         # n = datetime.datetime.now().strftime('%H:%M:%S')
# #         self.btn = Button(text=f'hello', font_size=100)
# #         Clock.schedule_interval(self.timer, 1)
# #         self.main_box.add_widget(self.btn)
# #         return self.main_box

# #     def timer(self, abc):
# #         # print(abc)
# #         print(self.h, self.m, self.s)
# #         if int(self.s) > 0:
# #             self.btn.text = f'{self.h}:{self.m}:{self.s}'
# #             self.s = int(self.s) - 1
# #         else:
# #             self.btn.text = 'TIME UPS'


# # TimerApp().run()


# from kivymd.app import MDApp
# from kivymd.uix.label import MDLabel
# from kivy.uix.button import Button
# from kivy.lang import Builder
# from kivy.clock import Clock
# from kivy.properties import StringProperty

# kv = '''
# GridLayout:
#     cols: 1
#     dur: input
#     MDLabel:
#         id: update
#         text: 'Timer'
#         halign: 'center'
#         font_size: 100
#     TextInput:
#         id: input
#         hint_text: 'Enter duration of test in minutes'
#         multiline: False

#     Button:
#         text: 'Press'
#         on_release: app.btn_press()
# '''


# class TimerApp(MDApp):

#     def build(self):
#         return Builder.load_string(kv)

#     def btn_press(self):
#         self.second = 00
#         self.dur = self.root.ids['input'].text
#         self.duration = divmod(int(self.dur), 60)
#         self.minutes = self.duration[1]
#         self.hours = self.duration[0]
#         print(self.duration[0], 'Hours', self.duration[1], 'Minutes')

#         # self.h, self.m, self.s = self.dur.split(',')
#         # print(type(self.dur))

#         # print(f'{h}:{m}:{s}')
#         # self.root.ids['update'].text = f'{self.h}:{self.m}:{self.s}'
#         Clock.schedule_interval(self.countdown, 1)

#     def countdown(self, *args):
#         # self.s = abs(int(self.s)) - 1
#         # if abs(int(self.h)) > 0:
#         #     print(self.h)
#         #     if 0 <= abs(int(self.m)) < 61:
#         #         print(self.m)
#         #         if abs(int(self.s)) >= 0:
#         #             self.root.ids['update'].text = f'{abs(int(self.h))}:{abs(int(self.m))}:{abs(int(self.s))}'
#         #         if abs(int(self.s)) == 0:
#         #             self.m = abs(int(self.m)) - 1
#         #             self.s = 60
#         # elif abs(int(self.h)) == 0 and abs(int(self.m)) == 0 and abs(int(self.s)) == 0:
#         #     self.root.ids['update'].text = 'Times Ups'
#         # else:
#         #     self.h = abs(int(self.h)) - 1

#         if abs(int(self.hours)) == 0 and abs(int(self.minutes)) == 0 and abs(int(self.second)) == 0:
#             self.root.ids['update'].text = 'TIME\'S UPS'

#         elif abs(int(self.hours)) >= 0:
#             if abs(int(self.minutes)) >= 0:
#                 if self.second > 0:
#                     self.root.ids['update'].text = f'{abs(int(self.hours))}:{abs(int(self.minutes))}:{abs(int(self.second))}'
#                     self.second -= 1
#                 elif self.second == 0 and abs(int(self.minutes)) > 0:
#                     self.root.ids['update'].text = f'{abs(int(self.hours))}:{abs(int(self.minutes))}:{abs(int(self.second))}'
#                     self.second = 59
#                     self.minutes -= 1
#                 elif self.minutes == 0 and self.hours > 0 and self.second == 0:
#                     self.root.ids['update'].text = f'{abs(int(self.hours))}:{abs(int(self.minutes))}:{abs(int(self.second))}'
#                     self.minutes = 60
#                     self.hours -= 1


# TimerApp().run()


# lst = ['hi\n', 'hello\n']

# f = open('file.txt', 'a')
# f.writelines(lst)


# import random

# lst = [1, 2, 3, 4]
# lst[1] = 9
# print(str(lst))


# from kivymd.app import MDApp
# # from kivy.uix.modalview import
# from kivy.lang import Builder

# kv = '''
# BoxLayout:
#     orinentation: 'vertical'
#     canvas:
#         Color:
#             rgba: [1, 1, .56, 1]
#         Rectangle:
#             pos: self.pos
#             size: self.size
#     padding: dp(40)
#     spacing: "50dp"
#     Carousel:
#         # padding: "20dp"
#         MDFloatLayout:
#             MDCard:
#                 pos_hint: {'center_x': .5, 'center_y': .5}
#                 size_hint: .9, .58
#                 MDLabel:
#                     text: "Prashant"

#         MDFloatLayout:
#             MDCard:
#                 pos_hint: {'center_x': .5, 'center_y': .5}
#                 size_hint: .9, .58
#                 MDLabel:
#                     text: "Prashant"

#         MDFloatLayout:
#             MDCard:
#                 pos_hint: {'center_x': .5, 'center_y': .5}
#                 size_hint: .9, .58
#                 MDLabel:
#                     text: "Prashant"

# '''

# class faltu(MDApp):
#     def build(self):
#         return Builder.load_string(kv)


# faltu().run()


# with open('results/' + '2020-09-11 Python 700-109-314' + '.mock', 'r') as f:
#     line = f.readline()
#     qo = f.readlines()
#     name, id, date, qn, t = line.split(',')
# with open('results/' + id + ".ans", 'r') as a:
#     answers = a.readline().split(',')
#     for i in range(int(qn)):
#         ewai = qo[i].split(',')
#         cq = 0
#         wq = 0
#         print(answers[i], ewai[1])
#         if ewai[1] == answers[i]:
#             cq += 2
#         elif ewai[1] != answers[i]:
#             wq += 1

# print(cq, wq)








# from kivymd.app import MDApp
# from kivy.lang import Builder

# kv = '''
# Screen:
#     id: sc
#     name: 'sc'
#     GridLayout:
#         id: gl
#         cols: 1
#         MDLabel:
#             id: lb
#             text: "Hello"
#         Button:
#             text: "remove"
#             on_release:
#                 app.a()
            
#         Button:
#             text: "Add"
#             on_release:
#                 app.s()

# '''

# class EWAI(MDApp):
#     def build(self):
#         return Builder.load_string(kv)
    
#     def a(self):
#         from kivymd.uix.label import MDLabel
#         lb1 = MDLabel(
#             text="Prashant",
#             halign='center'
#         )
#         self.root.ids['gl'].add_widget(lb1)

#     def s(self):
#         # self.root.ids['sc'].ids[]
#         # print(self.root.ids['lb'])
#         # self.root.ids['gl'].remove_widget(self.root.ids['lb'])
#         for i in self.root.ids['gl'].children:
#             print(i)
#             self.root.ids['gl'].remove_widget(i)

# if __name__ == "__main__":
#     EWAI().run()



import datetime

d1 = datetime.datetime.strptime('05/01/2015', '%d/%m/%Y').date()
d2 = datetime.datetime.strptime('30/04/2015', '%d/%m/%Y').date()
print(d1<d2)


