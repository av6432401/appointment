

from flask import Flask, jsonify, request
from models import Doctor, Appointment

app = Flask(__name__)

doctors = [
    Doctor(1, "Dr. Smith", ["2023-10-02 18:00", "2023-10-02 19:00"]),
    Doctor(2, "Dr. Johnson", ["2023-10-03 18:00", "2023-10-03 19:00"]),
]

appointments = []

@app.route('/doctors', methods=['GET'])
def get_doctors():
    return jsonify([doctor.__dict__ for doctor in doctors])

@app.route('/doctors/<int:doctor_id>', methods=['GET'])
def get_doctor(doctor_id):
    doctor = next((doctor for doctor in doctors if doctor.id == doctor_id), None)
    if doctor:
        return jsonify(doctor.__dict__)
    return jsonify({'message': 'Doctor not found'}), 404

@app.route('/appointments', methods=['POST'])
def book_appointment():
    data = request.get_json()
    doctor_id = data.get('doctor_id')
    date = data.get('date')
    time = data.get('time')

    doctor = next((doctor for doctor in doctors if doctor.id == doctor_id), None)

    if not doctor:
        return jsonify({'message': 'Doctor not found'}), 404

    if f"{date} {time}" not in doctor.available_slots:
        return jsonify({'message': 'Slot not available'}), 400

    appointment_id = len(appointments) + 1
    appointment = Appointment(appointment_id, doctor_id, date, time)
    appointments.append(appointment)

    # Remove booked slot from available slots
    doctor.available_slots.remove(f"{date} {time}")

    return jsonify(appointment.__dict__), 201

if __name__ == '__main__':
    app.run(debug=True)
