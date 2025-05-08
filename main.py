from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from screens.start_screen import StartScreen  # First screen
from screens.dispute_type_screen import DisputeTypeScreen  # Second screen

class MedPayApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_dispute = {}

    def build(self):
        sm = ScreenManager(transition=SlideTransition())
        sm.add_widget(StartScreen(name="start"))  # First screen
        sm.add_widget(DisputeTypeScreen(name="dispute_type"))  # Second screen
        return sm

if __name__ == "__main__":
    MedPayApp().run()