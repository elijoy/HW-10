# ProcedureClass.py - write a class named Procedure that represents a medical procedure that has been performed on a patient. 
# The Procedure class should have the following attributes - Name of the procedure, Date of the procedure, Name of the practitioner who performed the procedure, Charges for
# the procedure and patient ID. The Procedure class’s __init__ method should accept an argument for each attribute. 
# The Procedure class should have accessor methods only for each attribute.

class Procedure:

    def __init__(self, procedure_name, procedure_date, practioner_name, charges, patient_ID):
        self.procedure_name = procedure_name
        self.procedure_date = procedure_date
        self.practioner_name = practioner_name
        self.charges = charges
        self.patient_ID = patient_ID


        print("Procedure Name: ", self.procedure_name)
        print("Procedure Date: ", self.procedure_date)
        print("Practioner Name: ", self.practioner_name)
        print("Charges: ", self.charges)
        print("Patient ID", self.patient_ID)