create_table = '''
    CREATE TABLE appointments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        event TEXT NOT NULL,
        place TEXT NOT NULL,
        time TEXT NOT NULL,
        date TEXT NOT NULL,
        other TEXT
    )
'''

create_appointment = '''
    INSERT INTO appointments (event, place, time, date, other) values (?, ?, ?, ?, ?)
'''

find_appointments_by_date = "SELECT * FROM appointments WHERE date(date) = ?"