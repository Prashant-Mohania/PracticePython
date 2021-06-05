import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class CalcGridLayout(GridLayout):
    def Calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display = 'Error'


class CalculatorApp(App):
    def build(self):
        return CalcGridLayout()


if __name__ == "__main__":
    CalculatorApp().run()
