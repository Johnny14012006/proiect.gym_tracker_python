from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
# --- IMPORT MODIFICAT ---
from database.db_manager import get_all_exercises, delete_last_exercise

class HistoryScreen(Screen):
    def go_back(self, instance):
        self.manager.current = "add"
        
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        self.scroll = ScrollView()
        self.content = BoxLayout(orientation="vertical", size_hint_y=None)
        self.content.bind(minimum_height=self.content.setter('height'))

        self.scroll.add_widget(self.content)
        self.layout.add_widget(Label(text="📋 Istoric exerciții", font_size=22, bold=True))
        self.layout.add_widget(self.scroll)

        # --- ÎNCEPUT MODIFICARE BUTOANE ---
        # Creăm un layout orizontal pentru butoanele de jos
        bottom_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height=50, spacing=10)

        btn_back = Button(text="⬅️ Înapoi")
        btn_back.bind(on_press=self.go_back)
        
        # Butonul nou de ștergere
        btn_delete_last = Button(text="🗑️ Șterge ultima")
        btn_delete_last.bind(on_press=self.delete_last)

        # Adăugăm butoanele în layout-ul orizontal
        bottom_layout.add_widget(btn_back)
        bottom_layout.add_widget(btn_delete_last)

        # Adăugăm layout-ul orizontal la layout-ul principal
        self.layout.add_widget(bottom_layout)
        # --- SFÂRȘIT MODIFICARE BUTOANE ---

        self.add_widget(self.layout)

    # --- FUNCȚIE NOUĂ PENTRU ȘTERGERE ---
    def delete_last(self, instance):
        try:
            delete_last_exercise() # Apelăm funcția din db_manager
            self.refresh() # Reîmprospătăm lista
        except Exception as e:
            # Ar fi bine să avem un label de status și aici, dar momentan doar printăm
            print(f"Eroare la ștergere: {e}")
    # --- SFÂRȘIT FUNCȚIE NOUĂ ---

    def on_pre_enter(self):
        self.refresh()

    def refresh(self):
        self.content.clear_widgets()
        exercises = get_all_exercises()
        if not exercises:
            # Am adăugat size_hint_y și height pentru a se afișa corect
            self.content.add_widget(Label(text="Nicio înregistrare găsită.", size_hint_y=None, height=40))
            return

        for id_db, name, weight, reps, date in exercises:
            text = f"[{date}] {name} - {weight}kg ({reps or '-'} reps)"
            self.content.add_widget(Label(text=text, size_hint_y=None, height=40))