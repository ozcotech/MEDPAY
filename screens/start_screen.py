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
        
        # Uygulama başlığı
        title = Label(
            text="MEDPAY - Arabuluculuk Ücreti Hesaplama",
            font_size=dp(20),
            halign='center'
        )
        layout.add_widget(title)
        
        # Giriş butonu
        start_button = Button(
            text="Giriş",
            size_hint=(1, 0.2),
            font_size=dp(18)
        )
        start_button.bind(on_release=self.goto_next)
        layout.add_widget(start_button)
        
        self.add_widget(layout)

    def goto_next(self, instance):
        # Bu kısım sonraki ekran tanımlandığında değiştirilecek
        self.manager.current = "dispute_type"  # placeholder ekran adı