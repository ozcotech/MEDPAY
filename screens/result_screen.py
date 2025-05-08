

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.metrics import dp

class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(20))

        self.result_label = Label(
            text="Sonuç burada gösterilecek",
            font_size=dp(20),
            size_hint=(1, 0.8)
        )
        self.layout.add_widget(self.result_label)

        back_button = Button(
            text="Geri Dön",
            size_hint=(1, 0.2),
            font_size=dp(18)
        )
        back_button.bind(on_release=self.go_back)
        self.layout.add_widget(back_button)

        self.add_widget(self.layout)

    def set_result(self, result_text: str):
        """Updates the result label with the given result."""
        self.result_label.text = result_text

    def go_back(self, instance):
        """Returns to the dispute type screen."""
        self.manager.current = "dispute_type"