import PySimpleGUI as sg
from helpers.defaults import m, d, y, empty_table, table_headings, col_widths
from views.find import find_appointments_by_date, find_appointments_by_id
from views.find_more import find_more
from views.new import new_appointment
from views.delete import delete_appointment


sg.theme("DarkBrown2")


def main():
    def clear_inputs(window):
        window["-SCHEDULE-"].update(empty_table, alternating_row_color=sg.theme_background_color())
        window["-DATE-"].update("")


    appointment_idx = None
    selected_appointment = None


    col_left_top = [
        [
            sg.Text("Pick a Date:"), 
            sg.In(key="-DATE-", enable_events=True, size=(45, 1)),
            sg.CalendarButton("", target="-DATE-", button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename="files/calendar.png", border_width=0, default_date_m_d_y=(m, d, y), no_titlebar=False, format=("%Y-%m-%d")),
            sg.Button("Find", size=(10, 1)),
        ]
    ]

    col_right_top = [[sg.Button("Find More", size=(10, 1))]]


    col_left_bottom = [
        [
            sg.Table(values=empty_table, headings=table_headings, key="-SCHEDULE-", col_widths=col_widths, auto_size_columns=False, enable_events=True, num_rows=8, pad=(5, 10))
        ]
    ]

    col_right_bottom = [
        [sg.Button("New", size=(10, 1))],
        [sg.Button("Update", size=(10, 1))],
        [sg.Button("Delete", size=(10, 1))],
        [sg.Button("Clear", size=(10, 1))],
        [sg.Button("Close", size=(10, 1))]
    ]


    layout = [
        [sg.Col(col_left_top), sg.VerticalSeparator(color="#240808"), sg.Col(col_right_top)],
        [sg.Col(col_left_bottom), sg.Col(col_right_bottom)]
    ]


    window = sg.Window("Schedule", layout, finalize=True)


    while True:
        event, values = window.read()
        if event == "Close" or event == sg.WINDOW_CLOSED:
            break

        elif event == "Find More":
            find_more()

        elif event == "New":
            new_appointment()

        elif event == "Find":
            res = find_appointments_by_date(values["-DATE-"])

            if len(res["appointments"]) == 0:
                sg.popup_ok("You have no appointments for the given day.")
            else:
                appointment_idx = [appointment[0] for appointment in res["appointments"]]
                appointments = [appointment[1:] for appointment in res["appointments"]]
                window["-SCHEDULE-"].update(appointments, alternating_row_color="#e1bd53")
        
        elif event == "-SCHEDULE-":
            if window["-SCHEDULE-"].get() == empty_table:
                pass
            else:
                idx_selected = values["-SCHEDULE-"][0]
                appointment = find_appointments_by_id(appointment_idx[idx_selected])["appointments"]
                selected_appointment = {
                    "id": appointment[0],
                    "event": appointment[1],
                    "place": appointment[2],
                    "time": appointment[3],
                    "date": appointment[4],
                    "other": appointment[5]
                }
            
        elif event == "Update":
            if selected_appointment is None:
                sg.popup_ok("You have to select an appointment")
            else:
                new_appointment(selected_appointment)

        elif event == "Delete":
            if selected_appointment is None:
                sg.popup_ok("You have to select an appointment")
            else:
                b = sg.popup_ok_cancel("Are you sure you want to delete this appointment?")
                if b == "OK":
                    res = delete_appointment(selected_appointment["id"])
                    if res["success"]:
                        sg.popup_ok(res["msg"])
                else:
                    pass

        elif event == "Clear":
            clear_inputs(window)
            appointment_idx = None
            selected_appointment = None



    window.close()
    