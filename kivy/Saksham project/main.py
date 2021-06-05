from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from plyer import gps


from kivymd.app import MDApp


class DetailsPage(Screen):
    pass


class HomePage(Screen):
    pass


class DashboardPage(Screen):
    pass


class GivenLocation(Screen):
    pass


class MainApp(MDApp):
    def build(self):
        return Builder.load_file('main.kv')

    def on_start(self):
        try:
            with open('details.text', 'r') as d:
                self.changeScreen('details') if d.readline(
                ) == '' else self.changeScreen('Home')
        except:
            self.changeScreen('details')

    def changeScreen(self, screenName):
        sm = self.root.ids['sm']
        sm.current = screenName

    def detailsValidate(self):
        if (self.root.ids['details'].ids['name'].text != '' and self.root.ids['details'].ids['age'].text != '' and self.root.ids['details'].ids['email'].text != '' and self.root.ids['details'].ids['phoneNumber'].text != ''):
            if (self.root.ids['details'].ids['age'].text).isnumeric() and (self.root.ids['details'].ids['phoneNumber'].text).isnumeric():
                if len(self.root.ids['details'].ids['phoneNumber'].text) == 10:
                    with open('details.text', 'w') as d:
                        d.write(self.root.ids['details'].ids['name'].text + ',' + self.root.ids['details'].ids['age'].text + ',' +
                                self.root.ids['details'].ids['email'].text + ',' + self.root.ids['details'].ids['phoneNumber'].text)
                    self.root.ids['sm'].current = 'Home'
                else:
                    print("Phone Number should we 10 digits")
            else:
                print("Age and Phone Number should be numeric")
        else:
            print("All fields are required")

    def preDashboard(self):
        with open('details.text', 'r') as d:
            name, age, email, phoneNumber = d.readline().split(',')
            self.root.ids['Dashboard'].ids['name'].text = name
            self.root.ids['Dashboard'].ids['age'].text = age
            self.root.ids['Dashboard'].ids['email'].text = email
            self.root.ids['Dashboard'].ids['phoneNumber'].text = phoneNumber

    def locationTrace(self):
        gps.configure(on_location=self.location)
        gps.start()

    def location(self, **kwargs):
        print(kwargs)


if __name__ == "__main__":
    MainApp().run()
