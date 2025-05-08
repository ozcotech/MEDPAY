from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.app import App


class DisputeDetailScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(15))

        category_labels = {
            "employment_dispute": "İşçi-İşveren Uyuşmazlığı",
            "commercial": "Ticari Uyuşmazlık",
            "consumer": "Tüketici Uyuşmazlığı",
            "rental_neighbor_condo": "Kira/Komşu/Kat Mülkiyeti",
            "dissolution_of_partnership": "Ortaklığın Giderilmesi",
            "family_law": "Aile Hukuku",
            "other": "Diğer"
        }

        selected_key = App.get_running_app().selected_dispute.get("kategori", "other")
        category_label = category_labels.get(selected_key, "Diğer")

        self.title_label = Label(
            text=f"Uyuşmazlık Kategorisi: {category_label}",
            font_size=dp(22),
            size_hint=(1, 0.2)
        )
        self.layout.add_widget(self.title_label)

        self.amount_input = TextInput(
            hint_text="Anlaşma Tutarını Giriniz",
            multiline=False,
            input_filter='float',
            size_hint=(1, 0.2),
            font_size=dp(18)
        )
        self.layout.add_widget(self.amount_input)

        self.party_input = TextInput(
            hint_text="Taraf Sayısını Giriniz",
            multiline=False,
            input_filter='int',
            size_hint=(1, 0.2),
            font_size=dp(18)
        )
        self.layout.add_widget(self.party_input)

        self.calculate_button = Button(
            text="HESAPLA",
            size_hint=(1, 0.2),
            font_size=dp(18)
        )
        self.calculate_button.bind(on_release=self.calculate_fee)
        self.layout.add_widget(self.calculate_button)

        self.result_label = Label(
            text="",
            font_size=dp(18),
            size_hint=(1, 0.2)
        )
        self.layout.add_widget(self.result_label)

        self.add_widget(self.layout)

    def calculate_fee(self, instance):
        try:
            amount = float(self.amount_input.text)
            parties = int(self.party_input.text)

            app = App.get_running_app()
            selected_dispute_category = app.selected_dispute.get("kategori", "general") # "tur" "kategori" olarak değiştirildi
            # Placeholder for calculation - replace with real logic
            fee = amount * 0.06
            if selected_dispute_category == "commercial" and fee < 9000: # selected_dispute selected_dispute_category olarak değiştirildi
                fee = 9000
            elif fee < 6000:
                fee = 6000

            self.result_label.text = f"Arabuluculuk Ücreti: {fee:.2f} TL"

        except ValueError:
            self.result_label.text = "Geçerli bir tutar ve taraf sayısı giriniz."