import PySimpleGUI as sg
from helpers.defaults import empty_table, table_headings, col_widths, m, d, y


def Button(text):
    return sg.Button(text, size=(10, 1))

def ScheduleTable(key, rows):
    return [sg.Table(values=empty_table, headings=table_headings, key=key, col_widths=col_widths, auto_size_columns=False, enable_events=True, num_rows=rows, pad=(5, 10))]

def Calendar(target):
    return sg.CalendarButton("", target=target, button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename="files/calendar.png", border_width=0, default_date_m_d_y=(m, d, y), no_titlebar=False, format=("%Y-%m-%d"))
