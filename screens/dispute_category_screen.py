from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.metrics import dp
from kivy.app import App
from functools import partial

class DisputeCategoryScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = GridLayout(cols=2, padding=dp(20), spacing=dp(15), row_force_default=True, row_default_height=dp(60))

        # Title Label (spans two columns)
        title = Label(
            text="Uyuşmazlık Kategorisini Seçin",
            font_size=dp(22),
            size_hint=(1, None),
            height=dp(40),
            halign="center",
            valign="middle"
        )
        layout.add_widget(title)
        layout.add_widget(Label())  # Empty label to occupy second column

        # Dispute categories and corresponding keys
        categories = [
            ("İşçi-İşveren", "employment_dispute"),
            ("Ticari", "commercial"),
            ("Tüketici", "consumer"),
            ("Kira-Komşu-Kat Mülkiyeti", "rental_neighbor_condo"),
            ("Ortaklığın Giderilmesi", "dissolution_of_partnership"),
            ("Aile Hukuku", "family_law"),
            ("Diğer", "other")
        ]

        for label, key in categories:
            btn = Button(text=label, font_size=dp(18))
            btn.bind(on_release=partial(self.select_category, key))
            layout.add_widget(btn)

        self.add_widget(layout)

    def select_category(self, category_key, *args):
        app = App.get_running_app()
        app.selected_dispute["kategori"] = category_key
        if app.selected_dispute.get("anlasma"):  # "durum" anahtarı "anlasma" olarak değiştirildi
            self.manager.current = "dispute_detail"
        else:
            self.manager.current = "non_agreement_detail"
