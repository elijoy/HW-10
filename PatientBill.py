import PatientClass as a
import ProcedureClass as b


def main():
        
    #variables/setting up everything
    # vet = True
    # NotVet = False
    Matt_Jones = a.Patient(1, "Matt Jones", "123 Main st, Waco TX 76706", "254-555-7415", True)
    Irvine = b.Procedure("Physical Exam", "2/15/2022", "Dr. Irvine", 250.00, 1)
    Hamilton = b.Procedure("MRI", "2/15/2022", "Dr. Hamilton", 1500, 1)
    Drey = b.Procedure("CT Scan", "2/17/2022", "Dr. Drey", 1200, 2)
    vet_discount = .4
    total = 0



    #Processing/Outputs
    print()
    print("*** Patient Bill ***")
    print("Name: ", Matt_Jones.get_name() +
    "\n" + "Address: ", Matt_Jones.get_address() +
    "\n" + "Phone: ", Matt_Jones.get_phone(), sep ='')

    if Matt_Jones.get_ID() == Irvine.get_patient_ID():
        print()
        print("Procedure: ", Irvine.get_procedure_name() +
              "\n" + "Date: ", Irvine.get_procedure_date() +
              "\n" + "Practitioner: ", Irvine.get_practioner_name() +
              "\n" + "Charge: $", format(Irvine.get_charges(), ',.2f'), sep='')
        total += float(Irvine.get_charges())


    if Matt_Jones.get_ID() == Hamilton.get_patient_ID():
        print()
        print("Procedure: ", Hamilton.get_procedure_name() +
              "\n" + "Date: ", Hamilton.get_procedure_date() +
              "\n" + "Practitioner: ", Hamilton.get_practioner_name() +
              "\n" + "Charge: $", format(Hamilton.get_charges(), ',.2f'), sep='')
        total += float(Hamilton.get_charges())

    if Matt_Jones.get_ID() == Drey.get_patient_ID():
        print()
        print("Procedure: ", Drey.get_procedure_name() +
              "\n" + "Date: ", Drey.get_procedure_date() +
              "\n" + "Practitioner: ", Drey.get_practioner_name() +
              "\n" + "Charge: $", format(Drey.get_charges(), ',.2f'), sep='')
        total += float(Drey.get_charges())

    discount = total * vet_discount
    # print(discount)
    # New_total = total - discount
    # print("Total Charges: $", format(New_total, ',.2f'), sep = '')

    if Matt_Jones.get_veteran_status() == True:
        print()
        New_total = total - discount
        print("Total Charges: $", format(New_total, ',.2f'), sep = '')
    else:
        print()
        print("Total Charges: $", format(total, ',.2f'), sep = '')


main()