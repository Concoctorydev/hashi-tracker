import sqlite3

conn = sqlite3.connect('hashitracker.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL UNIQUE,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS log_entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    date DATE NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS symptoms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS logged_symptoms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    log_entry_id INTEGER NOT NULL,
    symptom_id INTEGER NOT NULL,
    severity TEXT NOT NULL,
    FOREIGN KEY (log_entry_id) REFERENCES log_entries(id),
    FOREIGN KEY (symptom_id) REFERENCES symptoms(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS lifestyle_factors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    log_entry_id INTEGER NOT NULL,
    sleep_hours INTEGER,
    sleep_minutes INTEGER,
    sleep_quality TEXT,
    stress TEXT,
    illness BOOLEAN,
    menstruation BOOLEAN,
    routine_disruption BOOLEAN,
    exercise TEXT,
    FOREIGN KEY (log_entry_id) REFERENCES log_entries(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS diet_triggers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS logged_diet_triggers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    log_entry_id INTEGER NOT NULL,
    trigger_id INTEGER NOT NULL,
    FOREIGN KEY (log_entry_id) REFERENCES log_entries(id),
    FOREIGN KEY (trigger_id) REFERENCES diet_triggers(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS medications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    type TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS logged_medications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    log_entry_id INTEGER NOT NULL,
    medication_id INTEGER NOT NULL,
    status TEXT,
    FOREIGN KEY (log_entry_id) REFERENCES log_entries(id),
    FOREIGN KEY (medication_id) REFERENCES medications(id)
)
''')

symptom_list = [
    'fatigue', 'brain fog', 'constipation', 'muscle aches', 'joint pain',
    'bone pain', 'cold intolerance', 'depression', 'hair loss', 'dry skin',
    'irregular periods', 'puffy face', 'decreased sex drive'
]

for symptom in symptom_list:
    cursor.execute('INSERT OR IGNORE INTO symptoms (name) VALUES (?)', (symptom,))

diet_trigger_list = [
    'gluten', 'soy', 'dairy', 'nightshades', 'grains',
    'nuts/seeds', 'alcohol', 'caffeine', 'added sugar', 'unknown exposure'
]

for trigger in diet_trigger_list:
    cursor.execute('INSERT OR IGNORE INTO diet_triggers (name) VALUES (?)', (trigger,))

medication_list = [
    ('levothyroxine', 'prescription'),
    ('desiccated thyroid hormone', 'prescription'),
    ('liothyronine', 'prescription'),
    ('tymlos', 'prescription'),
    ('GLP-1', 'prescription'),
    ('selenium', 'supplement'),
    ('vitamin D', 'supplement'),
    ('zinc', 'supplement'),
    ('magnesium', 'supplement'),
    ('myo-inositol', 'supplement'),
    ('iron', 'supplement'),
    ('ashwagandha', 'supplement'),
    ('omega-3', 'supplement'),
    ('probiotics', 'supplement'),
    ('LDN', 'supplement'),
]

for name, med_type in medication_list:
    cursor.execute('INSERT OR IGNORE INTO medications (name, type) VALUES (?, ?)', (name, med_type))

conn.commit()
conn.close()
print("Database and all tables created successfully.")