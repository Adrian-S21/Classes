class Doctor:
    
    def __init__(self, doctor_id="", name="", speciality="", timing="", qualification="", room_number=""):
        self.__doctor_id = doctor_id
        self.__name = name
        self.__speciality = speciality
        self.__timing = timing
        self.__qualification = qualification
        self.__room_number = room_number
    
    # Getter
    def get_doctor_id(self):
        return self.__doctor_id
    
    def get_name(self):
        return self.__name
    
    def get_speciality(self):
        return self.__speciality
    
    def get_timing(self):
        return self.__timing
    
    def get_qualification(self):
        return self.__qualification
    
    def get_room_number(self):
        return self.__room_number
    
    # Setter
    def set_doctor_id(self, new_id):
        self.__doctor_id = new_id
    
    def set_name(self, new_name):
        self.__name = new_name
    
    def set_speciality(self, new_speciality):
        self.__speciality = new_speciality
    
    def set_timing(self, new_timing):
        self.__timing = new_timing
    
    def set_qualification(self, new_qualification):
        self.__qualification = new_qualification
    
    def set_room_number(self, new_room_number):
        self.__room_number = new_room_number
    
    def __str__(self):
        return f"{self.__doctor_id}_{self.__name}_{self.__speciality}_{self.__timing}_{self.__qualification}_{self.__room_number}"