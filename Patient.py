class Patient:
    
    def __init__(self, pid="", name="", disease="", gender="", age=""):
        self.__pid = pid
        self.__name = name
        self.__disease = disease
        self.__gender = gender
        self.__age = age
    
    # Getters
    def get_pid(self):
        return self.__pid
    
    def get_name(self):
        return self.__name
    
    def get_disease(self):
        return self.__disease
    
    def get_gender(self):
        return self.__gender
    
    def get_age(self):
        return self.__age
    
    # Setters
    def set_pid(self, new_pid):
        self.__pid = new_pid
    
    def set_name(self, new_name):
        self.__name = new_name
    
    def set_disease(self, new_disease):
        self.__disease = new_disease
    
    def set_gender(self, new_gender):
        self.__gender = new_gender
    
    def set_age(self, new_age):
        self.__age = new_age
    
    def __str__(self):
        return f"{self.__pid}_{self.__name}_{self.__disease}_{self.__gender}_{self.__age}"