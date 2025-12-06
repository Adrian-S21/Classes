class Patient:
    
    def __init__(self, pid="", name="", disease="", gender="", age=""):
        """Initialize patient object with given attributes."""
        self.__pid = pid
        self.__name = name
        self.__disease = disease
        self.__gender = gender
        self.__age = age
    
    # Getters
    def get_pid(self):
        """Return the patient's ID."""
        return self.__pid
    
    def get_name(self):
        """Return the patient's name."""
        return self.__name
    
    def get_disease(self):
        """Return the patient's disease."""
        return self.__disease
    
    def get_gender(self):
        """Return the patient's gender."""
        return self.__gender
    
    def get_age(self):
        """Return the patient's age."""
        return self.__age
    
    # Setters
    def set_pid(self, new_pid):
        """Set the patient's ID."""
        self.__pid = new_pid
    
    def set_name(self, new_name):
        """Set the patient's name."""
        self.__name = new_name
    
    def set_disease(self, new_disease):
        """Set the patient's disease."""
        self.__disease = new_disease
    
    def set_gender(self, new_gender):
        """Set the patient's gender."""
        self.__gender = new_gender
    
    def set_age(self, new_age):
        """Set the patient's age."""
        self.__age = new_age
    
    def __str__(self):
        """Return string representation of patient object."""
        return f"{self.__pid}_{self.__name}_{self.__disease}_{self.__gender}_{self.__age}"