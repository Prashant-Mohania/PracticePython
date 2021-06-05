import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 2

        self.add_widget(Label(text="First name:- "))
        self.fname = TextInput(multiline=False)
        self.add_widget(self.fname)

        self.add_widget(Label(text="Last name:- "))
        self.lname = TextInput(multiline=False)
        self.add_widget(self.lname)

        self.add_widget(Label(text="Age:- "))
        self.age = TextInput(multiline=False)
        self.add_widget(self.age)

        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.btnSubmit)
        self.add_widget(Label())
        self.add_widget(self.submit)

    def btnSubmit(self, instance):
        fname = self.fname.text
        lname = self.lname.text
        age = self.age.text

        print(f"{fname}  {lname}   {age}")


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
