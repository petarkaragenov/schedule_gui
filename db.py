import sqlite3

con = sqlite3.connect('appointments.db')
cursor = con.cursor()