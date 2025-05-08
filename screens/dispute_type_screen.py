from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.metrics import dp
from kivy.app import App

class DisputeTypeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(15))

        # Title label
        self.layout.add_widget(Label(
            text="Anlaşma Durumunu Seçin",
            font_size=dp(22),
            size_hint=(1, 0.2)
        ))

        # Agreement status buttons
        self.add_status_button("Anlaşma Yapıldı", True)
        self.add_status_button("Anlaşma Yapılamadı", False)

        self.add_widget(self.layout)

    def add_status_button(self, label: str, is_agreement: bool):
        btn = Button(text=label, size_hint=(1, 0.2), font_size=dp(18))
        btn.bind(on_release=lambda instance: self.set_status_and_continue(is_agreement))
        self.layout.add_widget(btn)

    def set_status_and_continue(self, is_agreement: bool):
        app = App.get_running_app()
        app.selected_dispute = {"anlasma": is_agreement}
        self.manager.current = "dispute_category"