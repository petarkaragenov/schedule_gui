from controllers.appointments_controller import AppointmentsController
from db.db import con, cursor

def find_appointments_by_date(date):
    return AppointmentsController(con, cursor).find_many_by_date(date)

def find_appointments_by_id(idx):
    return AppointmentsController(con, cursor).find_one(idx)
