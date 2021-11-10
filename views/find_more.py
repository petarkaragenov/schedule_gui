import PySimpleGUI as sg
from datetime import datetime, timedelta
import calendar
from db.db import con, cursor
from helpers.defaults import time_periods
from helpers.elements import ScheduleTable, Button
from controllers.appointments_controller import AppointmentsController


def find_more():
    def get_start_and_end_dates(period):
        today = datetime.now()

        if "Week" in period:
            current_day = today.weekday()

            if "Next" in period:
                today += timedelta(days=7)

            week_start = (today - timedelta(days=current_day)).strftime("%Y-%m-%d")
            week_end = ((today - timedelta(days=current_day)) + timedelta(days=6)).strftime("%Y-%m-%d")

            return [week_start, week_end]

        elif "Month" in period:
            month = today.month
            year = today.year

            if "Next" in period:
                if month == 12:
                    month = 1
                    year += 1
                else:
                    month += 1

            num_of_days = calendar.monthrange(year, month)[1]
            month_start = datetime(year, month, 1).strftime("%Y-%m-%d")
            month_end = datetime(year, month, num_of_days).strftime("%Y-%m-%d")

            return [month_start, month_end]


    layout = [
        [sg.Text("Pick a time period:"), sg.Combo(time_periods, default_value="This Week", key="-PERIOD-", size=(31, 1)), Button("Find"), Button("Close")],
        ScheduleTable("-SCHEDULE-", 16)   
    ]


    window = sg.Window("Pick a time period", layout)
    

    while True:
        event, values = window.read()
        if event == "Close" or event == sg.WINDOW_CLOSED:
            break

        elif event == "Find":
            period = window["-PERIOD-"].get()
            if period == "All":
                appointments = AppointmentsController(con, cursor).find_all()["appointments"]

            else:
                start_date, end_date = get_start_and_end_dates(period)
                appointments = AppointmentsController(con, cursor).find_many_per_time_period(start_date, end_date)["appointments"]

            if len(appointments) == 0:
                sg.popup_ok("You have no appointments for the selected time period.")
            else:
                appointments = [appointment[1:] for appointment in appointments]
                window["-SCHEDULE-"].update(appointments)
                
    
    window.close()