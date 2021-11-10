from datetime import datetime

today = datetime.now()
m = today.month
d = today.day
y = today.year

empty_table = [["", "", "", "", ""]]
table_headings = ["Event", "Place", "Time", "Date", "Additional"]
col_widths = [8, 16, 5, 10, 20]

time_periods = ["This Week", "Next Week", "This Month", "Next Month", "All"]
