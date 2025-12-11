import sqlite3
import datetime

def init_db():
    conn = sqlite3.connect("gym_data.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS exercises (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            weight REAL NOT NULL,
            reps INTEGER NOT NULL,
            date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_exercise(name, weight, reps):
    conn = sqlite3.connect("gym_data.db")
    cursor = conn.cursor()
    
    today = datetime.date.today().strftime("%Y-%m-%d")
    
    cursor.execute("INSERT INTO exercises (name, weight, reps, date) VALUES (?, ?, ?, ?)",
                   (name, weight, reps, today))
    conn.commit()
    conn.close()

def get_all_exercises():
    conn = sqlite3.connect("gym_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, weight, reps, date FROM exercises ORDER BY date DESC, id DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows

# --- FUNCȚIE NOUĂ ADAUGATĂ ---
def delete_last_exercise():
    """
    Găsește înregistrarea cu cel mai mare ID (ultima adăugată) și o șterge.
    """
    conn = sqlite3.connect("gym_data.db")
    cursor = conn.cursor()
    
    # Găsește ID-ul cel mai mare (ultima înregistrare adăugată)
    cursor.execute("SELECT MAX(id) FROM exercises")
    last_id_result = cursor.fetchone()
    
    if last_id_result and last_id_result[0] is not None:
        last_id = last_id_result[0]
        # Șterge înregistrarea cu acel ID
        cursor.execute("DELETE FROM exercises WHERE id = ?", (last_id,))
        conn.commit()
        
    conn.close()
# --- SFÂRȘIT FUNCȚIE NOUĂ ---