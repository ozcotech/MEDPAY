from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from screens.start_screen import StartScreen  # First screen
from screens.dispute_type_screen import DisputeTypeScreen  # Second screen
from screens.dispute_category_screen import DisputeCategoryScreen
from screens.dispute_detail_screen import DisputeDetailScreen
from screens.non_agreement_detail_screen import NonAgreementDetailScreen
from screens.result_screen import ResultScreen

class MedPayApp(App):
    title = "MEDPAY"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_dispute = {}

    def build(self):
        sm = ScreenManager(transition=SlideTransition())
        sm.add_widget(StartScreen(name="start"))  # First screen
        sm.add_widget(DisputeTypeScreen(name="dispute_type"))  # Second screen
        sm.add_widget(DisputeCategoryScreen(name="dispute_category"))  # Third screen
        sm.add_widget(DisputeDetailScreen(name="dispute_detail"))  # Fourth screen
        sm.add_widget(NonAgreementDetailScreen(name="non_agreement_detail"))
        sm.add_widget(ResultScreen(name="result"))
        return sm

if __name__ == "__main__":
    MedPayApp().run()