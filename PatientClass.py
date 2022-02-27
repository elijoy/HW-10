class Patient:
    
    def __init__(self, ID, name, address, phone, vet):
        self.ID = ID
        self.name = name
        self.address = address
        self.phone = phone
        self.veteran_status = vet

    def set_ID (self,ID):
        self.ID = ID

    def set_name(self,name):
        self.name = name

    def set_address(self,address):
        self.address = address
    
    def set_phone(self,phone):
        self.phone = phone

    def set_veteran_status(self, vet):
        self.veteran_status = vet

    def get_ID(self):
        return self.ID

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_phone(self):
        return self.phone

    def get_veteran_status(self):
        return self.get_veteran_status

