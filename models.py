

class Doctor:
    def __init__(self, id, name, available_slots):
        self.id = id
        self.name = name
        self.available_slots = available_slots

class Appointment:
    def __init__(self, id, doctor_id, date, time):
        self.id = id
        self.doctor_id = doctor_id
        self.date = date
        self.time = time
