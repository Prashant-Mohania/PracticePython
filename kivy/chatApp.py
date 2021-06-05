import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen


class ConnectPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        try:
            with open("Prev_details.text", "r") as f:
                d = f.read().split(",")
                prev_ip = d[0]
                prev_port = d[1]
                prev_username = d[2]

            self.cols = 2

            self.add_widget(Label(text="IP:- "))
            self.ip = TextInput(text=prev_ip, multiline=False)
            self.add_widget(self.ip)

            self.add_widget(Label(text="PORT:- "))
            self.port = TextInput(text=prev_port, multiline=False)
            self.add_widget(self.port)

            self.add_widget(Label(text="USERNAME:- "))
            self.username = TextInput(text=prev_username, multiline=False)
            self.add_widget(self.username)

        except:
            self.cols = 2

            self.add_widget(Label(text="IP:- "))
            self.ip = TextInput(multiline=False)
            self.add_widget(self.ip)

            self.add_widget(Label(text="PORT:- "))
            self.port = TextInput(multiline=False)
            self.add_widget(self.port)

            self.add_widget(Label(text="USERNAME:- "))
            self.username = TextInput(multiline=False)
            self.add_widget(self.username)

        self.join = Button(text="Join")
        self.join.bind(on_press=self.join_button)
        self.add_widget(Label())
        self.add_widget(self.join)

    def join_button(self, instance):
        ip = self.ip.text
        port = self.port.text
        username = self.username.text

        with open("prev_details.text", "w") as f:
            f.write(f"{ip},{port},{username}")

        # print(f"Joining: {ip}:{port} as {username}")
        info = f"Joining: {ip}:{port} as {username}"
        chat_app.info_page.upadte_info(info)
        chat_app.screen_manager.current = 'Info'


class InfoPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1

        self.message = Label(halign="center", valign="middle", font_size=30)

        self.message.bind(width=self.upadte_text_width)
        self.add_widget(self.message)

    def upadte_info(self, message):
        self.message.text = message

    def upadte_text_width(self, *_):
        self.message.text_size = (self.message.width * 0.9, None)


class ChatApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.connect_page = ConnectPage()
        screen = Screen(name='Connect')
        screen.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen)

        # info page
        self.info_page = InfoPage()
        screen = Screen(name='Info')
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)
        return self.screen_manager


if __name__ == "__main__":
    chat_app = ChatApp()
    chat_app.run()
