class Procedure:

    def __init__(self, procedure_name, procedure_date, practioner_name, charges, patient_ID):
        self.procedure_name = procedure_name
        self.procedure_date = procedure_date
        self.practioner_name = practioner_name
        self.charges = charges
        self.patient_ID = patient_ID


    def set_procedure_name(self, procedure_name):
        self.procedure_name = procedure_name

    def set_procedure_date(self, procedure_date):
        self.procedure_date = procedure_date

    def set_practioner_name(self, practioner_name):
        self.practioner_name = practioner_name

    def set_charges(self,charges):
        self.charges = charges

    def set_patient_ID(self,patient_ID):
        self.patient_ID = patient_ID

    def get_procedure_name(self):
        return self.procedure_name

    def get_procedure_date(self):
        return self.procedure_date
    
    def get_practioner_name(self):
        return self.practioner_name

    def get_charges(self):
        return self.charges
    
    def get_patient_ID(self):
        return self.patient_ID

