class customersDC:
    def __init__(self):
        self.customerNAME = ""
        self.classiFICT = ""
        self.totalKWU = 0.0
        self.ratePKU = 0.0
        self.groAMT = 0.0
        self.misceCHAR = 0.0
        self.totalAMT = 0.0
        self.prevREADING = 0.0
        self.currREADING = 0.0
        self.meterID = 0

customersD = []

def main():
    while True:
        print("\n[ELECTRIC COMPANY]")
        print("1. Calculate Bill")
        print("2. Visit Database")
        print("3. Exit")
        try:
            choice = int(input("Enter: "))
        except ValueError:
            choice = -1
        match choice:
            case 1:
                elecCAL()
            case 2:
                dataBASE()
            case 3:
                exit()
                return
            case _:
                for i in range(1, 4):
                    print("\n[PLEASE ENTER A VALID INPUT]")

def elecCAL():
    customers = customersDC()
    print("\n[CALCULATE ELECTRIC BILL]")
    customers.customerNAME = input("Enter Customer Name: ")
    customers.meterID = int(input("\nEnter Meter ID: "))
    customers.classiFICT = input("\nEnter Classification: ")
    customers.prevREADING = float(input("\nEnter Previous Reading: "))
    customers.currREADING = float(input("\nEnter Current Reading: "))
    #bruh
    customers.totalKWU = customers.currREADING - customers.prevREADING
    if customers.classiFICT.lower() == "residential":
        if customers.totalKWU > 300:
            customers.misceCHAR = 0.8
            customers.ratePKU = 0.55
            customers.groAMT = customers.totalKWU * customers.ratePKU
            customers.totalAMT = customers.groAMT + customers.misceCHAR
            customersD.append(customers)
            SAVEDFILES()
            disPLAY()
        elif customers.totalKWU >= 100 and customers.totalKWU <= 299:
            customers.misceCHAR = 0.5
            customers.ratePKU = 0.55
            customers.groAMT = customers.totalKWU * customers.ratePKU
            customers.totalAMT = customers.groAMT + customers.misceCHAR
            customersD.append(customers)
            SAVEDFILES()
            disPLAY()
        elif customers.totalKWU < 100:
            customers.misceCHAR = 0
            customers.ratePKU = 0.55
            customers.groAMT = customers.totalKWU * customers.ratePKU
            customers.totalAMT = customers.groAMT + customers.misceCHAR
            customersD.append(customers)
            SAVEDFILES()
            disPLAY()
    elif customers.classiFICT.lower() == "commercial":
        if customers.totalKWU > 300:
            customers.misceCHAR = 0.8
            customers.ratePKU = 0.75
            customers.groAMT = customers.totalKWU * customers.ratePKU
            customers.totalAMT = customers.groAMT + customers.misceCHAR
            customersD.append(customers)
            SAVEDFILES()
            disPLAY()
        elif customers.totalKWU >= 100 and customers.totalKWU <= 299:
            customers.misceCHAR = 0.5
            customers.ratePKU = 0.75
            customers.groAMT = customers.totalKWU * customers.ratePKU
            customers.totalAMT = customers.groAMT + customers.misceCHAR
            customersD.append(customers)
            SAVEDFILES()
            disPLAY()
        elif customers.totalKWU < 100:
            customers.misceCHAR = 0
            customers.ratePKU = 0.75
            customers.groAMT = customers.totalKWU * customers.ratePKU
            customers.totalAMT = customers.groAMT + customers.misceCHAR
            customersD.append(customers)
            SAVEDFILES()
            disPLAY()

def dataBASE():
    try:
        print("\n[CUSTOMERS' DATABASE]")
        with open("customersPY.txt", "r") as reader:
            for line in reader:
                print(line.strip())
    except IOError:
        for _ in range(3):
            print("\n[ERROR]")

def disPLAY():
    for customers in customersD:
        print(f"Customer Name: {customers.customerNAME}")
        print(f"Total Kilowatt Usage: {customers.totalKWU:.2f} kWh")
        print(f"Rate Per Kilowatt: {customers.ratePKU:.2f} kWh")
        print(f"Gross Amount: {customers.groAMT:.2f} PHP")
        print(f"Miscellaneous Charges: {customers.misceCHAR:.2f} PHP")
        print(f"Total Amount Due: {customers.totalAMT:.2f} PHP")

def exit():
    print("\n[THANK YOU FOR USING!]")

def SAVEDFILES():
    try:
        with open("customersPY.txt", "w") as writer:
            for customers in customersD:
                writer.write(f"CUSTOMER NAME: {customers.customerNAME}\n")
                writer.write(f"METER ID: {customers.meterID}\n")
                writer.write(f"PREVIOUS READING: {customers.prevREADING:.2f} kWh\n")
                writer.write(f"CURRENT READING: {customers.currREADING:.2f} kWh\n")
                writer.write(f"TOTAL KILOWATT USAGE: {customers.totalKWU:.2f} kWh\n")
                writer.write(f"RATE PER KILOWATT: {customers.ratePKU:.2f} kWh\n")
                writer.write(f"GROSS AMOUNT: {customers.groAMT:.2f} PHP\n")
                writer.write(f"MISCELLANEOUS CHARGES: {customers.misceCHAR:.1f} PHP\n")
                writer.write(f"TOTAL AMOUNT DUE: {customers.totalAMT:.2f} PHP\n")
    except IOError:
        for _ in range(3):
            print("\n[ERROR]")

if __name__ == "__main__":
    main()