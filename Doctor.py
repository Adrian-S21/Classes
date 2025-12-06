class Doctor:
    
    def __init__(self, doctor_id="", name="", speciality="", timing="", qualification="", room_number=""):
        """Initialize doctor object with given attributes."""
        self.__doctor_id = doctor_id
        self.__name = name
        self.__speciality = speciality
        self.__timing = timing
        self.__qualification = qualification
        self.__room_number = room_number
    
    # Getter
    def get_doctor_id(self):
        """Return the doctor's ID."""
        return self.__doctor_id
    
    def get_name(self):
        """Return the doctor's name."""
        return self.__name
    
    def get_speciality(self):
        """Return the doctor's speciality."""
        return self.__speciality
    
    def get_timing(self):
        """Return the doctor's working hours."""
        return self.__timing
    
    def get_qualification(self):
        """Return the doctor's qualifications."""
        return self.__qualification
    
    def get_room_number(self):
        """Return the doctor's room number."""
        return self.__room_number
    
    # Setter
    def set_doctor_id(self, new_id):
        """Set the doctor's ID."""
        self.__doctor_id = new_id
    
    def set_name(self, new_name):
        """Set the doctor's name."""
        self.__name = new_name
    
    def set_speciality(self, new_speciality):
        """Set the doctor's speciality."""
        self.__speciality = new_speciality
    
    def set_timing(self, new_timing):
        """Set the doctor's working hours."""
        self.__timing = new_timing
    
    def set_qualification(self, new_qualification):
        """Set the doctor's qualifications."""
        self.__qualification = new_qualification
    
    def set_room_number(self, new_room_number):
        """Set the doctor's room number."""
        self.__room_number = new_room_number
    
    def __str__(self):
        """Return string representation of doctor object."""
        return f"{self.__doctor_id}_{self.__name}_{self.__speciality}_{self.__timing}_{self.__qualification}_{self.__room_number}"