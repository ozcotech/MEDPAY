from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.metrics import dp
from kivy.app import App


class NonAgreementDetailScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(15))

        # Display selected dispute category
        self.selected_dispute_label = Label(text="", font_size=dp(20), size_hint=(1, 0.15))
        self.layout.add_widget(self.selected_dispute_label)

        # Dropdown simulation for party count
        self.party_count_label = Label(text="Taraf Sayısını Giriniz", font_size=dp(16), size_hint=(1, 0.1))
        self.layout.add_widget(self.party_count_label)

        self.party_count_input = TextInput(hint_text="Örn: 2", multiline=False, size_hint=(1, 0.1))
        self.layout.add_widget(self.party_count_input)

        # Calculate button
        self.calculate_button = Button(text="HESAPLA", font_size=dp(18), size_hint=(1, 0.2))
        self.calculate_button.bind(on_release=self.calculate_fee)
        self.layout.add_widget(self.calculate_button)

        # Result label
        self.result_label = Label(text="", font_size=dp(18), size_hint=(1, 0.2))
        self.layout.add_widget(self.result_label)

        self.add_widget(self.layout)

    def on_enter(self):
        app = App.get_running_app()
        dispute_category = app.selected_dispute.get("kategori", "Belirtilmemiş")
        self.selected_dispute_label.text = f"Uyuşmazlık Kategorisi: {dispute_category}"

    def calculate_fee(self, instance):
        app = App.get_running_app()
        dispute_category = app.selected_dispute.get("kategori", "")
        try:
            party_count = int(self.party_count_input.text)
        except ValueError:
            self.result_label.text = "Lütfen geçerli bir sayı girin."
            return

        from models.tariff_model import TariffModel
        model = TariffModel()

        if party_count == 2:
            party_key = "2_kisi"
        elif 3 <= party_count <= 5:
            party_key = "3_5_kisi"
        elif 6 <= party_count <= 10:
            party_key = "6_10_kisi"
        else:
            party_key = "11_ve_uzeri"

        fee = model.get_non_monetary_nonagreement_fee(
            dispute_type=dispute_category,
            party_key=party_key
        )

        self.result_label.text = f"Arabuluculuk Ücreti: {fee:.2f} TL"