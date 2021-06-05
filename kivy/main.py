from win32com.client import Dispatch
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


# for voice speaking


class MyGrid(Widget):
    fname = ObjectProperty(None)
    lname = ObjectProperty(None)

    def Submit(self):
        print(f"First Name:- {self.fname.text}\nLast Name:- {self.lname.text}")

        # audio = Dispatch("SAPI.SpVoice")
        # audio.speak(self.fname.text + " " + self.lname.text)

        self.fname.text = ""
        self.lname.text = ""


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
