from Doctor import Doctor

class DoctorManager:

    def __init__(self):
        """Initialize empty list of doctors and load from file."""
        self.doctors = []
        self.read_doctors_file()
    
    def format_dr_info(self, doctor):
        """Format doctor object information for file storage."""
        return str(doctor)
    
    def enter_dr_info(self):
        """Prompt user to enter doctor information and return doctor object."""
        doctor_id = input("Enter the doctor's ID: ")
        name = input("Enter the doctor's name: ")
        speciality = input("Enter the doctor's specility: ")
        timing = input("Enter the doctor's timing (e.g., 7am-10pm): ")
        qualification = input("Enter the doctor's qualification: ")
        room_number = input("Enter the doctor's room number: ")
        
        return Doctor(doctor_id, name, speciality, timing, qualification, room_number)
    
    def read_doctors_file(self):
        """Read doctors data from doctors.txt and create doctor objects."""
        try:
            with open("doctors.txt", "r") as file:
                lines = file.readlines()
                for i in range(len(lines)):
                    if i == 0:
                        continue
                    
                    line = lines[i].strip()
                    if line:
                        parts = line.split("_")
                        if len(parts) == 6:
                            doctor = Doctor(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5])
                            self.doctors.append(doctor)
        except FileNotFoundError:
            pass
    
    def search_doctor_by_id(self):
        """Search for a doctor by ID and display information."""
        doctor_id = input("\nEnter the doctor Id: ")
        
        found = False
        for doctor in self.doctors:
            if doctor.get_doctor_id() == doctor_id:
                self.display_doctor_info(doctor)
                found = True
                break
        
        if not found:
            print("Can't find the doctor with the same ID on the system\n")
    
    def search_doctor_by_name(self):
        """Search for a doctor by name and display information."""
        name = input("\nEnter the doctor name: ")
        
        found = False
        for doctor in self.doctors:
            if doctor.get_name() == name:
                self.display_doctor_info(doctor)
                found = True
                break
        
        if not found:
            print("Can't find the doctor with the same name on the system\n")
    
    def display_doctor_info(self, doctor):
        """Display formatted doctor information."""
        print("\n{:<5}{:<23}{:<16}{:<16}{:<16}{:<16}".format("Id", "Name", "Speciality", "Timing", "Qualification", "Room Number"))
        print()
        print("{:<5}{:<23}{:<16}{:<16}{:<16}{:<16}".format(
            doctor.get_doctor_id(),
            doctor.get_name(),
            doctor.get_speciality(),
            doctor.get_timing(),
            doctor.get_qualification(),
            doctor.get_room_number()
        ))
        print()
    
    def edit_doctor_info(self):
        """Edit existing doctor information."""
        doctor_id = input("\nPlease enter the id of the doctor that you want to edit their information: ")
        
        found = False
        for doctor in self.doctors:
            if doctor.get_doctor_id() == doctor_id:
                name = input("Enter new Name: ")
                speciality = input("Enter new Specilist in: ")
                timing = input("Enter new Timing: ")
                qualification = input("Enter new Qualification: ")
                room_number = input("Enter new Room number: ")
                
                doctor.set_name(name)
                doctor.set_speciality(speciality)
                doctor.set_timing(timing)
                doctor.set_qualification(qualification)
                doctor.set_room_number(room_number)
                
                self.write_list_of_doctors_to_file()
                print(f"\nDoctor whose ID is {doctor_id} has been edited\n")
                found = True
                break
        
        if not found:
            print("Cannot find the doctor with the same ID on the system\n")
    
    def display_doctors_list(self):
        """Display all doctors in formatted table."""
        print("{:<5}{:<23}{:<16}{:<16}{:<16}{:<16}".format("Id", "Name", "Speciality", "Timing", "Qualification", "Room Number"))
        print()
        
        for doctor in self.doctors:
            print("{:<5}{:<23}{:<16}{:<16}{:<16}{:<16}".format(
                doctor.get_doctor_id(),
                doctor.get_name(),
                doctor.get_speciality(),
                doctor.get_timing(),
                doctor.get_qualification(),
                doctor.get_room_number()
            ))
            print()
    
    def write_list_of_doctors_to_file(self):
        """Write all doctors to doctors.txt file."""
        with open("doctors.txt", "w") as file:
            file.write("id_name_specilist_timing_qualification_roomNb\n")
            for doctor in self.doctors:
                formatted = self.format_dr_info(doctor)
                file.write(formatted + "\n")
    
    def add_dr_to_file(self):
        """Add a new doctor to the system."""
        new_doctor = self.enter_dr_info()
        self.doctors.append(new_doctor)
        
        with open("doctors.txt", "a") as file:
            formatted = self.format_dr_info(new_doctor)
            file.write(formatted + "\n")
        
        print(f"\nDoctor whose ID is {new_doctor.get_doctor_id()} has been added\n")