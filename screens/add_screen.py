from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from database.db_manager import add_exercise

class AddScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", padding=90, spacing=15)

        self.exercise = TextInput(hint_text="Exercițiu", multiline=False)
        self.weight = TextInput(hint_text="Greutate (kg)", multiline=False, input_filter='float')
        self.reps = TextInput(hint_text="Repetări", multiline=False, input_filter='int')

        self.status = Label(text="", font_size=16)

        btn_add = Button(text="💾 Adaugă exercițiu", size_hint_y=None, height=50)
        btn_add.bind(on_press=self.save_exercise)

        btn_history = Button(text="📋 Vezi Istoric", size_hint_y=None, height=50)
        
        # --- MODIFICARE ---
        # Am șters funcția 'go_to_history' de aici
        btn_history.bind(on_press=self.go_to_history) # Și am legat-o de metoda clasei

        layout.add_widget(Label(text="🏋️ GYM TRACKER 🏋️", font_size=22, bold=True))
        layout.add_widget(self.exercise)
        layout.add_widget(self.weight)
        layout.add_widget(self.reps)
        layout.add_widget(btn_add)
        layout.add_widget(btn_history)
        layout.add_widget(self.status)

        self.add_widget(layout)

    # --- MODIFICARE ---
    # Am mutat funcția aici, ca metodă a clasei
    def go_to_history(self, instance):
        self.manager.current = "history"

    def save_exercise(self, instance):
        ex = self.exercise.text.strip()
        wt = self.weight.text.strip()
        rp = self.reps.text.strip()

        if not ex or not wt:
            self.status.text = "⚠️ Completează exercițiul și greutatea!"
            return

        try:
            # --- MODIFICARE ---
            # 1. Am scos argumentul 'date' (se adaugă automat)
            # 2. Am înlocuit 'None' cu 0, deoarece coloana 'reps' este NOT NULL
            add_exercise(ex, float(wt), int(rp) if rp else 0)
            
            self.status.text = f"✅ {ex} adăugat!"
            self.exercise.text = self.weight.text = self.reps.text = ""
        except Exception as e:
            self.status.text = f"❌ Eroare: {e}"