from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '300')
from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import StringProperty, ListProperty

import string
import random

def random_password():
    special_char = [33,35,36,37,38]
    elements = "".join(map(chr, special_char))
    characters = string.ascii_letters + string.digits + elements
    return "".join(random.choice(characters) for i in range(random.randint(8, 15)))

class Generator(Widget):
    password = StringProperty(random_password())

    def generate(self):
        self.password = random_password()

class PasswordGeneratorApp(App):
    def build(self):
        return Generator()


if __name__ == "__main__":
    PasswordGeneratorApp().run()

# wJOVTiwgPB6YM
# YtETkOl4