import re
from queries import create_table, create_appointment, find_appointments_by_date


class AppointmentsController():
    def __init__(self, con, cursor):
        self.con = con
        self.cursor = cursor


    @staticmethod
    def format_time(time):
        time = time.strip()
        time_pattern = r"(\d+):?(\d{2})?"

        if re.search(time_pattern, time) != None:
            time_groups = re.search(time_pattern, time)

            if int(time_groups.group(1)) > 23:
                raise ValueError("Could not parse time value.")

            if not time_groups.group(2):
                time = time_groups.group(1)
                time += ":00"
            else:
                time = f"{time_groups.group(1)}:{time_groups.group(2)}"
                print(time)

            if len(time.split(":")[0]) < 2:
                time = "0" + time

            return time

        else:
            raise ValueError("Could not parse time value.")


    def create(self, data):
        if data["event"] == "" or data["place"] == "" or data["time"] == "" or data["date"] == "":
            return { 
                "msg": "Please fill all required fields.",
                "success": False 
            }
        else:
            try:
                time = AppointmentsController.format_time(data["time"])
            except ValueError:
                return { 
                    "msg": "Could not parse time value.",
                    "success": False 
                }

            self.cursor.execute(create_appointment, (
                data["event"].title(),
                data["place"].title(),
                time,
                data["date"],
                data["other"]
            ))

            self.con.commit()

            return { 
                "msg": "Appointment added successfully!",
                 "success": True
            }


    def find_one(self, date):
        self.cursor.execute(find_appointments_by_date, (date,))
        appointments = self.cursor.fetchall()

        return {
            "appointments": appointments
        }
