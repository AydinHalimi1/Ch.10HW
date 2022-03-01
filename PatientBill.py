import PatientClass as p
import ProcedureClass as pr

def main():
    Id = 1
    Name = "Matt Jones"
    Address = "123 Main st, Waco TX 76706"
    Phone = "254-555-7415"
    Veteran_Status = True

    Pat = p.patient(Id,Name,Address,Phone,Veteran_Status)

    Pat.get__id()
    Pat.get__Name()
    Pat.get__Address()
    Pat.get__Phone()
    Pat.get__Vet()
    

    Procedure = "Physical Exam"
    Date = "2/15/2022"
    Practitioner = "Dr. Irvine"
    Charge = 250
    PatID = 1

    Procedure1 = pr.Procedure(Procedure,Date,Practitioner,Charge,PatID)

    Procedure1.get_Name()
    Procedure1.get_Date()
    Procedure1.get_Practitioner()
    Procedure1.get_Charges()
    Procedure1.get_PatID()
    

    Procedure = "MRI"
    Date = "2/15/2022"
    Practitioner = "Dr. Hamilton"
    Charge = 1500
    PatID = 1

    Procedure2 = pr.Procedure(Procedure,Date,Practitioner,Charge,PatID)

    Procedure2.get_Name()
    Procedure2.get_Date()
    Procedure2.get_Practitioner()
    Procedure2.get_Charges()
    Procedure2.get_PatID()


    Procedure = "CT Scan"
    Date = "2/17/2022"
    Practitioner = "Dr. Drey"
    Charge = 1200
    PatID = 2

    Procedure3 = pr.Procedure(Procedure,Date,Practitioner,Charge,PatID)

    Procedure3.get_Name()
    Procedure3.get_Date()
    Procedure3.get_Practitioner()
    Procedure3.get_Charges()
    Procedure3.get_PatID()
    

    print("*** Patient Bill ***")
    print("Name:",Pat.get__Name())
    print("Address:",Pat.get__Address())
    print("Phone:",Pat.get__Phone())
    print()

    total_charge = 0
    if Pat.get__id() == Procedure1.get_PatID():
        print("Name:",Procedure1.get_Name())
        print("Date:",Procedure1.get_Date())
        print("Practitioner:",Procedure1.get_Practitioner())
        print("Charge:","${:.2f}".format(Procedure1.get_Charges()))
        print()

        total_charge += Procedure1.get_Charges()
    if Pat.get__id() == Procedure2.get_PatID():
        print("Name:",Procedure2.get_Name())
        print("Date:",Procedure2.get_Date())
        print("Practitioner:",Procedure2.get_Practitioner())
        print("Charge:","${:.2f}".format(Procedure2.get_Charges()))
        print()

        total_charge += Procedure2.get_Charges()
    if Pat.get__id() == Procedure3.get_PatID():
        print("Name:",Procedure3.get_Name())
        print("Date:",Procedure3.get_Date())
        print("Practitioner:",Procedure3.get_Practitioner())
        print("Charge:","${:.2f}".format(Procedure3.get_Charges()))
        print()

        total_charge += Procedure3.get_Charges()

    if Pat.get__Vet() == True:
        total_charge *= .60
    else:
        total_charge
    print("Total Charges:", "${:.2f}".format(total_charge))


main()