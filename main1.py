from kivy.app import App
from kivy.uix.label import Label

class Audio2(App):
    def build(self):
        label=Label(text="Welcome to Audiometry")
        return label

app= Audio2()
app.run()