import PySimpleGUI as sg
from defaults import today, m, d, y
from appointments_controller import AppointmentsController
from db import con, cursor

def find_appointments_by_date(date):
    print(AppointmentsController(con, cursor).find_one(date))
    return AppointmentsController(con, cursor).find_one(date)