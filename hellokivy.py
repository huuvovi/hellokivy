from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
        def build(self):
            return Label(text='HUU VO VI')

if __name__ == '__main__':
    MyApp().run()
