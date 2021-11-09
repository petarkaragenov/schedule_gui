from controllers.appointments_controller import AppointmentsController
from db.db import con, cursor

def delete_appointment(idx):
    return AppointmentsController(con, cursor).delete(idx)
    