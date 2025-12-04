"""
Alberta Hospital Management System
Date: December 2024
Description: A hospital management system that allows users to manage doctors and patients.
The system provides functionality to add, search, edit, and display information for both
doctors and patients. Data is stored in text files (doctors.txt and patients.txt).

Input: User menu selections and data entry for doctors/patients
Processing: File I/O operations, data validation, searching, and updating records
Output: Formatted displays of doctor/patient information and system messages
"""

# ===========================
# Class #1: Doctor
# ===========================
class Doctor:
    """Represents a doctor with their professional information"""
    
    def __init__(self, doctor_id="", name="", specialization="", timing="", qualification="", room_number=""):
        """Initialize doctor object with default or provided values"""
        self.__doctor_id = doctor_id
        self.__name = name
        self.__specialization = specialization
        self.__timing = timing
        self.__qualification = qualification
        self.__room_number = room_number
    
    # Getters
    def get_doctor_id(self):
        """Returns the doctor ID"""
        return self.__doctor_id
    
    def get_name(self):
        """Returns the doctor name"""
        return self.__name
    
    def get_specialization(self):
        """Returns the doctor specialization"""
        return self.__specialization
    
    def get_timing(self):
        """Returns the doctor working time"""
        return self.__timing
    
    def get_qualification(self):
        """Returns the doctor qualification"""
        return self.__qualification
    
    def get_room_number(self):
        """Returns the doctor room number"""
        return self.__room_number
    
    # Setters
    def set_doctor_id(self, new_id):
        """Sets the doctor ID"""
        self.__doctor_id = new_id
    
    def set_name(self, new_name):
        """Sets the doctor name"""
        self.__name = new_name
    
    def set_specialization(self, new_specialization):
        """Sets the doctor specialization"""
        self.__specialization = new_specialization
    
    def set_timing(self, new_timing):
        """Sets the doctor working time"""
        self.__timing = new_timing
    
    def set_qualification(self, new_qualification):
        """Sets the doctor qualification"""
        self.__qualification = new_qualification
    
    def set_room_number(self, new_room_number):
        """Sets the doctor room number"""
        self.__room_number = new_room_number
    
    def __str__(self):
        """Returns string representation of doctor object"""
        return f"{self.__doctor_id}_{self.__name}_{self.__specialization}_{self.__timing}_{self.__qualification}_{self.__room_number}"


# ===========================
# Class #2: DoctorManager
# ===========================
class DoctorManager:
    """Manages all doctor-related operations"""
    
    def __init__(self):
        """Initialize empty doctors list and load from file"""
        self.doctors = []
        self.read_doctors_file()
    
    def format_dr_info(self, doctor):
        """Formats doctor object info for file storage"""
        return str(doctor)
    
    def enter_dr_info(self):
        """Asks user to enter doctor info and returns doctor object"""
        print()
        doctor_id = input("Enter the doctor's ID: ")
        name = input("Enter the doctor's name: ")
        specialization = input("Enter the doctor's specility: ")
        timing = input("Enter the doctor's timing (e.g., 7am-10pm): ")
        qualification = input("Enter the doctor's qualification: ")
        room_number = input("Enter the doctor's room number: ")
        
        doctor = Doctor(doctor_id, name, specialization, timing, qualification, room_number)
        return doctor
    
    def read_doctors_file(self):
        """Reads doctors data from doctors.txt file"""
        file = open("doctors.txt", "r")
        lines = file.readlines()
        # Skip header line
        for i in range(1, len(lines)):
            line = lines[i].strip()
            if line:
                parts = line.split("_")
                if len(parts) == 6:
                    doctor = Doctor(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5])
                    self.doctors.append(doctor)
        file.close()
    
    def search_doctor_by_id(self):
        """Searches for a doctor by ID"""
        print()
        doctor_id = input("Enter the doctor Id: ")
        
        for doctor in self.doctors:
            if doctor.get_doctor_id() == doctor_id:
                self.display_doctor_info(doctor)
                return
        
        print(f"Can't find the doctor with the same ID on the system")
    
    def search_doctor_by_name(self):
        """Searches for a doctor by name"""
        print()
        name = input("Enter the doctor name: ")
        
        for doctor in self.doctors:
            if doctor.get_name() == name:
                self.display_doctor_info(doctor)
                return
        
        print(f"Can't find the doctor with the same name on the system")
    
    def display_doctor_info(self, doctor):
        """Displays formatted doctor information"""
        print(f"\nId   Name                   Speciality      Timing          Qualification   Room Number\n")
        print(f"{doctor.get_doctor_id():<5}{doctor.get_name():<23}{doctor.get_specialization():<16}{doctor.get_timing():<16}{doctor.get_qualification():<16}{doctor.get_room_number():<14}")
        print("       ")
    
    def edit_doctor_info(self):
        """Edits doctor information by ID"""
        print()
        doctor_id = input("Please enter the id of the doctor that you want to edit their information: ")
        
        for doctor in self.doctors:
            if doctor.get_doctor_id() == doctor_id:
                name = input("Enter new Name: ")
                specialization = input("Enter new Specilist in: ")
                timing = input("Enter new Timing: ")
                qualification = input("Enter new Qualification: ")
                room_number = input("Enter new Room number: ")
                
                doctor.set_name(name)
                doctor.set_specialization(specialization)
                doctor.set_timing(timing)
                doctor.set_qualification(qualification)
                doctor.set_room_number(room_number)
                
                self.write_list_of_doctors_to_file()
                print(f"\nDoctor whose ID is {doctor_id} has been edited")
                return
        
        print("Cannot find the doctor with the same ID on the system")
    
    def display_doctors_list(self):
        """Displays all doctors in formatted table"""
        print("Id   Name                   Speciality      Timing          Qualification   Room Number\n")
        for doctor in self.doctors:
            print(f"{doctor.get_doctor_id():<5}{doctor.get_name():<23}{doctor.get_specialization():<16}{doctor.get_timing():<16}{doctor.get_qualification():<16}{doctor.get_room_number():<14}")
            print("       ")
    
    def write_list_of_doctors_to_file(self):
        """Writes all doctors to doctors.txt file"""
        with open("doctors.txt", "w") as file:
            file.write("id_name_specilist_timing_qualification_roomNb\n")
            for doctor in self.doctors:
                file.write(self.format_dr_info(doctor) + "\n")
    
    def add_dr_to_file(self):
        """Adds a new doctor to the system"""
        doctor = self.enter_dr_info()
        self.doctors.append(doctor)
        
        with open("doctors.txt", "a") as file:
            file.write(self.format_dr_info(doctor) + "\n")
        
        print(f"\nDoctor whose ID is {doctor.get_doctor_id()} has been added")


# ===========================
# Class #3: Patient
# ===========================
class Patient:
    """Represents a patient with their medical information"""
    
    def __init__(self, pid="", name="", disease="", gender="", age=""):
        """Initialize patient object with default or provided values"""
        self.__pid = pid
        self.__name = name
        self.__disease = disease
        self.__gender = gender
        self.__age = age
    
    # Getters
    def get_pid(self):
        """Returns the patient ID"""
        return self.__pid
    
    def get_name(self):
        """Returns the patient name"""
        return self.__name
    
    def get_disease(self):
        """Returns the patient disease"""
        return self.__disease
    
    def get_gender(self):
        """Returns the patient gender"""
        return self.__gender
    
    def get_age(self):
        """Returns the patient age"""
        return self.__age
    
    # Setters
    def set_pid(self, new_pid):
        """Sets the patient ID"""
        self.__pid = new_pid
    
    def set_name(self, new_name):
        """Sets the patient name"""
        self.__name = new_name
    
    def set_disease(self, new_disease):
        """Sets the patient disease"""
        self.__disease = new_disease
    
    def set_gender(self, new_gender):
        """Sets the patient gender"""
        self.__gender = new_gender
    
    def set_age(self, new_age):
        """Sets the patient age"""
        self.__age = new_age
    
    def __str__(self):
        """Returns string representation of patient object"""
        return f"{self.__pid}_{self.__name}_{self.__disease}_{self.__gender}_{self.__age}"


# ===========================
# Class #4: PatientManager
# ===========================
class PatientManager:
    """Manages all patient-related operations"""
    
    def __init__(self):
        """Initialize empty patients list and load from file"""
        self.patients = []
        self.read_patients_file()
    
    def format_patient_info_for_file(self, patient):
        """Formats patient object info for file storage"""
        return str(patient)
    
    def enter_patient_info(self):
        """Asks user to enter patient info and returns patient object"""
        print()
        pid = input("Enter Patient id: ")
        name = input("Enter Patient name: ")
        disease = input("Enter Patient disease: ")
        gender = input("Enter Patient gender: ")
        age = input("Enter Patient age: ")
        
        patient = Patient(pid, name, disease, gender, age)
        return patient
    
    def read_patients_file(self):
        """Reads patients data from patients.txt file"""
        file = open("patients.txt", "r")
        lines = file.readlines()
        # Skip header line
        for i in range(1, len(lines)):
            line = lines[i].strip()
            if line:
                parts = line.split("_")
                if len(parts) == 5:
                    patient = Patient(parts[0], parts[1], parts[2], parts[3], parts[4])
                    self.patients.append(patient)
        file.close()
    
    def search_patient_by_id(self):
        """Searches for a patient by ID"""
        print()
        pid = input("Enter the Patient Id: ")
        
        for patient in self.patients:
            if patient.get_pid() == pid:
                self.display_patient_info(patient)
                return
        
        print(f"Can't find the Patient with the same id on the system")
    
    def display_patient_info(self, patient):
        """Displays formatted patient information"""
        print(f"\nID   Name\t\t    Disease\t    Gender\t    Age\n")
        print(f"{patient.get_pid():<5}{patient.get_name():<23}{patient.get_disease():<16}{patient.get_gender():<16}{patient.get_age():<15}")
        print("            ")
    
    def edit_patient_info_by_id(self):
        """Edits patient information by ID"""
        print()
        pid = input("Please enter the id of the Patient that you want to edit their information: ")
        
        for patient in self.patients:
            if patient.get_pid() == pid:
                name = input("Enter new Name: ")
                disease = input("Enter new disease: ")
                gender = input("Enter new gender: ")
                age = input("Enter new age: ")
                
                patient.set_name(name)
                patient.set_disease(disease)
                patient.set_gender(gender)
                patient.set_age(age)
                
                self.write_list_of_patients_to_file()
                print(f"\nPatient whose ID is {pid} has been edited.")
                return
        
        print("Cannot find the patient with the same ID on the system")
    
    def display_patients_list(self):
        """Displays all patients in formatted table"""
        print("ID   Name                   Disease         Gender          Age")
        print("           ")
        for patient in self.patients:
            print(f"{patient.get_pid():<5}{patient.get_name():<23}{patient.get_disease():<16}{patient.get_gender():<16}{patient.get_age():<15}")
            print("            ")
        print()
    
    def write_list_of_patients_to_file(self):
        """Writes all patients to patients.txt file"""
        with open("patients.txt", "w") as file:
            file.write("id_Name_Disease_Gender_Age\n")
            for patient in self.patients:
                file.write(self.format_patient_info_for_file(patient) + "\n")
    
    def add_patient_to_file(self):
        """Adds a new patient to the system"""
        patient = self.enter_patient_info()
        self.patients.append(patient)
        
        with open("patients.txt", "a") as file:
            file.write(self.format_patient_info_for_file(patient) + "\n")
        
        print(f"\nPatient whose ID is {patient.get_pid()} has been added.")


# ===========================
# Class #5: Management
# ===========================
class Management:
    """Main management class for displaying menus and controlling flow"""
    
    def __init__(self):
        """Initialize doctor and patient managers"""
        self.doctor_manager = DoctorManager()
        self.patient_manager = PatientManager()
    
    def display_menu(self):
        """Displays main menu and handles user navigation"""
        while True:
            print("\nWelcome to Alberta Hospital (AH) Managment system ")
            print("Select from the following options, or select 3 to stop: ")
            print("1 - \tDoctors")
            print("2 - \tPatients")
            print("3 -\tExit Program ")
            choice = input(">>> ")
            
            if choice == "1":
                self.doctors_menu()
            elif choice == "2":
                self.patients_menu()
            elif choice == "3":
                print("Thanks for using the program. Bye!")
                break
            else:
                print("Invalid choice. Please try again.")
    
    def doctors_menu(self):
        """Displays doctors submenu"""
        while True:
            print("\nDoctors Menu:")
            print("1 - Display Doctors list")
            print("2 - Search for doctor by ID")
            print("3 - Search for doctor by name")
            print("4 - Add doctor")
            print("5 - Edit doctor info")
            print("6 - Back to the Main Menu")
            
            choice = input(">>> ")
            
            if choice == "1":
                self.doctor_manager.display_doctors_list()
            elif choice == "2":
                self.doctor_manager.search_doctor_by_id()
            elif choice == "3":
                self.doctor_manager.search_doctor_by_name()
            elif choice == "4":
                self.doctor_manager.add_dr_to_file()
            elif choice == "5":
                self.doctor_manager.edit_doctor_info()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")
    
    def patients_menu(self):
        """Displays patients submenu"""
        while True:
            print("\nPatients Menu:")
            print("1 - Display patients list")
            print("2 - Search for patient by ID")
            print("3 - Add patient")
            print("4 - Edit patient info")
            print("5 - Back to the Main Menu")
            
            choice = input(">>> ")
            
            if choice == "1":
                self.patient_manager.display_patients_list()
            elif choice == "2":
                self.patient_manager.search_patient_by_id()
            elif choice == "3":
                self.patient_manager.add_patient_to_file()
            elif choice == "4":
                self.patient_manager.edit_patient_info_by_id()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")


# ===========================
# Main Program
# ===========================
if __name__ == "__main__":
    # Create management system and display menu
    management = Management()
    management.display_menu()