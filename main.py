from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from database.db_manager import init_db
from screens.add_screen import AddScreen
from screens.history_screen import HistoryScreen

class GymApp(App):
    def build(self):
        Window.clearcolor = (0.1, 0.1, 0.1, 1)
        Window.size = (400, 600)

        init_db()

        sm = ScreenManager()
        sm.add_widget(AddScreen(name="add"))
        sm.add_widget(HistoryScreen(name="history"))
        return sm

if __name__ == "__main__":
    GymApp().run()
