from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class Interface(FloatLayout):
    def print_label(self):
        self.ids.LBL1.text = self.ids.TXTINP1.text


class FirstApp(App):
    def build(self):
        return Interface()

FirstApp().run()