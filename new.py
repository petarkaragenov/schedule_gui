import PySimpleGUI as sg
from defaults import today, m, d, y
from appointments_controller import AppointmentsController
from db import con, cursor



def new_appointment():
    left_col = [
        [sg.Text("Event:")],
        [sg.Text("Place:")],
        [sg.Text("Time:")],
        [sg.Text("Date:")],
        [sg.Text("Additional:")]
    ]

    right_col = [
        [sg.In(key="-EVENT-", size=(25, 1))],
        [sg.In(key="-PLACE-", size=(25, 1))],
        [sg.In(key="-TIME-", size=(25, 1))],
        [sg.In(today.strftime("%Y-%m-%d"), key="-DATE-", size=(20, 1)), sg.CalendarButton("", target="-DATE-", format="%Y-%m-%d", default_date_m_d_y=(m, d, y), image_filename="calendar.png", no_titlebar=False,  button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)],
        [sg.In(key="-OTHER-", size=(25, 1))]
    ]


    layout = [
        [sg.Column(left_col), sg.Column(right_col)],
        [sg.Button("Save", expand_x=True), sg.Button("Close", expand_x=True)]
    ]


    window = sg.Window("New Appointment", layout)


    while True:
        event, values = window.read()
        if event == "Close" or event == sg.WINDOW_CLOSED:
            break
        elif event == "Save":
            data = {
                "event": values["-EVENT-"],
                "place": values["-PLACE-"],
                "time": values["-TIME-"],
                "date": values["-DATE-"],
                "other": values["-OTHER-"],
            }

            appointment = AppointmentsController(con, cursor).create(data)

            if appointment["success"]:
                sg.popup_ok(appointment["msg"])

                break
            else:
                sg.popup_error(appointment["msg"])


    window.close()