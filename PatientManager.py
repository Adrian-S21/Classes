from Patient import Patient

class PatientManager:
    """
    PatientManager class to manage all patient operations.
    Handles reading, writing, searching, adding, and editing patients.
    """
    
    def __init__(self):
        """Initialize empty list of patients and load from file."""
        self.patients = []
        self.read_patients_file()
    
    def format_patient_info_for_file(self, patient):
        """Format patient object information for file storage."""
        return str(patient)
    
    def enter_patient_info(self):
        """Prompt user to enter patient information and return patient object."""
        pid = input("Enter Patient id: ")
        name = input("Enter Patient name: ")
        disease = input("Enter Patient disease: ")
        gender = input("Enter Patient gender: ")
        age = input("Enter Patient age: ")
        
        return Patient(pid, name, disease, gender, age)
    
    def read_patients_file(self):
        """Read patients data from patients.txt and create patient objects."""
        try:
            with open("patients.txt", "r") as file:
                lines = file.readlines()
                for i in range(len(lines)):
                    if i == 0:
                        continue
                    
                    line = lines[i].strip()
                    if line:
                        parts = line.split("_")
                        if len(parts) == 5:
                            patient = Patient(parts[0], parts[1], parts[2], parts[3], parts[4])
                            self.patients.append(patient)
        except FileNotFoundError:
            pass
    
    def search_patient_by_id(self):
        """Search for a patient by ID and display information."""
        pid = input("\nEnter the Patient Id: ")
        
        found = False
        for patient in self.patients:
            if patient.get_pid() == pid:
                self.display_patient_info(patient)
                found = True
                break
        
        if not found:
            print("Can't find the Patient with the same id on the system\n")
    
    def display_patient_info(self, patient):
        """Display formatted patient information."""
        print("\n{:<5}{:<23}{:<16}{:<16}{:<16}".format("ID", "Name", "Disease", "Gender", "Age"))
        print()
        print("{:<5}{:<23}{:<16}{:<16}{:<16}".format(
            patient.get_pid(),
            patient.get_name(),
            patient.get_disease(),
            patient.get_gender(),
            patient.get_age()
        ))
        print()
    
    def edit_patient_info_by_id(self):
        """Edit existing patient information."""
        pid = input("\nPlease enter the id of the Patient that you want to edit their information: ")
        
        found = False
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
                print(f"\nPatient whose ID is {pid} has been edited.\n")
                found = True
                break
        
        if not found:
            print("Cannot find the patient with the same ID on the system\n")
    
    def display_patients_list(self):
        """Display all patients in formatted table."""
        print("{:<5}{:<23}{:<16}{:<16}{:<16}".format("ID", "Name", "Disease", "Gender", "Age"))
        print()
        
        for patient in self.patients:
            print("{:<5}{:<23}{:<16}{:<16}{:<16}".format(
                patient.get_pid(),
                patient.get_name(),
                patient.get_disease(),
                patient.get_gender(),
                patient.get_age()
            ))
            print()
    
    def write_list_of_patients_to_file(self):
        """Write all patients to patients.txt file."""
        with open("patients.txt", "w") as file:
            file.write("id_Name_Disease_Gender_Age\n")
            for patient in self.patients:
                formatted = self.format_patient_info_for_file(patient)
                file.write(formatted + "\n")
    
    def add_patient_to_file(self):
        """Add a new patient to the system."""
        new_patient = self.enter_patient_info()
        self.patients.append(new_patient)
        
        with open("patients.txt", "a") as file:
            formatted = self.format_patient_info_for_file(new_patient)
            file.write(formatted + "\n")
        
        print(f"\nPatient whose ID is {new_patient.get_pid()} has been added.\n")