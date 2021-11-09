

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

update_appointment = '''
    UPDATE appointments SET event = ?, place = ?, time = ?, date = ?, other = ? WHERE id = ?
'''

find_appointments_by_date = "SELECT * FROM appointments WHERE date(date) = ?"

find_appointments_by_id = "SELECT * FROM appointments WHERE id = ?"

delete_appointment = "DELETE FROM appointments WHERE id = ?"