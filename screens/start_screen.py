# screens/start_screen.py

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.metrics import dp


class StartScreen(Screen):
    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', spacing=dp(20), padding=dp(40))
        
        # Application title
        title = Label(
            text="MEDPAY - Arabuluculuk Ücreti Hesaplama",
            font_size=dp(20),
            halign='center'
        )
        layout.add_widget(title)
        
        # Start button
        start_button = Button(
            text="Giriş",
            size_hint=(1, 0.2),
            font_size=dp(18)
        )
        start_button.bind(on_release=self.goto_next)
        layout.add_widget(start_button)
        
        self.add_widget(layout)

    def goto_next(self, instance):
        # This part will be changed when the next screen is defined
        self.manager.current = "dispute_type"  # placeholder screen name