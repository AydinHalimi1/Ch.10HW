import PatientClass as p
import ProcedureClass as pr

def main():
    Id = 1
    Name = "Matt Jones"
    Address = "123 Main st, Waco TX 76706"
    Phone = "254-555-7415"
    Veteran_Status = True

    Pat = p.patient(Id,Name,Address,Phone,Veteran_Status)

    print("ID:",Pat.get_id())
    print("Name:",Pat.get_Name())
    print("Address:",Pat.get_Address())
    print("Phone:",Pat.get_Phone())
    print("Veteran:",Pat.get_Vet())
    print()

    Procedure = "Physical Exam"
    Date = "2/15/2022"
    Practitioner = "Dr. Irvine"
    Charge = 250
    PatID = 1

    Procedure1 = pr.Procedure(Procedure,Date,Practitioner,Charge,PatID)

    print("Name:",Procedure1.get_Name())
    print("Date:",Procedure1.get_Date())
    print("Practitioner:",Procedure1.get_Practitioner())
    print("Charge:",Procedure1.get_Charge())
    print("Patient ID:",Procedure1.get_PatID())
    print()

    Procedure = "MRI"
    Date = "2/15/2022"
    Practitioner = "Dr. Hamilton"
    Charge = 1500
    PatID = 1

    Procedure2 = pr.Procedure(Procedure,Date,Practitioner,Charge,PatID)

    print("Name:",Procedure2.get_Name())
    print("Date:",Procedure2.get_Date())
    print("Practitioner:",Procedure2.get_Practitioner())
    print("Charge:",Procedure2.get_Charge())
    print("Patient ID:",Procedure2.get_PatID())
    print()

    Procedure = "CT Scan"
    Date = "2/17/2022"
    Practitioner = "Dr. Drey"
    Charge = 1200
    PatID = 2

    Procedure3 = pr.Procedure(Procedure,Date,Practitioner,Charge,PatID)

    print("Name:",Procedure3.get_Name())
    print("Date:",Procedure3.get_Date())
    print("Practitioner:",Procedure3.get_Practitioner())
    print("Charge:",Procedure3.get_Charge())
    print("Patient ID:",Procedure3.get_PatID())
    print()

    print("*** Patient Bill ***")
    print("Name:",Pat.get__Name())
    print("Address:",Pat.get__Address())
    print("Phone:",Pat.get__Phone())
    print()

    total_charge = 0
    if Pat.get_id() == Procedure1.get_PatID():
        print("Name:",Procedure1.get_Name())
        print("Date:",Procedure1.get_Date())
        print("Practitioner:",Procedure1.get_Practitioner())
        print("Charge:",Procedure1.get_Charges())
        print()

        total_charge += Procedure1.get_Charges()
    if Pat.get_id() == Procedure2.get_PatID():
        print("Name:",Procedure2.get_Name())
        print("Date:",Procedure2.get_Date())
        print("Practitioner:",Procedure2.get_Practitioner())
        print("Charge:",Procedure2.get_Charges())
        print()

        total_charge += Procedure2.get_Charges()
    if Pat.get_id() == Procedure3.get_PatID():
        print("Name:",Procedure3.get_Name())
        print("Date:",Procedure3.get_Date())
        print("Practitioner:",Procedure3.get_Practitioner())
        print("Charge:",Procedure3.get_Charges())
        print()

        total_charge += Procedure3.get_Charges()

    if Pat.get_veteran() == True:
        total_charge *= .60
    else:
        total_charge
    print("Total Charges:", "${:.2f}".format(total_charge))


main()