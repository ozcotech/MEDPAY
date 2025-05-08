from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from screens.start_screen import StartScreen  # First screen


class MedPayApp(App):
    def build(self):
        sm = ScreenManager(transition=SlideTransition())
        sm.add_widget(StartScreen(name="start"))  # First screen
        return sm

if __name__ == "__main__":
    MedPayApp().run()