import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import popup_ok
from defaults import m, d, y, empty_table
from find import find_appointments_by_date
from new import new_appointment


def main():
    col_left = [
        [
            sg.Text("Pick a Date:"), 
            sg.In(key="-DATE-", enable_events=True),
            sg.CalendarButton("", target="-DATE-", button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename="calendar.png", border_width=0, default_date_m_d_y=(m, d, y), no_titlebar=False, format=("%Y-%m-%d")),
            sg.Button("Find", size=(10, 1))
        ],
        [
            sg.Table(values=empty_table, headings=["Event", "Place", "Time", "Date", "Additional"], key="-SCHEDULE-", col_widths=[8, 16, 5, 10, 20], auto_size_columns=False)
        ]
    ]

    col_right = [
        [sg.Button("New", size=(10, 1))],
        [sg.Button("Update", size=(10, 1))],
        [sg.Button("Delete", size=(10, 1))],
        [sg.Button("Clear", size=(10, 1))],
        [sg.Button("Close", size=(10, 1))]
    ]


    layout = [
        [sg.Col(col_left), sg.Col(col_right)]
    ]


    window = sg.Window("Schedule", layout, finalize=True)


    while True:
        event, values = window.read()
        if event == "Close" or event == sg.WINDOW_CLOSED:
            break

        if event == "New":
            new_appointment()

        if event == "Find":
            res = find_appointments_by_date(values["-DATE-"])

            if len(res["appointments"]) == 0:
                popup_ok("You have no appointments for the given day.")
            else:
                appointments = [appointment[1:] for appointment in res["appointments"]]
                window["-SCHEDULE-"].update(appointments, alternating_row_color="#00468b")


    window.close()
    