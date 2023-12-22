import json
from datetime import datetime

class HospitalManagementSystem:
    def __init__(self):
        self.patients = []
        self.doctors = []

    def add_patient(self, name, age, gender):
        patient_id = len(self.patients) + 1
        patient = {'id': patient_id, 'name': name, 'age': age, 'gender': gender, 'admission_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        self.patients.append(patient)
        print(f"Patient {name} added with ID {patient_id}")

    def add_doctor(self, name, specialization):
        doctor_id = len(self.doctors) + 1
        doctor = {'id': doctor_id, 'name': name, 'specialization': specialization}
        self.doctors.append(doctor)
        print(f"Doctor {name} added with ID {doctor_id}")

    def view_patients(self):
        print("\nList of Patients:")
        for patient in self.patients:
            print(f"ID: {patient['id']}, Name: {patient['name']}, Age: {patient['age']}, Gender: {patient['gender']}, Admission Date: {patient['admission_date']}")

    def view_doctors(self):
        print("\nList of Doctors:")
        for doctor in self.doctors:
            print(f"ID: {doctor['id']}, Name: {doctor['name']}, Specialization: {doctor['specialization']}")


def main():
    hospital_system = HospitalManagementSystem()

    while True:
        print("\nOptions:")
        print("1. Add Patient")
        print("2. Add Doctor")
        print("3. View Patients")
        print("4. View Doctors")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter patient's name: ")
            age = input("Enter patient's age: ")
            gender = input("Enter patient's gender: ")
            hospital_system.add_patient(name, age, gender)

        elif choice == '2':
            name = input("Enter doctor's name: ")
            specialization = input("Enter doctor's specialization: ")
            hospital_system.add_doctor(name, specialization)

        elif choice == '3':
            hospital_system.view_patients()

        elif choice == '4':
            hospital_system.view_doctors()

        elif choice == '5':
            print("Exiting the Hospital Management System. Thank you!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
