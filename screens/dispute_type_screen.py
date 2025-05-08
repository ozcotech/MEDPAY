from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.metrics import dp
from kivy.app import App
from functools import partial

class DisputeTypeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(15))

        # Title label
        self.layout.add_widget(Label(
            text="Uyuşmazlık Türünü Seçin",
            font_size=dp(22),
            size_hint=(1, 0.2)
        ))

        # Dispute type buttons
        self.add_dispute_button("İşçi-İşveren", "employment_dispute")
        self.add_dispute_button("Ticari", "commercial")
        self.add_dispute_button("Tüketici", "consumer")
        self.add_dispute_button("Kira-Komşu-Kat Mülkiyeti", "rental_neighbor_condo")
        self.add_dispute_button("Ortaklığın Giderilmesi", "dissolution_of_partnership")
        self.add_dispute_button("Aile Hukuku", "family_law")
        self.add_dispute_button("Diğer", "other")

        self.add_widget(self.layout)

    def add_dispute_button(self, label: str, dispute_key: str):
        btn = Button(text=label, size_hint=(1, 0.1), font_size=dp(18))
        btn.bind(on_release=partial(self.select_dispute_type, dispute_key))
        self.layout.add_widget(btn)

    def select_dispute_type(self, dispute_key, *args):
        app = App.get_running_app()
        app.secilen_uyusmazlik["tur"] = dispute_key
        # Navigate to the next screen after selecting dispute type
        self.manager.current = "dispute_detail"