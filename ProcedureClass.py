class Procedure:

    def __init__(self, procedure_name, procedure_date, practioner_name, charges, patient_ID):
        self.__procedure_name = procedure_name
        self.__procedure_date = procedure_date
        self.__practioner_name = practioner_name
        self.__charges = charges
        self.__patient_ID = patient_ID

    def set_patient_ID(self,patient_ID):
        self.__patient_ID = patient_ID

    def get_procedure_name(self):
        return self.__procedure_name

    def get_procedure_date(self):
        return self.__procedure_date
    
    def get_practioner_name(self):
        return self.__practioner_name

    def get_charges(self):
        return self.__charges
    
    def get_patient_ID(self):
        return self.__patient_ID

