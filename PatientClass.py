#  PatientClass.py - Write a class named Patient that has the following attributes - ID, name, address, phone, veteran_status (True or False).
#  The Patient class’s __init__ method should accept an argument for each attribute. The Patient class should have accessor methods only for each attribute.



class Patient:
    
    def __init__(self, ID, name, address, phone, veteran_status):
        self.ID = ID
        self.name = name
        self.name = address
        self.phone = phone
        self.veteran_status = veteran_status

        print("Patient ID: ", self.ID)
        print("Patient Name: ", self.name)
        print("Patient Address: ", self.address)
        print("Patient Phone: ", self.phone)
        print("Patient Veteran Status: ", self.veteran_status)